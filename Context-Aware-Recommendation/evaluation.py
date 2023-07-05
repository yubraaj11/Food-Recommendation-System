from Recommendation import recommendation
import pandas as pd
from math import log2
csv_path = '../Dataset/Instacart_original.csv'

df = pd.read_csv(csv_path, index_col=0)

df1 = df[["order_dow", "order_hour_of_day", "product_name"]].copy()


day = int(input("Enter day: "))
hour = int(input("Enter hour: "))

pred_list = recommendation(day=day, hour=hour)
actual_list = df1.loc[(df1['order_dow'] == day) & (df['order_hour_of_day'] == hour), 'product_name'].tolist()


def precision_at_k(recommended_items, ground_truth_items , k ):
    """
    Calculates precision at k for a list of recommended items.
    
    Args:
        recommended_items (list): List of recommended items.
        ground_truth_items (list): List of ground truth items.
        k (int): Number of items to consider for calculating precision.
    
    Returns:
        float: Precision at k.
    
    Raises:
        ValueError: If k is less than or equal to 0.
    """
    recommended_k = recommended_items[:k]
    relevant_items = set(recommended_k) & set(ground_truth_items)
    precision = len(relevant_items) / float(k)
    return precision

def recall_at_k(recommended_items, ground_truth_items , k):
    """
    Calculates recall at k for a list of recommended items.
    
    Args:
        recommended_items (list): List of recommended items.
        ground_truth_items (list): List of ground truth items.
        k (int): Number of items to consider for calculating precision.
    
    Returns:
        float: Recall at k.
    
    Raises:
        ValueError: If k is less than or equal to 0.
    """
    recommended_k = recommended_items[:k]
    relevant_items = set(recommended_k) & set(ground_truth_items)
    recall = len(relevant_items) / float(len(ground_truth_items))
    return recall

def average_precision_at_k(recommended_items, ground_truth_items, k):
    """
    Calculates average precision at k for a list of recommended items.
    
    Args:
        recommended_items (list): List of recommended items.
        ground_truth_items (list): List of ground truth items.
        k (int): Number of items to consider for calculating precision.
    
    Returns:
        float: Average Precision at k.
    
    Raises:
        ValueError: If k is less than or equal to 0.
    """
    relevant_items = set(ground_truth_items)
    precision_sum = 0.0
    num_hits = 0

    for i in range(k):
        item = recommended_items[i]
        if item in relevant_items:
            num_hits += 1
            precision = num_hits / float(i + 1)
            precision_sum += precision

    average_precision = precision_sum / min(len(relevant_items), k)
    return average_precision

def hit_rate_at_k(recommended_items, ground_truth_items, k):
    """
    Calculates hitrate at k for a list of recommended items.
    
    Args:
        recommended_items (list): List of recommended items.
        ground_truth_items (list): List of ground truth items.
        k (int): Number of items to consider for calculating precision.
    
    Returns:
        float: Hitrate at k.
    
    Raises:
        ValueError: If k is less than or equal to 0.
    """
    recommended_k = recommended_items[:k]
    hits = set(recommended_k) & set(ground_truth_items)
    hit_rate = len(hits) / float(len(ground_truth_items))
    return hit_rate

def ndcg_at_k(recommended_items, ground_truth_items, k):
    """
    Calculates ndcg at k for a list of recommended items.
    
    Args:
        recommended_items (list): List of recommended items.
        ground_truth_items (list): List of ground truth items.
        k (int): Number of items to consider for calculating precision.
    
    Returns:
        float: nDCG at k.
    
    Raises:
        ValueError: If k is less than or equal to 0.
    """
    dcg = 0.0
    idcg = 0.0

    for i in range(k):
        item = recommended_items[i]
        if item in ground_truth_items:
            relevance = 1.0 / log2(i + 2)
            dcg += relevance
        idcg += 1.0 / log2(i + 2)

    ndcg = dcg / idcg
    return ndcg

def item_coverage_at_k(recommended_items, unique_items, k):
    """
    Calculates itemCoverage at k for a list of recommended items.
    
    Args:
        recommended_items (list): List of recommended items.
        unique_items (list): List of unique items.
        k (int): Number of items to consider for calculating precision.
    
    Returns:
        float: Item Coverage at k.
    
    Raises:
        ValueError: If k is less than or equal to 0.
    """
    recommended_k = recommended_items[:k]
    coverage = len(set(recommended_k)) / float(len(unique_items))
    return coverage

k=7
precision_at_k = precision_at_k(recommended_items=pred_list, ground_truth_items=actual_list, k=k)
recall_at_k = recall_at_k(recommended_items=pred_list, ground_truth_items=actual_list, k=k)
map_at_k = average_precision_at_k(recommended_items=pred_list, ground_truth_items=actual_list, k=k)
hit_at_k = hit_rate_at_k(recommended_items=pred_list, ground_truth_items=actual_list, k=k)
ndgc_at_k = ndcg_at_k(recommended_items=pred_list, ground_truth_items=actual_list, k=k)
itemcoverage_at_k = item_coverage_at_k(recommended_items=pred_list, unique_items=set(actual_list), k=k)

print(f"For day:{day} and hour:{hour} the evaluation metrics are:")
print(f"MAP@{k} :{map_at_k}")
print(f"Precision@{k} :{precision_at_k}")
print(f"Recall@{k} :{recall_at_k}")
print(f"Hit@{k} : {hit_at_k}")
print(f"nDCG@{k} : {ndgc_at_k}")
print(f"Itemcoverage@{k} : {itemcoverage_at_k}")