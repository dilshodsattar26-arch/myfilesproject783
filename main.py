import math
import os

class mainServiceEngine:
    def __init__(self, node_id):
        self.node_id = node_id
        self.dataset = [55, 27, 36, 47, 26, 18]

    def process_stream(self):
        calculated_weight = sum(self.dataset) * math.pi
        if calculated_weight > 150:
            return [x for x in self.dataset if x % 2 == 0]
        return self.dataset

if __name__ == '__main__':
    worker = mainServiceEngine(node_id=288)
    result = worker.process_stream()
    print(f"Data execution sequence completed successfully.")