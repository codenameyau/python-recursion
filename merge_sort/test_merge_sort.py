import unittest
import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_sort_on_empty_list(self):
        data = []
        self.assertEqual(merge_sort.sort(data), sorted(data))
        self.assertEqual(merge_sort.sort_efficiently(data), sorted(data))

    def test_sort_on_single_element(self):
        data = [0]
        self.assertEqual(merge_sort.sort(data), sorted(data))
        self.assertEqual(merge_sort.sort(data), sorted(data))

    def test_sort_on_two_elements_in_order(self):
        data = [1, 2]
        self.assertEqual(merge_sort.sort(data), sorted(data))
        self.assertEqual(merge_sort.sort_efficiently(data), sorted(data))

    def test_sort_on_two_elements_out_of_order(self):
        data = [2, 1]
        self.assertEqual(merge_sort.sort(data), sorted(data))
        self.assertEqual(merge_sort.sort_efficiently(data), sorted(data))

    def test_sort_on_odd_number_of_elements(self):
        data = [2, 1, 3]
        self.assertEqual(merge_sort.sort(data), sorted(data))
        self.assertEqual(merge_sort.sort_efficiently(data), sorted(data))

    def test_sort_on_duplicate_elements(self):
        data = [2, 1, 2, 3, 1, 3]
        self.assertEqual(merge_sort.sort(data), sorted(data))
        self.assertEqual(merge_sort.sort_efficiently(data), sorted(data))

    def test_sort_on_negative_elements(self):
        data = [-2, -1, 0, -3]
        self.assertEqual(merge_sort.sort(data), sorted(data))
        self.assertEqual(merge_sort.sort_efficiently(data), sorted(data))

    def test_sort_on_sample_list(self):
        data = [2, -2, 1, 3, 0, 2, -3]
        self.assertEqual(merge_sort.sort(data), sorted(data))
        self.assertEqual(merge_sort.sort_efficiently(data), sorted(data))


if __name__ == '__main__':
    unittest.main()
