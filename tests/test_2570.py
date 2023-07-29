import unittest

from Exercise1.firstExercise import Solution
# from Exercise1 import Solution

class  TestMergeArrays(unittest.TestCase):

    def setUp(self):
       self.testObj = Solution()

    def test_zero(self):
        v1 = []
        v2 = []
        self.assertEqual(self.testObj.mergeArrays(v1,v2),[])

    def test_diffzero(self):
        v1 = [[2,3]]
        v2 = []
        self.assertEqual(self.testObj.mergeArrays(v1,v2),[[2,3]])
    
    def test_sum(self):
        v1 = [[5,7]]
        v2 = [[5,13]]
        self.assertEqual(self.testObj.mergeArrays(v1,v2),[[5,20]])

    def test_differences(self):
        v1 = [[2,6]]
        v2 = [[3,8]]
        self.assertEqual(self.testObj.mergeArrays(v1,v2),[[2,6],[3,8]])

    def test_order(self):
        v1 = [[2,6],[3,4],[1,2],[5,4]]
        v2 = [[3,8]]
        self.assertEqual(self.testObj.mergeArrays(v1,v2),[[1,2],[2,6],[3,12],[5,4]])

    def test_case3leetcode(self):
        v1 = [[148,597],[165,623],[306,359],[349,566],[403,646],[420,381],[566,543],[730,209],[757,875],[788,208],[932,695]]
        v2 = [[74,669],[87,399],[89,165],[99,749],[122,401],[138,16],[144,714],[148,206],[177,948],[211,653],[285,775],[309,289],[349,396],[386,831],[403,318],[405,119],[420,153],[468,433],[504,101],[566,128],[603,688],[618,628],[622,586],[641,46],[653,922],[672,772],[691,823],[693,900],[756,878],[757,952],[770,795],[806,118],[813,88],[919,501],[935,253],[982,385]]
        self.assertEqual(self.testObj.mergeArrays(v1,v2),[[74,669],[87,399],[89,165],[99,749],[122,401],[138,16],[144,714],[148,803],[165,623],[177,948],[211,653],[285,775],[306,359],[309,289],[349,962],[386,831],[403,964],[405,119],[420,534],[468,433],[504,101],[566,671],[603,688],[618,628],[622,586],[641,46],[653,922],[672,772],[691,823],[693,900],[730,209],[756,878],[757,1827],[770,795],[788,208],[806,118],[813,88],[919,501],[932,695],[935,253],[982,385]])
    


    

