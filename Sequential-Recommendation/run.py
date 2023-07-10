from recbole.quick_start import run_recbole

parameter_dict = {
    'train_neg_sample_args': None,
}
run_recbole(model='NextItNet', dataset="data1/dataset/", config_file_list=['test.yaml'])