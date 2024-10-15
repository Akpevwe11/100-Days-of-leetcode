from typing import Union
class Node:
    def __init__(self, value: Union[int, float]) -> None:
        self.value = value 
        self.next = None