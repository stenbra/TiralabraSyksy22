import unittest
from KNN import Knn
from testData import TestData

class TestKNNFunctions(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_get_majority_neighbour_number(self):
        self.assertEqual(Knn.GetTheMajorityNeighbourNumber(TestData.DistListForADigitFour(),TestData.HundredFirstTrainLabels()),4)
    
    def test_create_pixel_bool_coordinate_number(self):
        self.assertAlmostEqual(Knn.CreatePixelBoolCoordinateNumber(TestData.NumberData()),TestData.NumberPixelBoolData())

    def test_closest_coordinate_distance(self):
        coordinate = [23,12]
        self.assertEqual(Knn.GetClosestNeighbour(coordinate,TestData.BoolCordTableTrainDataEntryindex_nine_nine()),2)