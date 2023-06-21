model_path = '/RecSys'
from keras import models

loaded_model = models.load(model_path)


if __name__ == "__main__":
    print('yes')