import unittest
import time
from .evaluate_two_arrays import evaluate


class TestEvaluate(unittest.TestCase):
    def test_evaluate(self):
        test_cases = [
            ([1, 2, 3, 4], [2, 3, 5, 6], [5, 6]),
            ([1, 2, 3], [1, 2, 3], []),
            ([1, 2, 3], [4, 5, 6], [4, 5, 6]),
            ([], [1, 2, 3], [1, 2, 3]),
            ([1, 2, 3], [], []),
            ([], [], []),
            ([1, 2, 3], [4, 4, 5, 5], [4, 4, 5, 5]),
        ]

        for base_arr, target_arr, expected in test_cases:
            with self.subTest(base_arr=base_arr, target_arr=target_arr):
                # Act
                result = evaluate(base_arr, target_arr)

                # Assert
                self.assertEqual(result, expected)

    def test_evaluate_performance(self):
        # Arrange
        array_size = 10 ** 8
        base_arr = list(range(array_size))
        target_arr = base_arr + [base_arr[-1] + 1]
        
        # Act
        start_time = time.time()
        result = evaluate(base_arr, target_arr)
        execution_time = time.time() - start_time

        # Assert
        self.assertLess(execution_time, 2.0,
                        f"Processing {array_size} elements took {execution_time:.3f}s, expected < 2.0s")
        self.assertEqual(result, [base_arr[-1] + 1])


if __name__ == "__main__":
    unittest.main()
