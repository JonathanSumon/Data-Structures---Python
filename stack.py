# Stack Data Structure
# Modifying a Traditional Python List
# Last In First Out

class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item) #Pushes the Element to the Stack

    def pop(self):
        self.items.pop() #Pops the top-most Element of the Stack

    def view_Stack(self):
        return self.items #Returns All the elements of a Stack
        
a = Stack() #Object Initialisation

a.push(1)
a.push(2)
a.push(3)
print(a.view_Stack())
a.pop()
print(a.view_Stack())
