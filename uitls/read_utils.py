import os
import yaml

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")


def read_yaml():
    with open(data_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data


"""
if __name__ == '__main__':
   print(read_yaml())
"""



