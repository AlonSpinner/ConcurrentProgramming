import yaml
from multiprocessing import Queue
import importlib

class YamlPipelineExecutor():
    def __init__(self, pipeline_location) -> None:
        self._pipeline_location = pipeline_location
        self._queues = {}
        self._workers = {}

    def _load_pipeline(self):
        with open(self._pipeline_location, 'r') as inFile:
            self._yaml_data = yaml.safe_load(inFile)
            
    def _initalize_queues(self):
        for queue in self._yaml_data['queues']:
            queue_name = queue['name']
            self._queues[queue_name] = Queue()

    def _initalize_workers(self):
        for worker in self._yaml_data['workers']:
            WorkerClass = getattr(importlib.import_module(worker['location']), worker['class'])
            input_queue = worker.get('input_queue')
            output_queues = worker.get('output_queues')
            worker_name = worker['name']
            num_instances = worker.get('instances', 1)

            init_params = {
                'input_queue': self._queues[input_queue] if input_queue is not None else None,
                'output_queue': [self._queues[output_queue] for output_queue in output_queues] \
                    if output_queues is not None else None
            }

            self._workers[worker_name] = []
            for _ in range(num_instances):
                self._workers[worker_name].append((WorkerClass(**init_params)))

    def _join_workers(self):
        for worker_name in self._workers:
            for worker_thread in self._workers[worker_name]:
                worker_thread.join()
    
    def process_pipline(self):
        self._load_pipeline()
        self._initalize_queues()
