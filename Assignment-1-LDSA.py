# Q-1 Delete the elements in an linked list whose sum is equal to zero

class Node():
  def __init__(self,data):
     self.data = data
     self.next = None

class Linkedlist():
   def __init__(self):
     self.head = None
    
   def append(self,data):
     new_node = Node(data)
     h = self.head
     if self.head is None:
         self.head = new_node
         return
     else:
         while h.next!=None:
             h = h.next
         h.next = new_node

   def remove_zeros_from_linkedlist(self, head):
     stack = []
     curr = head
     list = []
     while (curr):
         if curr.data >= 0:
             stack.append(curr)
         else:
             temp = curr
             sum = temp.data
             flag = False
             while (len(stack) != 0):
                 temp2 = stack.pop()
                 sum += temp2.data
                 if sum == 0:
                     flag = True
                     list = []
                     break
                 elif sum > 0:
                     list.append(temp2)
             if not flag:
                 if len(list) > 0:
                     for i in range(len(list)):
                         stack.append(list.pop())
                 stack.append(temp)
         curr = curr.next
     return [i.data for i in stack]

if __name__ == "__main__":
 l = Linkedlist()

 l.append(4)
 l.append(6)
 l.append(-10)
 l.append(8)
 l.append(9)
 l.append(10)
 l.append(-19)
 l.append(10)
 l.append(-18)
 l.append(20)
 l.append(25)
 print(l.remove_zeros_from_linkedlist(l.head))
 
 # Q-2 Reverse a linked list in groups of given size

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def reverse(self, head, k):
		
		if head == None:
		  return None
		current = head
		next = None
		prev = None
		count = 0

		while(current is not None and count < k):
			next = current.next
			current.next = prev
			prev = current
			current = next
			count += 1

		if next is not None:
			head.next = self.reverse(next, k)

		# prev is new head of the input list
		return prev

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data,end=' ')
			temp = temp.next


# Driver program
llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Given linked list")
llist.printList()
llist.head = llist.reverse(llist.head, 3)

print ("\nReversed Linked list")
llist.printList()

# Q-3 Merge a linked list into another linked list at alternate positions.

class Node(object):
	def __init__(self, data:int):
		self.data = data
		self.next = None


class LinkedList(object):
	def __init__(self):
		self.head = None
		
	def push(self, new_data:int):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
		
	# Function to print linked list from the Head
	def printList(self):
		temp = self.head
		while temp != None:
			print(temp.data)
			temp = temp.next
			
	def merge(self, p, q):
		p_curr = p.head
		q_curr = q.head

		# swap their positions until one finishes off
		while p_curr != None and q_curr != None:

			p_next = p_curr.next
			q_next = q_curr.next

			q_curr.next = p_next 
			p_curr.next = q_curr 

			p_curr = p_next
			q_curr = q_next
			q.head = q_curr

llist1 = LinkedList()
llist2 = LinkedList()

# Creating LLs

# 1.
llist1.push(3)
llist1.push(2)
llist1.push(1)
llist1.push(0)

# 2.
for i in range(8, 3, -1):
	llist2.push(i)

print("First Linked List:")
llist1.printList()

print("Second Linked List:")
llist2.printList()

# Merging the LLs
llist1.merge(p=llist1, q=llist2)

print("Modified first linked list:")
llist1.printList()

print("Modified second linked list:")
llist2.printList()

# Q-4 In an array, Count Pairs with given sum

def getPairsCount(arr, n, sum):

	count = 0 # Initialize result
 
	for i in range(0, n):
		for j in range(i + 1, n):
			if arr[i] + arr[j] == sum:
				count += 1

	return count

# Driver function
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is",
	getPairsCount(arr, n, sum))

# Q-5 Find duplicates in an array

#Initialize array   
arr = [1, 2, 3, 4, 2, 7, 8, 8, 3];   
   
print("Duplicate elements in given array: ");  
#Searches for duplicate element  
for i in range(0, len(arr)):  
    for j in range(i+1, len(arr)):  
        if(arr[i] == arr[j]):  
            print(arr[j]); 
            
# Q-6 Find the Kth largest and Kth smallest number in an array

# program to find K'th smallest
def kthSmallest(arr, N, K):

	arr.sort()
	return arr[K-1]


# Driver code
if __name__ == '__main__':
	arr = [12, 3, 5, 7, 19]
	N = len(arr)
	K = 2

	# Function call
	print("K'th smallest element is",
		kthSmallest(arr, N, K))
 
#Python code for k largest elements in an array'''

def kLargest(arr, k):
	# Sort the given array arr in reverse
	# order.
	arr.sort(reverse=True)
	# Print the first kth largest elements
	for i in range(k):
		print(arr[i], end=" ")

# Driver code
arr = [1, 23, 12, 9, 30, 2, 50]
# n = len(arr)
k = 3
print(kLargest(arr, k))

# Q-7 Move all the negative elements to one side of the array

def move(arr):
    arr.sort()

# driver code
arr = [ -1, 2, -3, 4, 5, 6, -7, 8, 9 ]
move(arr)
for e in arr:
	print(e, end = " ")


# Q-8 Reverse a string using a stack data structure

import string
def the_helper(s):
	# create an empty stack
	stack = []
	# push all characters of the string into the stack
	for i in s:
		stack.append(i)
	# empty the string
	s = ""
	while stack:
		s += stack.pop()
	return s

# main function
if __name__ == "__main__":
	# define the input string
	str = "PrasannPatil"
	
	reversed_str = the_helper(str)
	
	print("Reversed string is: ", reversed_str)


# Q-9 Evaluate a postfix expression using stack

class evalpostfix:
	def __init__(self):
		self.stack = []
		self.top = -1

	def pop(self):
		if self.top == -1:
			return
		else:
			self.top -= 1
			return self.stack.pop()

	def push(self, i):
		self.top += 1
		self.stack.append(i)

	def centralfunc(self, ab):
		for i in ab:

			# If the component of the list is an integer
			try:
				self.push(int(i))
	
			except ValueError:
				val1 = self.pop()
				val2 = self.pop()
				if i == '/':
					self.push(val2 / val1)
				else:
					
					# Switch statement to perform operation
					switcher = {'+': val2 + val1, '-': val2 -
								val1, '*': val2 * val1, '^': val2**val1}
					self.push(switcher.get(i))
		return int(self.pop())

# Driver code
if __name__ == '__main__':
	str = '100 200 + 2 / 5 * 7 +'
	
	strconv = str.split(' ')
	obj = evalpostfix()
	print(obj.centralfunc(strconv))

# Q-10 Implement a queue using the stack data structure

class Queue:
	def __init__(self):
		self.s1 = []
		self.s2 = []

	def enQueue(self, x):
		
		# Move all elements from s1 to s2
		while len(self.s1) != 0:
			self.s2.append(self.s1[-1])
			self.s1.pop()

		# Push item into self.s1
		self.s1.append(x)

		# Push everything back to s1
		while len(self.s2) != 0:
			self.s1.append(self.s2[-1])
			self.s2.pop()

	def deQueue(self):
		
			# if first stack is empty
		if len(self.s1) == 0:
			print("Q is Empty")
	
		# Return top of self.s1
		x = self.s1[-1]
		self.s1.pop()
		return x

# Driver code
if __name__ == '__main__':
	q = Queue()
	q.enQueue(1)
	q.enQueue(2)
	q.enQueue(3)

	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue())

