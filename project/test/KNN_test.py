import unittest
import KNN
from testData import TestData

class TestKNNFunctions(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    def test_get_majority_neighbour_number(self):
        self.assertEqual(KNN.GetTheMajorityNeighbourNumber([[14,5],[15,6],[29,6],[34,5],[36,6],[40,6]]),6)
    def test_create_pixel_bool_coordinate_number(self):
        self.assertAlmostEqual(KNN.CreatePixelBoolCoordinateNumber(TestData.NumberData),TestData.NumberPixelBoolData)