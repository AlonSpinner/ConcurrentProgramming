import time
import os 
from workers.WikiWorker import WikiWorker
from yaml_reader import YamlPipelineExecutor

def main():
    scraper_start_time = time.time()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    pipeline_location = os.path.join(dir_path,'pipelines','wiki_yahoo_scrapper_pipeline.yaml')
    yamlPipelineExecutor = YamlPipelineExecutor(pipeline_location = pipeline_location)
    yamlPipelineExecutor.process_pipline()

    yamlPipelineExecutor._join_workers()

    print('Extracting time took:', round(time.time() - scraper_start_time, 1))

if __name__ == "__main__":
    main()
