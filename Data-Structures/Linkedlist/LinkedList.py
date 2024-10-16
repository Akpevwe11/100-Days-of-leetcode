from typing import Union
from Node import Node
class LinkedList:
    def __init__(self, value: Union[int, float]) -> None:
        new_Node  = Node(value)
        self.head = new_Node
        self.tail = new_Node
        self.length = 1


if __name__ == "__main__":
    linked_list = LinkedList(10)
    print(f"Linked List: {linked_list}")