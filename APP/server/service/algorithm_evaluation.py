import json
import subprocess
import re
import math
from typing import List, Dict

# 从search_algorithm_irish.py复制相同的tokenization逻辑
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
    """使用与search_algorithm_irish.py完全相同的tokenization方法"""
    words = []
    for match in re.finditer(r'\b[a-zA-ZḟṡáéíóúÁÉÍÓÚ]+\b', text):
        word = match.group(0).lower()
        normalized_word = apply_irish_mutations(word)
        words.append(normalized_word)
    return words

def calculate_f1_score(result_text: str, ground_truth: str) -> float:
    """
    计算F1分数（考虑词频）
    精确率 = 预测正确的词数 / 预测词总数
    召回率 = 预测正确的词数 / 真实词总数
    """
    from collections import Counter
    
    result_words = tokenization_with_mutations(result_text)
    ground_truth_words = tokenization_with_mutations(ground_truth)
    
    if len(result_words) == 0 and len(ground_truth_words) == 0:
        return 1.0
    
    if len(result_words) == 0 or len(ground_truth_words) == 0:
        return 0.0
    
    # 统计词频
    result_counter = Counter(result_words)
    ground_truth_counter = Counter(ground_truth_words)
    
    # 计算正确预测的词数（考虑频次）
    correct_predictions = 0
    for word, count in result_counter.items():
        if word in ground_truth_counter:
            correct_predictions += min(count, ground_truth_counter[word])
    
    # 计算精确率和召回率
    precision = correct_predictions / len(result_words)
    recall = correct_predictions / len(ground_truth_words)
    
    if precision + recall == 0:
        return 0.0
    
    # 计算F1分数
    f1 = 2 * (precision * recall) / (precision + recall)
    return f1

def call_search_algorithm(article_file: str, query: str, window_size: float, step: int, dissimilarity_threshold: float, top_k: int) -> List[Dict]:
    """调用search_algorithm_irish.py"""
    try:
        # 按照search_algorithm_irish.py的main()函数参数顺序调用
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
            print(f"算法调用错误: {result.stderr}")
            return []
        
        return json.loads(result.stdout)
        
    except Exception as e:
        print(f"调用异常: {e}")
        return []

def evaluate_single_query(article: str, query: str, ground_truth: str, window_size: float, step: int) -> float:
    """
    评估单个查询
    获取Top-3结果 → 分别计算每个结果与标准答案的F1分数 → 选取最高分
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
    print("开始Irish算法评估...")
    
    # 加载acSen.json数据
    with open('acSen.json', 'r', encoding='utf-8') as f:
        acsen_data = json.load(f)
    
    print(f"加载了 {len(acsen_data['blocks'])} 条查询数据")
    
    # 4种参数组合：大/小窗口 × 精确/模糊搜索
    param_combinations = [
        {"name": "大窗口精确搜索", "window_size": 1.0, "step_type": "exact"},
        {"name": "大窗口模糊搜索", "window_size": 1.0, "step_type": "fuzzy"},
        {"name": "小窗口精确搜索", "window_size": 0.6, "step_type": "exact"},
        {"name": "小窗口模糊搜索", "window_size": 0.6, "step_type": "fuzzy"}
    ]
    
    with open("clnModIrish_extracted.txt", "r") as file:
        clnModIrish_extracted = file.read()

    results = {}
    
    for param in param_combinations:
        print(f"\n=== 评估: {param['name']} ===")
        print(f"参数: window_size={param['window_size']}, step_type={param['step_type']}")
        
        f1_scores = []
        
        for i, block in enumerate(acsen_data['blocks']):
            query = block['clnMedIrish']    # 查询：acSen的medIrish
            ground_truth = block['clnModIrish']  # 标准答案：acSen的clnModIrish
            
            # 计算step参数
            if param['step_type'] == 'exact':
                step = 1
            else:  # fuzzy
                query_tokens = tokenization_with_mutations(query)
                step = max(1, math.ceil(len(query_tokens) * 0.5))  # 向上取整
            
            # 评估此查询
            f1_score = evaluate_single_query(clnModIrish_extracted, query, ground_truth, param['window_size'], step)
            f1_scores.append(f1_score)
            
            # 进度更新
            if (i + 1) % 50 == 0:
                current_mean = sum(f1_scores) / len(f1_scores)
                print(f"进度: {i + 1}/522, 当前平均F1: {current_mean:.4f}")
        
        # 计算平均准确率
        mean_accuracy = sum(f1_scores) / len(f1_scores)
        results[param['name']] = {
            'mean_accuracy': mean_accuracy,
            'individual_scores': f1_scores,
            'parameters': param
        }
        
        print(f"{param['name']} - 平均准确率: {mean_accuracy:.4f}")
    
    # 保存结果          
    with open('evaluation_results4.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print("\n=== 评估完成 ===")
    for name, result in results.items():
        print(f"{name}: {result['mean_accuracy']:.4f}")
    
    print(f"详细结果已保存到: evaluation_results5.json")

if __name__ == "__main__":
    main()