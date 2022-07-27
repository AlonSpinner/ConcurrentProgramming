import yaml
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path,'pipelines','wiki_yahoo_scrapper_pipeline.yaml'), 'r') as inFile:
    yaml_data = yaml.safe_load(inFile)

print(yaml_data.keys())


print(yaml_data['queues'])