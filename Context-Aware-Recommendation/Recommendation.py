model_path = '../RecSys/'
from keras import models
import pickle
import numpy as np
import pandas as pd

loaded_model = models.load_model(model_path)
dict_path = '../Dataset/product_dict_v1.pkl'


df_path = '../Dataset/Instacart_original.csv'
instacart_df = pd.read_csv(df_path)

# # if __name__ == "__main__":
def recommendation(day: int, hour: int) -> list:
    
    product_score = {}

    with open (dict_path, 'rb') as file:
        loaded_dict = pickle.load(file)


    bigger_dict = {
    'order_dow': [],
    'order_hour_of_day': [],
    'product_id': [],
    'aisle_id': [],
    'department_id': []
    }

    for product_id, (aisle_id, department_id) in loaded_dict.items():
        bigger_dict['order_dow'].append(day)
        bigger_dict['order_hour_of_day'].append(hour)
        bigger_dict['product_id'].append(product_id)
        bigger_dict['aisle_id'].append(aisle_id)
        bigger_dict['department_id'].append(department_id)

    for key in bigger_dict:
        bigger_dict[key] = np.array(bigger_dict[key])

    # # creating a dictionary; product_id as key and predicted score as value
    pred_ans = loaded_model.predict(bigger_dict, batch_size=2965)
    for key, value in zip(loaded_dict.keys(), pred_ans):
        product_score[key] = value

    # print(product_score)


    # Sorting the product_id and score in the dictionary based on the score value and getting top 10 highest only    
    sorted_items = sorted(product_score.items(), key=lambda x: x[1], reverse=True)
    top_10 = sorted_items[:10]


    # Recommending products to the user based on the day and hour provided by them
    print("\n ***************Recommending*************** \n")

    product_list  = []
    for key, value in top_10:
        # print(key)
        product_name = instacart_df.loc[instacart_df['product_id'] == key, 'product_name'].iloc[0]
        product_list.append(product_name) 
    
    return product_list


# recommendation(4, 12)