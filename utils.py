import os

def check_and_create_result():
    result_path = '../results'
    if not os.path.exists(result_path):
        os.makedirs(result_path)
    return result_path