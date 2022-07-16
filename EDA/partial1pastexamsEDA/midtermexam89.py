#JIAHAO CHEN G.89


class DNode:
  def __init__(self,elem,next=None,prev=None ):
    self.elem = elem
    self.next = next
    self.prev = prev
    
class MyDList():
    
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
     
    def append(self,e):
        """Add a new element, e, at the end of the list"""
        #create the new node
        newNode=DNode(e)
        
        if self._size==0:
            self._head=newNode
        else:
            newNode.prev=self._tail
            self._tail.next=newNode
        
        #update the reference of head to point the new node
        self._tail=newNode
        #increase the size of the list  
        self._size+=1
        
    def __len__(self):
        return self._size
    
    
   
    def __str__(self):
        """Returns a string with the elements of the list"""
        nodeIt=self._head
        result='['
        while nodeIt:
            result+= str(nodeIt.elem)+ ", "
            nodeIt=nodeIt.next
        
        if len(result)>1:
            result=result[:-2]

        result+=']'
        return result


                   

    def checkSequentialEven(self):
        """
        The problem can be tacked taking two steps:

        1) Delete the uneven nodes
        2) Complete the sequence with missing even nodes between two nodes

        #The list is sorted

        """

        """
        
        My 1º Solution to the problem
        
        current = self._head

        #First Loop: Remove the elements that are not even

        while current:#while the node exists
            if current.elem % 2 != 0: #if the node is odd
                #delete the node 
                if current == self._head: #if the node is at the beginning of the list 
                    self._head = self._head.next #the new head will the the next one 
                    if self._head == None: #if the next one is None, the list is empty and the tail is None also 
                        self._tail = None 
                    else: #head is a new node, we set its previous node to None 
                        self._head.prev = None
                else: #the node is not in the middle of the list  
                    current.prev.next = current.next #we jump over the current node, to do it, we set that the next node of the previous node is the next node of the current node 
                    if current.next: #if the next one is a node, we say that the prev of this node is the previous node of the current node
                        current.next.prev = current.prev
                    else: #if next one is not a node, None. We are at the end of the list, the new tail of the list is the previous node of the current node
                        self._tail = current.prev
                        self._tail.next = None
                self._size -= 1 #decrease the size because a node is removed 
            
            current = current.next #we go to the next node of the list 

        current = self._head

        #Second loop: complete the sequence

        while current:
            if current != self._head:
                if current.elem != current.prev.elem + 2:

                    current.prev.next = DNode(current.prev.elem +2)

                    current.prev.next.next = current

                    current.prev = current.prev.next

                    self._size += 1

                    current = current.prev

            current = current.next
        """

        #Second solution: reducing half of Time Complexity of the 1º Solution

        current = self._head
        last = None

        while current:  # while the node exists
            # Remove the elements that are not even
            if current.elem % 2 != 0:  # if the node is odd
                # delete the node
                if current == self._head:  # if the node is at the beginning of the list
                    self._head = self._head.next  # the new head will the the next one
                    if self._head == None:  # if the next one is None, the list is empty and the tail is None also
                        self._tail = None
                    else:  # head is a new node, we set its previous node to None
                        self._head.prev = None
                else:  # the node is not in the middle of the list
                    current.prev.next = current.next  # we jump over the current node, to do it, we set that the next node of the previous node is the next node of the current node
                    if current.next:  # if the next one is a node, we say that the prev of this node is the previous node of the current node
                        current.next.prev = current.prev
                    else:  # if next one is not a node, None. We are at the end of the list, the new tail of the list is the previous node of the current node
                        self._tail = current.prev
                        self._tail.next = None
                self._size -= 1  # decrease the size because a node is removed
            else: #if the node is not odd,the odd nodes before this even node are all deleted
                #complete the sequence if neccesary

                if current != self._head: #if current node is not at the beginning, the first even number will never fullfil the conditional because it can't be possible that the node at the beginning of the list is not even after the first part

                    if current.elem != last + 2: #if a even number is lost between the last even number and the current even number

                        current.prev.next = DNode(last + 2) #create a new even number node

                        current.prev.next.next = current #the next of the new node is the current one

                        current.prev = current.prev.next #the previous node of the current one is the new node

                        self._size += 1 #increase the size

                        current = current.prev #go back 1 step to subtract the effect of advancing one node later, because there might be more missing even number between the new added node and the current node

                last = current.elem #the last previous even number

            current = current.next  # we go to the next node of the list





