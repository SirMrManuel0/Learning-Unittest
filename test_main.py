import unittest
import main

class TestMain(unittest.TestCase):
    def test_reverse(self):
        text: str = "Hallo"
        revers: str = "ollaH"
        self.assertEqual(main.reverse(text), revers)
    
    def test_first_letter_big(self):
        text: str = "mARK"
        first_big: str = "Mark"
        self.assertEqual(main.first_letter_big(text), first_big)
    
    def test_bubblesort(self):
        l: list = [5,4,8,6]
        sort: list = [4,5,6,8]
        self.assertEqual(main.bubblesort(l), sort)
        
        l: list = [2,2,1,5,8,9]
        sort: list = [1,2,2,5,8,9]
        self.assertEqual(main.bubblesort(l), sort)
        
        l: list = [-1,-1,-2,5,6]
        sort: list = [-2,-1,-1,5,6]
        self.assertEqual(main.bubblesort(l), sort)
    
    def test_linearSearch(self):
        l: list = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(main.linearSearch(l, 3), 2)
        
        l: list = [1,2,3,3,4,5,6,7,8,9,10]
        self.assertEqual(main.linearSearch(l, 3), 2)
        
    def test_binarySearch(self):
        l: list = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(main.binarySearch(l, 3), 2)
        
        l: list = [1,2,3,3,4,5,6,7,8,9,10]
        self.assertEqual(l[main.binarySearch(l, 3)], 3)
        
    def test_heapSort(self):
        l: list = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(main.heapSort(l), l)
        
        l: list = [10,9,8,7,6,5,4,3,2,1]
        self.assertEqual(main.heapSort(l), [1,2,3,4,5,6,7,8,9,10])
        
        l: list = [4,5,8,7,1,8,-1,-5,-3]
        self.assertEqual(main.heapSort(l), [-5,-3,-1,1,4,5,7,8,8])
        
        l: list = [1,2,3,4,5,6,6,6,7,7,8,9,10]
        self.assertEqual(main.heapSort(l), l)

    def test_check(self):
        l: list = [1,2,3,4,5]
        self.assertTrue(main.check(l))
        l: list = [5,4,3,2,1]
        self.assertFalse(main.check(l))
        
    def test_heapSortOptimized(self):
        l: list = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(main.heapSortOptimized(l), l)
        
        l: list = [10,9,8,7,6,5,4,3,2,1]
        self.assertEqual(main.heapSortOptimized(l), [1,2,3,4,5,6,7,8,9,10])
        
        l: list = [4,5,8,7,1,8,-1,-5,-3]
        self.assertEqual(main.heapSortOptimized(l), [-5,-3,-1,1,4,5,7,8,8])
        
        l: list = [1,2,3,4,5,6,6,6,7,7,8,9,10]
        self.assertEqual(main.heapSortOptimized(l), l)
    
if __name__ == "__main__":
    unittest.main()