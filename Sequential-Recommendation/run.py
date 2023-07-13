from recbole.quick_start import run_recbole
from recbole.config import Config
from recbole.data import create_dataset, data_preparation
from recbole.utils import init_logger, init_seed
from logging import getLogger
from recbole.model.sequential_recommender import NextItNet
from recbole.trainer import Trainer

parameter_dict = {
    'train_neg_sample_args': None,
}

if __name__ == "__main__":
    config = Config(model='NextItNet',
                    dataset='dataset',
                    config_file_list=['test.yaml'],
                    config_dict=parameter_dict)



    init_seed(config['seed'], config['reproducibility'])

    r'''
        Logger Initialized
    '''
    init_logger(config)
    logger = getLogger()
    

    logger.info(config)

    r'''
    Dataset created and info is logged.
    '''
    dataset = create_dataset(config)
    logger.info(dataset)

    train_data, valid_data, test_data = data_preparation(config, dataset)

    model = NextItNet(config, train_data.dataset)
    logger.info(model)
    
    trainer = Trainer(config, model)

    best_valid_score, best_valid_result = trainer.fit(train_data)

