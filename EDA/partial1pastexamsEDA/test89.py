from midtermexam89 import MyDList
import unittest #package that contains the classes t

class Test(unittest.TestCase):
    
    def setUp(self):
        """This functions is executed for each of the test functions"""
        self.expected = [4,6,8,10,12,14,16,18,20]
    
    def test1_checkSequentialEven(self):
        """ Case empty list"""
        self.empty=MyDList()
        self.expected=[]
        self.empty.checkSequentialEven()
        self.assertEqual(str(self.empty), str(self.expected), "Fail: Case 1: list empty'")
           
    def test2_checkSequentialEven(self):
        """ Case list with one even element"""
        self.l=MyDList()
        self.l.append(4)
        self.expected = [4]
        self.l.checkSequentialEven()
        self.assertEqual(str(self.l), str(self.expected), "Fail: Case 2: list with one even element'")

    def test3_checkSequentialEven(self):
        """ Case list with one odd element"""
        self.l=MyDList()
        self.l.append(5)
        self.expected = []
        self.l.checkSequentialEven()
        self.assertEqual(str(self.l), str(self.expected), "Fail: Case 3: list with one odd element'")       
        
    def test4_checkSequentialEven(self):
        """ Case correct list"""
        self.l=MyDList()
        self.data=[4,6,8,10,12,14,16,18,20]
        for x in self.data:
            self.l.append(x)
        self.l.checkSequentialEven()
        self.assertEqual(str(self.l), str(self.expected), "Fail: Case4: correct list")
     
    def test5_checkSequentialEven(self):
        """ Case list with missing even numbers"""
        self.l=MyDList()
        self.data=[4,6,14,16,20]
        for x in self.data:
            self.l.append(x)
        self.l.checkSequentialEven()
        self.assertEqual(str(self.l), str(self.expected), "Fail: Case 5:  list with missing even numbers")
      
        
    def test6_checkSequentialEven(self):
        """ Case correct sequiential list but with start/end odd numbers"""
        self.l=MyDList()
        self.data=[3,4,6,8,10,12,14,16,18,20,27]
        for x in self.data:
            self.l.append(x)
        self.l.checkSequentialEven()
        self.assertEqual(str(self.l), str(self.expected), "Fail: Case 6: correct sequiential list but with start/end odd numbers")
   
        
    def test7_checkSequentialEven(self):
        """ Case correct sequiential list but with interleaved odd numbers"""
        self.l=MyDList()
        self.data=[3,4,6,8,10,11,12,14,16,17,18,20]
        for x in self.data:
            self.l.append(x)
        self.l.checkSequentialEven()
        self.assertEqual(str(self.l), str(self.expected), "Fail: Case 7: correct sequiential list but with interleaved odd numbers")
    
    def test8_checkSequentialEven(self):
        """ Case incomplete sequential list with start/end odd numbers"""
        self.l=MyDList()
        self.data=[3,4,6,8,14,20,27]
        for x in self.data:
            self.l.append(x)
        self.l.checkSequentialEven()
        self.assertEqual(str(self.l), str(self.expected), "Fail: Case 8: incomplete sequential list with start/end odd numbers")
        
        
    def test9_checkSequentialEven(self):
        """ Case incomplete sequential list with interleaved odd numbers"""
        self.l=MyDList()
        self.data=[4,10,11,12,14,17,20]
        for x in self.data:
            self.l.append(x)
        self.l.checkSequentialEven()
        self.assertEqual(str(self.l), str(self.expected), "Fail: Case 9: incomplete sequential list with interleaved odd numbers")
      
        
   
  

#If you are using Spyder, please comment the following line: 
#unittest.main(argv=['first-arg-is-ignored'], exit=False)

#To use Spyder, remove the following comments:
if __name__ == '__main__':
    unittest.main()

