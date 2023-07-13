class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next    ## pointer to another node or None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last_node = None
    
    ## display method
    ## iterative , can I rewrite w/ recurssive
    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next
        ll_string += " None"
        print(ll_string)
    
    ## recursive func for above print
    def recur_print(self, node):
        if node is None:
            return " None"
        return f" {str(node.data)} ->" + self.recur_print(node.next)
        
    ## insert beginning(head)
    def insert_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
    

ll = LinkedList()
node4 = Node("data4", None)
node3 = Node("data3", node4)
node2 = Node("data2", node3)
node1 = Node("data1", node2)

ll.head = node1

ll.insert_beginning("heyyy")
ll.insert_beginning("yoooo")

# ll.print_ll()
print(ll.recur_print(ll.head))