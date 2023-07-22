class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum1 = int(a,2)+int(b,2)
        return bin(sum1)[2:]

"""
Concept:- print(int("101",2))

101 = 1 * 2^2 + 0 * 2^1 + 1 * 2^0
= 4 + 0 + 1
= 5

[2:] :- To remove "0b" we use it.

Time complexity :- O(1)
space complexity :-O(1)
"""
