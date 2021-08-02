class Node:
    def __init__(self,data):
        self.data = data #Assing data
        self.next = None #Init, next as null
        #Node structure (data, none)

#Class linked list that contains a node object
class LinkedList:
    #Function to init the LL
    #List object
    def __init__(self):
        self.head = None
        #structure (Head, none)

    #we introduce a new node pointing to head.
    #Then we assert the new node as the new head.
    def push(self,new_data):
        new_node      = Node(new_data)
        new_node.next = self.head
        self.head     = new_node
    
    def deleteNode(self, prev_node):
        if prev_node is 
        if prev_node is None:
            print("The prev. node must be in the LinkedList")
        temp           = prev_node.next
        prev_node.next = temp.next


    def insterAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given prev. node must be in the LinkedList")
            return
        new_node       = Node(new_data)
        new_node.next  = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

l_list = LinkedList()

l_list.head = Node(1) #(1   , None)
second      = Node(2) #(2   , None)
third       = Node(3) #(3   , None)


l_list.head.next = second #Head   -> second : (1,2) -> (2,none)
second.next      = third  #second -> third  :  (2,4) -> (3,none)

l_list.insterAfter(second,7)
l_list.append(4)
l_list.printList(),print()

l_list.deleteNode(second)
l_list.printList()