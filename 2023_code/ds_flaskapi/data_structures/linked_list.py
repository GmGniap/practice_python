class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next    ## pointer to another node or None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last_node = None
    
    def to_list(self):
        lst = []
        if self.head is None:
            return lst
        
        node = self.head
        while node:
            lst.append(node.data)
            node = node.next
        return lst
            
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
        ## Modify : starting from beginning, track last_node
        if self.head is None:
            self.head = Node()
            self.last_node = self.head

        ## simple
        new_node = Node(data, self.head)
        self.head = new_node
    
    def insert_at_end(self, data):
        
        if self.head is None:
            self.insert_beginning(data)
            return
        ## comment - if statement (check readme)
        '''
        if self.last_node is None:
            ## starting from head
            node = self.head        
            ## transverse through linked list
            while node.next:
                node = node.next
            node.next = Node(data, None) ## next will always be None because we insert at the end
            self.last_node = node.next
        '''
        
        self.last_node.next = Node(data, None)
        self.last_node = self.last_node.next ## need to assign last node
        
            
    
'''General test
ll = LinkedList()
node4 = Node("data4", None)
node3 = Node("data3", node4)
node2 = Node("data2", node3)
node1 = Node("data1", node2)

ll.head = node1

ll.insert_beginning("heyyy")
ll.insert_beginning("yoooo")
ll.insert_at_end("endddd1")

ll.print_ll()
print(ll.recur_print(ll.head))
print(ll.last_node.data)
print("--xx--")
ll.insert_at_end("222end")
ll.print_ll()
print(ll.last_node.data)
print(ll.last_node.next)
'''