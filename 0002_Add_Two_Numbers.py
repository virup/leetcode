# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# In this solution we will iterate over the digits of the two numbers and
# add them together. We will have a carry variable which will store the carry
# of each sum. We will also add the carry to the next digits.
# 
# There are a couple of scenarios to consider:
# 1. Both the numbers are of the same number of digits
# 2. The first number has more digits than the second number
# 3. The second number has more digits than the second number
# 
# After all the digits are added it is possible that there is a carry
# which needs to be stored in the final result. 
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = None # Store the 
        carry = 0
        head = None
        
        # Add digits from both the numbers till you 
        # exhaust of of the numbers
        while (l1 != None and l2 != None):
            sum = l1.val + l2.val + carry
            l1 = l1.next
            l2 = l2.next
            digit = sum%10
            carry = sum//10
            if res == None:
            	 # Create a results linked list if not created
                res = ListNode(digit)
                head = res 
            else:
                temp = ListNode(digit)
                res.next = temp
                res = temp
        
        # If l1 is the large number (with more digits) then
        # keep adding it to the result
        while(l1 != None):
            sum = l1.val + carry
            l1 = l1.next
            digit = sum%10
            carry = sum//10
            if res == None:
            	# Create a results linked list if not created
                res = ListNode(digit)
                head = res
            else:
                temp = ListNode(digit)
                res.next = temp
                res = temp
                
        # If l2 is the large number (with more digits) then
        # keep adding it to the result
        while(l2 != None):
            sum = l2.val + carry
            l2 = l2.next
            digit = sum%10
            carry = sum//10
            if res == None:
            	# Create a results linked list if not created
                res = ListNode(digit)
                head = res
            else:
                temp = ListNode(digit)
                res.next = temp
                res = temp
        
        # If there is a carry still left, add it to the result
        if carry > 0:
        	# No need to create a new linked list here
            temp = ListNode(carry)
            res.next = temp
            res = temp
            
        return head
        