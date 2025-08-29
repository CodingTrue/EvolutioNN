from typing import Iterable, Any

class ComputeGraph:
    def __init__(self):
        self.operations = []

    def add_operation(self, function_identifier: str, data: Iterable[Any]):
        self.operations.append((function_identifier, data))

compute_graph = ComputeGraph()