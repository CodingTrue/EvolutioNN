from typing import Optional, Any, Self
from evolutionn.compute import compute_graph

class Tensor:
    def __init__(self, data: Optional[Any] = None):
        self._data = data

    def __add__(self, other): return Tensor.add_tensors(self, other)
    def __mul__(self, other): return Tensor.multiply_tensors(self, other)
    def __sub__(self, other): return Tensor.subtract_tensors(self, other)
    def __truediv__(self, other): return Tensor.divide_tensors(self, other)

    def __radd__(self, other): return Tensor.add_tensors(other, self)
    def __rsub__(self, other): return Tensor.subtract_tensors(other, self)
    def __rmul__(self, other): return Tensor.multiply_tensors(other, self)
    def __rtruediv__(self, other): return dTensor.ivide_tensors(other, self)

    @staticmethod
    def add_tensors(a: Any, b: Any):
        compute_graph.add_operation(function_identifier="add", data=(a, b))
        return Tensor(None)

    @staticmethod
    def multiply_tensors(a: Any, b: Any):
        compute_graph.add_operation(function_identifier="multiply", data=(a, b))
        return Tensor(None)

    @staticmethod
    def subtract_tensors(a: Any, b: Any):
        compute_graph.add_operation(function_identifier="subtract", data=(a, b))
        return Tensor(None)

    @staticmethod
    def divide_tensors(a: Any, b: Any):
        compute_graph.add_operation(function_identifier="divide", data=(a, b))
        return Tensor(None)