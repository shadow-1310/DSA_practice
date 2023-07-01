# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) :
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """
from collections import deque

# this is a correct solution using DFS recursively
# done on 29-06-2023
class NestedIterator:
    def __init__(self, nestedList):
        self.res = []
        def iterate(element):
            for e in element:
                if e.isInteger():
                    self.res.append(e.getInteger())
                else:
                    iterate(e.getList())
        iterate(nestedList)
        self.res = deque(self.res)
    
    def next(self) -> int:
        return self.res.popleft()
    
    def hasNext(self) -> bool:
        return self.res
         