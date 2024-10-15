from typing import Union
from Node import Node
class LinkedList:
    def __init__(self, value: Union[int, float]) -> None:
        new_Node  = Node(value)
        self.head = new_Node
        self.tail = new_Node