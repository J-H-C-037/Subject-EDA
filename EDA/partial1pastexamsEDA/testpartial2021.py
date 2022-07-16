import random

class DNode:
 def __init__(self, elem, next=None, prev=None ):
  self.elem = elem
  self.next = next
  self.prev = prev

class DList:
 def __init__(self):
  self.head=None
  self.tail=None
  self.size=0

 def checkElements (self, e):

  other = DList()
  current = self.head
  othernode = None
  while current:
   if current.elem >= e:
    if other.head == None:
     othernode = DNode(current.elem)
     other.head = othernode

    else:
     othernode.next = DNode(current.elem)
     othernode = othernode.next

    if current.next == None and current.prev == None:
     self.head = None
     self.tail = None
    elif current.next == None:# == self.tail:
     current.prev.next = None
     self.tail = current.prev
    elif current.prev == None: # == self.head:
     current.next.prev = None
     self.head = current.next
    else:
     current.prev.next = current.next
     current.next.prev = current.prev

   current = current.next


  return other

  """
  other = DList() # Create the list other
  current=self.head
 
  while current!=None: # we traverse the nodes while current is not None
   if current.elem >= e: # check the element being processed >= e
    other.addLast(current.elem) # add last in other
   if (current.prev == None): # if true, remove the first node of self
    self.head = current.next
    self.head.prev = None
   elif (current.next == None): # if true, remove the last node
    self.tail = current.prev
    self.tail.next = None
   else: # remove a middle node
    current.next.prev = current.prev
    current.prev.next = current.next
 
   current=current.next
 
   return other
  """

 def __str__(self):
  """Returns a string with the elements of the list"""
  node = self.head
  result = '['
  while node:
   result += str(node.elem) + ", "
   node = node.next

  if len(result) > 1:
   result = result[:-2]

  result += ']'
  return result

 def addLast(self,e):
  e = int(e)
  newNode=DNode(e)
  if self.head == None:
   self.head=newNode
  else:
   newNode.prev=self.tail
   self.tail.next=newNode

  self.tail=newNode
  self.size=self.size+1


l = DList()

for i in range(2):
 l.addLast(random.randint(1,10))

print(l)
print(l.checkElements(5))
print(l)