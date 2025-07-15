class Solution:
    def calculate(a: int, b: int, operator: int) -> None:
        match operator:
            case 1: print(a + b)
            case 2: print(a - b)
            case 3: print(a * b)
            case _: print('Invalid Input')
            
Solution.calculate(2,3,1)
Solution.calculate(12,9,2)
Solution.calculate(2,3,3)