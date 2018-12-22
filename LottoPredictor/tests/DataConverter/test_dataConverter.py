import unittest
import src.DataConverter.dataConverter as dataConverter


class TestDataConverter(unittest.TestCase):
    __input_data_asc = [
        ['1', '2018-12-09', '1', '2', '3', '4', '5', '6'],
        ['2', '2018-12-09', '7', '8', '9', '10', '11', '12'],
    ]

    __input_data_desc = [
        ['2', '2018-12-09', '12', '11', '10', '9', '8', '7'],
        ['1', '2018-12-09', '6', '5', '4', '3', '2', '1'],
    ]

    def test_get_numbers_as_list_converts_list_of_sets_into_unordered_list_of_numbers(self):
        should_sort = False
        expected_output = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

        sut = dataConverter.DataConverter()
        actual_output = sut.get_numbers_as_list(self.__input_data_asc, should_sort)

        self.assertSequenceEqual(expected_output, actual_output)

    def test_get_numbers_as_list_converts_list_of_sets_into_ordered_list_of_numbers(self):
        should_sort = True
        expected_output = ['1', '10', '11', '12', '2', '3', '4', '5', '6', '7', '8', '9']

        sut = dataConverter.DataConverter()
        actual_output = sut.get_numbers_as_list(self.__input_data_asc, should_sort)

        self.assertSequenceEqual(expected_output, actual_output)

    def test_get_numbers_as_list_converts_list_of_sets_into_unordered_list_of_numbers_with_desc_data(self):
        should_sort = False
        expected_output = ['12', '11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1']

        sut = dataConverter.DataConverter()
        actual_output = sut.get_numbers_as_list(self.__input_data_desc, should_sort)

        self.assertSequenceEqual(expected_output, actual_output)

    def test_get_numbers_as_list_converts_list_of_sets_into_ordered_list_of_numbers_with_desc_data(self):
        should_sort = True
        expected_output = ['1', '10', '11', '12', '2', '3', '4', '5', '6', '7', '8', '9']

        sut = dataConverter.DataConverter()
        actual_output = sut.get_numbers_as_list(self.__input_data_desc, should_sort)

        self.assertSequenceEqual(expected_output, actual_output)

    def test_get_numbers_at_position_as_list_converts_list_of_sets_into_list_of_numbers_at_given_position(self):
        self.__test_get_numbers_at_position(1, ['1', '7'], False, self.__input_data_asc)
        self.__test_get_numbers_at_position(2, ['2', '8'], False, self.__input_data_asc)
        self.__test_get_numbers_at_position(3, ['3', '9'], False, self.__input_data_asc)
        self.__test_get_numbers_at_position(4, ['4', '10'], False, self.__input_data_asc)
        self.__test_get_numbers_at_position(5, ['5', '11'], False, self.__input_data_asc)
        self.__test_get_numbers_at_position(6, ['6', '12'], False, self.__input_data_asc)

    def __test_get_numbers_at_position(self, position, expected_output, should_sort, input_data):
        sut = dataConverter.DataConverter()
        actual_output = sut.get_numbers_at_position_as_list(position, input_data, should_sort)

        self.assertSequenceEqual(expected_output, actual_output)
