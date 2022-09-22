import unittest
from degrees import shortest_path
from degrees import person_id_for_name

source = '705' #person_id_for_name("Robin Wright")
target = '1597' #person_id_for_name("Mandy Patinkin")

class DegreesTestCase(unittest.TestCase):

    def test1(self):
        shortestpath = shortest_path(source, target)
        self.assertEqual(shortestpath ,[('93779', '1597')])

#unittest.main()
