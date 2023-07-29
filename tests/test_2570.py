import unittest

from Exercise1.firstExercise import Solution
# from Exercise1 import Solution

class  TestMergeArrays(unittest.TestCase):

    def setUp(self):
       self.testObj = Solution()

    def test_zero(self):
        v1 = [[]]
        v2 = [[]]
        self.assertEqual(self.testObj.mergeArrays(v1,v2),[[]])

    def test_diffzero(self):
        v1 = [[2,3]]
        v2 = [[]]
        self.assertEqual(self.testObj.mergeArrays(v1,v2),[[2,3]])
    
    
    def test_sum(self):
        v1 = [[5,7]]
        v2 = [[5,13]]
        self.assertEqual(self.testObj.mergeArrays(v1,v2),[[5,20]])

    def test_differences(self):
        v1 = [[2,6]]
        v2 = [[3,8]]
        self.assertEqual(self.testObj.mergeArrays(v1,v2),[[2,6],[3,8]])
    
    

