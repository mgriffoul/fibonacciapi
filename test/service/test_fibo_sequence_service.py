import unittest

from app.service.FiboSequenceService import FiboSequenceService
from test.service.DaoMocks import DaoWithMatchingBddBoundaries, DaoWithMatchingBddResult, DaoWithNoBddResults


class TestFibonacciSequenceService(unittest.TestCase):

    def test_fetch_closest_shouldReturnNumberRequest_when_requestNumberIsFoundInBdd(self):
        # Arrange
        dao = DaoWithMatchingBddResult('not_none')
        # Act
        number = FiboSequenceService.fetch_closest(FiboSequenceService(dao), 5)
        # Assert
        self.assertEqual(number, 5)

    def test_fetch_closest_shouldReturnClosest_when_boundariesAreFoundInBdd(self):
        # Arrange
        dao = DaoWithMatchingBddBoundaries(3, 8)
        # Act
        number = FiboSequenceService.fetch_closest(FiboSequenceService(dao), 4)
        # Assert
        self.assertEqual(number, 3)

    def test_fetch_closest_shouldReturnNumberRequest_when_boundariesAreNotFoundInBdd(self):
        # Arrange
        dao = DaoWithNoBddResults([{"value": 5}, {"value": 8}])
        # Act
        number = FiboSequenceService.fetch_closest(FiboSequenceService(dao), 13)
        # Assert
        self.assertEqual(number, 13)

    def test_fetch_closest_shouldReturnClosest_when_boundariesAreCalculated(self):
        # Arrange
        dao = DaoWithNoBddResults([{"value": 5}, {"value": 8}])
        # Act
        number = FiboSequenceService.fetch_closest(FiboSequenceService(dao), 12)
        # Assert
        self.assertEqual(number, 13)


if __name__ == '__main__':
    unittest.main()
