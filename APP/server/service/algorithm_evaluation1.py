import json
import subprocess
import re
import math
from typing import List, Dict

# copy the same tokenization logic from search_algorithm_irish.py
INITAL_MUTATIONS = {
    # nasalisation
    'ng': 'g', 'mb': 'b', 'nd': 'd',
    'na': 'a', 'ne': 'e', 'ni': 'i', 'no': 'o', 'nu': 'u',
    # lenition
    'ch': 'c', 'ph': 'p', 'th': 't', 
    'ḟ': 'f', 'fh': 'f', 'ṡ': 's', 'sh': 's',
    # gemination
    'll': 'l', 'nn': 'n', 'rr': 'r', 'mm': 'm', 'ss': 's',
}

def apply_irish_mutations(word):
    """Apply Irish initial mutations to normalize word forms"""
    if len(word) == 0:
        return word
        
    # Handle special dotted characters
    if word[0] == 'ḟ':  
        word = 'f' + word[1:]
    if word[0] == 'ṡ':
        word = 's' + word[1:]
        
    # Handle two-character mutations
    if len(word) >= 2:  
        replacement = INITAL_MUTATIONS.get(word[:2], '')
        if replacement:
            word = replacement + word[2:] 
    return word

def tokenization_with_mutations(text):
    """use the same tokenization method as search_algorithm_irish.py"""
    words = []
    for match in re.finditer(r'\b[a-zA-ZḟṡáéíóúÁÉÍÓÚ]+\b', text):
        word = match.group(0).lower()
        normalized_word = apply_irish_mutations(word)
        words.append(normalized_word)
    return words

def calculate_f1_score(result_text: str, ground_truth: str) -> float:
    """
    calculate the F1 score (consider the frequency)
    precision = the number of correctly predicted words / the total number of predicted words
    recall = the number of correctly predicted words / the total number of true words
    """
    from collections import Counter
    
    result_words = tokenization_with_mutations(result_text)
    ground_truth_words = tokenization_with_mutations(ground_truth)
    
    if len(result_words) == 0 and len(ground_truth_words) == 0:
        return 1.0
    
    if len(result_words) == 0 or len(ground_truth_words) == 0:
        return 0.0
    
    # count the frequency of the words
    result_counter = Counter(result_words)
    ground_truth_counter = Counter(ground_truth_words)
    
    # calculate the number of correctly predicted words (consider the frequency)
    correct_predictions = 0
    for word, count in result_counter.items():
        if word in ground_truth_counter:
            correct_predictions += min(count, ground_truth_counter[word])
    
    # calculate the precision and recall
    precision = correct_predictions / len(result_words)
    recall = correct_predictions / len(ground_truth_words)
    
    if precision + recall == 0:
        return 0.0
    
    # calculate the F1 score
    f1 = 2 * (precision * recall) / (precision + recall)
    return f1

def call_search_algorithm(article_file: str, query: str, window_size: float, step: int, dissimilarity_threshold: float, top_k: int) -> List[Dict]:
    """call the search_algorithm_irish.py"""
    try:
        # call the search_algorithm_irish.py
        cmd = [
            'python3', 'search_algorithm_irish.py',
            article_file,      # sys.argv[1]
            query,             # sys.argv[2]
            str(window_size),  # sys.argv[3]
            str(step),         # sys.argv[4]
            str(dissimilarity_threshold),  # sys.argv[5]
            str(top_k)         # sys.argv[6]
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode != 0:
            print(f"algorithm call error: {result.stderr}")
            return []
        
        return json.loads(result.stdout)
        
    except Exception as e:
        print(f"call error: {e}")
        return []

def evaluate_single_query(article: str, query: str, ground_truth: str, window_size: float, step: int) -> float:
    """
    evaluate a single query
    get the top-3 results → calculate the F1 score for each result → select the highest score
    """
    results = call_search_algorithm(article, query, window_size, step, 3.0, 3)
    
    if not results:
        return 0.0
    
    best_f1 = 0.0
    for result in results:
        f1 = calculate_f1_score(result['text'], ground_truth)
        best_f1 = max(best_f1, f1)
    
    return best_f1

def main():
    print("start Irish algorithm evaluation...")
    
    # load the acSen.json data
    with open('acSen.json', 'r', encoding='utf-8') as f:
        acsen_data = json.load(f)
    
    print(f"loaded {len(acsen_data['blocks'])} queries")
    
    # 4 parameter combinations: large/small window × exact/fuzzy search
    param_combinations = [
        {"name": "exact window exact search", "window_size": 1.0, "step_type": "exact"},


    ]
    
    with open("clnMedIrish_extracted.txt", "r") as file:
        clnMedIrish_extracted = file.read()

    results = {}
    
    for param in param_combinations:
        print(f"\n=== evaluate: {param['name']} ===")
        print(f"parameters: window_size={param['window_size']}, step_type={param['step_type']}")
        
        f1_scores = []
        
        for i, block in enumerate(acsen_data['blocks']):
            query = block['clnModIrish']    # query: acSen's medIrish
            ground_truth = block['clnMedIrish']  # ground truth: acSen's clnModIrish
            
            # calculate the step parameter
            if param['step_type'] == 'exact':
                step = 1
            else:  # fuzzy
                query_tokens = tokenization_with_mutations(query)
                step = max(1, math.ceil(len(query_tokens) * 0.5))  # round up
            
            # evaluate this query
            f1_score = evaluate_single_query(clnMedIrish_extracted, query, ground_truth, param['window_size'], step)
            f1_scores.append(f1_score)
            
            # update the progress
            if (i + 1) % 50 == 0:
                current_mean = sum(f1_scores) / len(f1_scores)
                print(f"progress: {i + 1}/522, current mean F1: {current_mean:.4f}")
        
        # calculate the mean accuracy
        mean_accuracy = sum(f1_scores) / len(f1_scores)
        results[param['name']] = {
            'mean_accuracy': mean_accuracy,
            'individual_scores': f1_scores,
            'parameters': param
        }
        
        print(f"{param['name']} - mean accuracy: {mean_accuracy:.4f}")
    
    # save the results          
    with open('rever_evaluation_results6.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print("\n=== evaluation completed ===")
    for name, result in results.items():
        print(f"{name}: {result['mean_accuracy']:.4f}")
    
    print(f"results saved to: rever_evaluation_results5.json")

if __name__ == "__main__":
    main()