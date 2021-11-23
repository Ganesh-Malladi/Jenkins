#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from SE_jenkins import add_6_to_list

class Testadd6(unittest.TestCase):
    def test1_list_int(self):
        """
        Test case to add 6 to elements of list
        """
        data = [1,2,3,4,5]
        result = add_6_to_list(data)
        self.assertEqual(result, [7,8,9,10,11])
    
    def test2_list_int(self):
        """
        Test case to add 6 to elements of list
        """
        data = [1,9,21,-3,11]
        result = add_6_to_list(data)
        self.assertEqual(result, [1,2,3,4,5])
        
    def test3_list_int(self):
        """
        Test case to add 6 to elements of list
        """
        data = [93,69,44,11,74]
        result = add_6_to_list(data)
        self.assertEqual(result, [99,75,50,17,80])


if __name__ == '__main__':
    unittest.main()
