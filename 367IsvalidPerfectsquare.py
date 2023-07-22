class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        place = int(num**0.5)
        return True if place * place == num else False
    
    """
   place = num ** 1/2 that is equal the square root of num  sqroot of 16 is 4.
    if place * place == num then it is a perfect square meaning 4 * 4 = 16.  
    """
