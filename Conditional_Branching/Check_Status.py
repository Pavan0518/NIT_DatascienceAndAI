class Solution:
    def checkStatus(a, b, flag):
        if (a > 0 and b < 0 and flag == False) or (a < 0 and b > 0 and flag == False): 
            print(True)
        elif a < 0 and b < 0 and flag == True: 
            print(True)
        else: 
             print(False)
            
            
# Input: a = 1, b = -1, flag = False
# Output: True
# Explanation: Since a is positive, b is negative, and flag is False, condition 1 holds true, so the function returns True.
Solution.checkStatus(1,-1,False)

# Input: a = -182, b = -9121, flag = True
# Output: True
# Explanation: Since both a and b are negative and flag is True, condition 2 holds true, so the function returns True.
Solution.checkStatus(-182,-9121,True)

# Input: a = 5, b = 3, flag = True
# Output: False
# Explanation: Neither condition 1 nor condition 2 holds, so the function returns False.
Solution.checkStatus(5,3,True)
