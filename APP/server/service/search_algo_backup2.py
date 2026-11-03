import Levenshtein
import sys
import json
import re
import os

# Add the rule-based directory to the path to import the lemmatizer
rule_based_dir = os.path.join(os.path.dirname(__file__), 'rule-based')
sys.path.append(rule_based_dir)

# Change to rule-based directory before importing lemmatizer
original_cwd = os.getcwd()
os.chdir(rule_based_dir)
from lemmatizer import Lemmatizer
os.chdir(original_cwd)

# # removing punctuations and numbers
# sym_and_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


# INITAL_MUTATIONS = {
#     #nasalisation
#     'ng': 'g', 'mb': 'b', 'nd': 'd',
#     'na': 'a', 'ne': 'e', 'ni': 'i', 'no': 'o', 'nu': 'u',
#     #lenition
#     'ch': 'c', 'ph': 'p', 'th': 't', 
#     'ḟ': 'f', 'fh': 'f', 'ṡ': 's', 'sh': 's',
#     #gemination
#     'll': 'l', 'nn': 'n', 'rr': 'r', 'mm': 'm', 'ss': 's',
# }



def tokenization(line):
    total_words = []
    for w in line:
        if w in sym_and_num:
            line = line.replace(w, "")
    if line.endswith('.'):
        line = line[:-1]
    line = line.lower()
    words = line.split()
    total_words += words
    return total_words

# def tokenization_irish(line):
#     total_words = []
#     for w in line: 
#         if w in sym_and_num:
#             line = line.replace(w, "")
#     if line.endswith('.'):
#         line = line[:-1]
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         if word[0] == 'ḟ':  
#             word = 'f' + word[1:]
#         if word[0] == 'ṡ':
#             word = 's'+ word[1:]
#         if len(word) >= 2:  
#             replacement = INITAL_MUTATIONS.get(word[:2],'')
#             if replacement:
#                 word = replacement+word[2:] 

#         total_words.append(word)

#     return total_words

def preprocess_irish_with_lemmatizer(text):
    """
    Apply rule-based lemmatization to Irish text and return both original and lemmatized text
    """
    original_cwd = os.getcwd()
    rule_based_dir = os.path.join(os.path.dirname(__file__), 'rule-based')
    os.chdir(rule_based_dir)
    
    try:
        # Create lemmatizer instance and get lemmatized text
        lemmatizer = Lemmatizer(text, method='predict')
        lemmatized_text = lemmatizer.lemmaText.strip()
        return lemmatized_text
    except Exception as e:
        print(f"Error in lemmatization: {e}", file=sys.stderr)
        return text  # Return original text if lemmatization fails
    finally:
        # Restore original working directory
        os.chdir(original_cwd)

def map_lemmatized_to_original_positions(original_text, lemmatized_text):
    """
    Create a mapping from lemmatized text positions back to original text positions
    """
    original_words = []
    original_indices = []
    
    # Get original word positions
    for match in re.finditer(r'\b\w+\b', original_text):
        original_words.append(match.group(0).lower())
        original_indices.append((match.start(), match.end()))
    
    # Get lemmatized word positions
    lemmatized_words = []
    lemmatized_indices = []
    for match in re.finditer(r'\b\w+\b', lemmatized_text):
        lemmatized_words.append(match.group(0).lower())
        lemmatized_indices.append((match.start(), match.end()))
    
    # Create mapping: lemmatized token index -> original text position
    position_mapping = {}
    
    # Simple alignment: assume one-to-one mapping by position
    # This works for most cases where lemmatization doesn't change word count significantly
    for i, (lem_start, lem_end) in enumerate(lemmatized_indices):
        if i < len(original_indices):
            position_mapping[i] = original_indices[i]
        else:
            # If lemmatized has fewer words, map to last original position
            position_mapping[i] = original_indices[-1] if original_indices else (0, 0)
    
    return position_mapping


def tokenization_with_index(line):
    words = []
    indices = []
    for match in re.finditer(r'\b\w+\b', line):
        words.append(match.group(0).lower()) 
        indices.append((match.start(), match.end())) 
    return words, indices



def moving_window_similarity1(target_words, total_words, actual_window_size, step=1, top_k=1):

    # 确保窗口大小不超过源文本长度
    if actual_window_size > len(total_words):
        actual_window_size = len(total_words)
        # print(f"Warning: Adjusted window size to {actual_window_size} (source text length)")
    
    # 如果没有足够的文本进行比较，返回特殊值
    if len(total_words) == 0 or actual_window_size == 0:
        return [(0, 1.0)]  # 返回索引0和最大不相似度1.0
    
    # 使用最大堆来保存top-k结果（python的heapq是最小堆，所以存储负分数来实现最大堆）
    top_results = []
    
    # 使用步长step移动窗口
    for i in range(0, len(total_words)-actual_window_size+1, step):
        matrix = [[float("inf") for _ in range(actual_window_size)] for _ in range(len(target_words))]
        source_words = total_words[i:i+actual_window_size]
        for k in range(len(target_words)):
            for j in range(len(source_words)):
                score = Levenshtein.distance(target_words[k],source_words[j]) / max(len(target_words[k]), len(source_words[j]))

                matrix[k][j] = score



        # 接下来计算每个矩阵中的分数
        dissimilarity_scores = calculate_dissimilarity_score(matrix, actual_window_size)
        score = sum(dissimilarity_scores) / len(target_words)  # 归一化到0-1之间

        top_results.append((score, i))

    # 排序结果，保证按分数从小到大返回
    return sorted(top_results)


def calculate_dissimilarity_score(matrix, actual_window_size):

    results = []

    for _ in range(len(matrix)):
        current_min_val = float("inf")
        min_row, min_col = -1,-1
        for r in range(len(matrix)):
            for c in range(actual_window_size):
                if matrix[r][c] < current_min_val:
                    current_min_val = matrix[r][c]
                    min_row = r
                    min_col = c
        
        if min_row == -1:
            break
        
        results.append(current_min_val)

        # 修正：将所有在min_row行的元素设为无穷大
        for c in range(actual_window_size):
            matrix[min_row][c] = float('inf')
        
        # 修正：将所有在min_col列的元素设为无穷大
        for r in range(len(matrix)):
            matrix[r][min_col] = float('inf')
    return results


def main():

    # Get parameters
    article = 'Laa ro boi cond i temraig iar ndioth dona rigaib atracht matin moch for ríraith na temrach ria turcbail gréine 7 a tri druith aroen ris .i. maol bloc bluicne. et a trii filid .i. ethain corb cesarn. Fodegh attraigesiom cach dia in lion sen do airdecin arna gabdaois fir side for erind cen airiugud dosom in dú dia ndéchaidsom do gres co tarlaic cloich and foa cosaib 7 saltrais fuirri. Ro ges an cloch fo cosaib co clos fo temraig uili 7 fo bregaib. Is and sin ro iarfacht conn dia druidib qui arusges an cloch cia hainm 7 can do ralad 7 no ragad 7 quid ro taraill temraigh. IS ed ro bert an drai fri conn ni slondad do co cent .l. laithi 7 a tri. IN tan ro cindiod an airiom sin. Rusiarfacht conn don drai afridhisi. Is ann adbert an drai. Fal anmaim na cloche. INis foail asatardad. Temair tiri fail i forromadh. Tir taillten a nairisfe co brath et is i an tir sen bus oenach cluiche cen uhes flaithios a temraig 7 la deginach an aonaigh in flaith nachus faigfi bid truú isan bliadain sin. Ro ges fal foat cosaibse annu ol in drai 7 dorairngert an lin gairm ro ges an cloch is ed lion rig bias dot siol co brath. Niba me nodsloindfe det ol in drai. A mbatar ierum co nacotar ciuich moir immaquairt conna fedotar quid docotar ar med an dorchu dusnainecc co colatar trethan in marcaigh ara namus. Moar mairc duinn ol conn diana ruccai a tir nainiuil. Ier sin dolleci an marcach tri orchora cucai 7 is traide dusnainic in torchor degenach inas torchor toísech. IS do guin rig emh or in drai cibe dibraicius conn a temraig. Anaid iar sin an marcach din dibraccud 7 tic cuca 7 ferais failti fri conn et congart les dia treb duscotar iarum. Condusrulai isin mag nalaind. Co nacatar an righraith isin maig 7 bili orda ina dorus 7 co nacatar tech nalaind nann fo octæ findraine .x. traigid .xx. a fod. Lotar iarum isin tech co nacatar an ingen macdachta isin toig 7 barr orda fora mullach. Dabach aircait co cerclaib orda impe 7 si lan do derglind escrai oir fora ur. copan di ór for a beolai. Co nacatar an scal fodeisin isin tigh fora cinn ina rigṡuide. Ni frith a temraich riam fer a mede nach a caoime ar aille a crotha ar inganta a deuluha. Prisgartside doib 7 adbert friu nidom scalsa em 7 nidom urtrach 7 domuirdercus duib iar mbas dodeochadus 7 is do cinel adaim daum. iss e mo slondad lug mac ethlend maic tigernmais. Is do dodechadus co necsi dedse saogal do flathau fen 7 cech flathai bias a temraich 7 ba si an ingen boi isin tig fora ciond flaithi erenn co prath. Ba si an ingen dobert an diched do cond .i. damasna 7 torcasnai cetri traigid .xx. fod an damhasna. ocht traigid itir a tuaim 7 talmain. IN tan luid an ingen don dail adbert friu. Cia da tibertar an airdeochsa. Friscart an scal. o ro sluindside cach flaith o cund co brath. Lotar a foscadh an (fo. 71b) scail cona rathaicsetar an rath nac an tec. Forracbad lia cond in dubach 7 int escrai ordao 7 and airech. IS de sin attá aisling an scail et egtrai 7 targraide cuind.'
    search_query = 'Laa ro bui cond i temraich iar ndith dona rigaib atraracht matin moch for aith na temrach ria turcbáil gréni 7 a tri druid ríam .i. mæl 7 blouc 7 bluiccniu. Eochaid 7 corbb 7 cessarnd in filid 7 cond fadeissin.'
    
    window_size = 1.3
    step_size = 1
    dissimilarity_threshold = 0.8
    top_k = 10

    # First apply lemmatization for Irish text
    lemmatized_search_query = preprocess_irish_with_lemmatizer(search_query)
    lemmatized_article = preprocess_irish_with_lemmatizer(article)
    
    # Create position mapping from lemmatized to original text
    position_mapping = map_lemmatized_to_original_positions(article, lemmatized_article)

    target_words = tokenization(lemmatized_search_query)

    article_tokens, token_indices = tokenization_with_index(lemmatized_article)

    actual_window_size = max(1, int(len(target_words) * window_size))

    if target_words == []:
        print(json.dumps([]))  
        return
    top_results = moving_window_similarity1(target_words, article_tokens, actual_window_size, step_size, top_k)
    
    # 显示top-k结果
    filtered_results = []
    for rank, (score, index) in enumerate(top_results[:top_k]):
        if score <= dissimilarity_threshold:
            if index + actual_window_size <= len(article_tokens):
                # Map back to original text positions
                start_token_idx = index
                end_token_idx = index + actual_window_size - 1
                
                # Get original text positions
                if start_token_idx in position_mapping and end_token_idx in position_mapping:
                    start_pos = position_mapping[start_token_idx][0]
                    end_pos = position_mapping[end_token_idx][1]
                    text_snippet = article[start_pos:end_pos]
                else:
                    # Fallback: use lemmatized text positions
                    start_pos = token_indices[index][0]
                    end_pos = token_indices[index+actual_window_size-1][1]
                    text_snippet = lemmatized_article[start_pos:end_pos]
            else:
                start_token_idx = index
                if start_token_idx in position_mapping:
                    start_pos = position_mapping[start_token_idx][0]
                    text_snippet = article[start_pos:]
                else:
                    # Fallback: use lemmatized text
                    start_pos = token_indices[index][0]
                    text_snippet = lemmatized_article[start_pos:]
            
            filtered_results.append({
                    "text": ''.join(text_snippet),
                    "score": score
                })
    
    print(json.dumps(filtered_results))
            
if __name__ == "__main__":
    main()