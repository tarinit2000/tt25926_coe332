import unittest
from read_animals import breed

class TestJsonParser(unittest.TestCase):

    def test_breed(self):
        dict1 = {
            "head": "lion",
            "body": "ape-ape",
            "arms": 2,
            "legs": 6,
            "tail": 8
        }
        dict2 = {
            "head": "lion",
            "body": "ape-ape",
            "arms": 2,
            "legs": 6,
            "tail": 8
        }       
        dict3 = {
            "head": "lion",
            "body": "ape-ape"
        }
        dict4 = {
            "head": "lion",
            "arms": 2,
            "body": "ape-ape",
            "legs": 6,
            "tail": 8
        }
        self.assertDictEqual(breed(dict1, dict2), dict1)
        self.assertRaises(KeyError, breed, dict1, dict3)
        self.assertDictEqual(breed(dict1, dict4), dict1)
        self.assertRaises(TypeError, breed, '', '')
        self.assertRaises(TypeError, breed, dict1, 'dict5')
        self.assertRaises(TypeError, breed, 'head', 5)
        self.assertRaises(TypeError, breed, ['head','body'], [2,'ape-lion'])
        
if __name__ == "__main__":
    unittest.main()
