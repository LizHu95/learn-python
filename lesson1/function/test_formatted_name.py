import unittest
from formatted_name import formattedName

class NamesTestCase(unittest.TestCase):
    """test formattedName，test开头才会被自动执行"""
    def test_first_last_name(self):
        """能够正确处理像 Janis Joplin 这样的姓名吗？"""
        # print("test_first_last_name start")
        formated_name=formattedName("janis",'joplin')
        self.assertEqual(formated_name,"Janis Joplin")
    
    def test_first_last_name2(self):
        """能够正确处理像 Liz Hu 这样的姓名吗？"""
        # print("test_first_last_name2 start")
        formated_name=formattedName("liz",'hu')
        self.assertEqual(formated_name,"Liz Hu")
    
    def test_first_last_name3(self):
        """能够正确处理像 Jade Ma 这样的姓名吗？"""
        # print("test_first_last_name3 start")
        formated_name=formattedName("jade",'ma')
        self.assertEqual(formated_name,"Jade Ma")
    
    def first_last_name(self):
        print("first_last_name start")

unittest.main()