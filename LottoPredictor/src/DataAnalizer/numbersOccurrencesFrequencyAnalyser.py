from collections import OrderedDict
from src.DataConverter import dataConverter


class NumbersOccurrencesFrequencyAnalyser:
    def __init__(self, converter: dataConverter.DataConverter):
        self.converter = converter

    def get_most_frequent_number(self, data):
        numbers_list = self.converter.get_numbers_as_list(data)

        return self.__get_most_frequent_number(numbers_list)

    def get_least_frequent_number(self, data):
        numbers_list = self.converter.get_numbers_as_list(data)

        least_frequent_number = None
        least_frequent_number_count = 0

        current_number = None
        current_number_count = 1
        for number in numbers_list:
            if current_number is None:
                current_number = number

                continue

            if current_number == number:
                current_number_count += 1

                continue

            if least_frequent_number_count == 0 or current_number_count < least_frequent_number_count:
                least_frequent_number_count = current_number_count
                least_frequent_number = current_number

            current_number = number
            current_number_count = 0

        return [least_frequent_number, least_frequent_number_count]

    def get_list_of_numbers_occurrences(self, data):
        numbers_list = self.converter.get_numbers_as_list(data)

        list_of_numbers_occurrences = {}
        for number in numbers_list:
            if number not in list_of_numbers_occurrences:
                list_of_numbers_occurrences[number] = 0

            list_of_numbers_occurrences[number] += 1

        return list_of_numbers_occurrences

    def get_six_most_frequent_numbers(self, data):
        numbers_list = self.converter.get_numbers_as_list(data)

        list_of_numbers_occurrences = OrderedDict(
            sorted(self.get_list_of_numbers_occurrences(numbers_list).items(), key=lambda t: t[1])
        )

        list_keys = list(list_of_numbers_occurrences.keys())
        return [
            list_keys[-1],
            list_keys[-2],
            list_keys[-3],
            list_keys[-4],
            list_keys[-5],
            list_keys[-6],
        ]

    def get_six_least_frequent_numbers(self, data):
        numbers_list = self.converter.get_numbers_as_list(data)

        list_of_numbers_occurrences = OrderedDict(
            sorted(self.get_list_of_numbers_occurrences(numbers_list).items(), key=lambda t: t[1])
        )

        list_keys = list(list_of_numbers_occurrences.keys())

        return list_keys[0:6]

    def get_most_frequent_number_at_position(self, position, data):
        numbers_list = self.converter.get_numbers_at_position_as_list(position, data)

        return self.__get_most_frequent_number(numbers_list)

    @staticmethod
    def __get_most_frequent_number(numbers_list):
        most_frequent_number = None
        most_frequent_number_count = 0

        current_number = None
        current_number_count = 1
        for number in numbers_list:
            if current_number is None:
                current_number = number

                continue

            if current_number == number:
                current_number_count += 1

                continue

            if current_number_count > most_frequent_number_count:
                most_frequent_number_count = current_number_count
                most_frequent_number = current_number

            current_number = number
            current_number_count = 0

        return [most_frequent_number, most_frequent_number_count]
