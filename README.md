# Food-Recommendation-System
This comprehensive system recommend food items to user. It has two models implemented, one is landing page that recommend items to user in context-aware manner and another recommends food based on the food item previously selected by user.

Dataset: Instacart Market Basket Analysis [Link](https://www.kaggle.com/competitions/instacart-market-basket-analysis)  
Model used: DeepCTR [Link](https://github.com/shenweichen/DeepCTR)

Folder **Context-Aware-Recommendation** contains the code for recommending the food items based on the day of week and hour of day provided.  
Folder **RecSys** contains the trained model for context-aware recommendation.  
To use the trained model,
`
!pip install keras  
from keras import models  
loaded_model = models.load_model('/path/to/RecSys')
`

Steps:
1. Clone the repository  
`git clone https://github.com/yubraaj11/Food-Recommendation-System`  
2. Open code in any IDE, preferable VsCode
Change directory to "Context-Aware-Recommendation" Folder then run  
`python recommendation.py`
