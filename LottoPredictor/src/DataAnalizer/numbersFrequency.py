import csv

from LottoPredictor.src.Config import reader
from LottoPredictor.src.DataAnalizer import numbersOccurrencesFrequencyAnalyser
from LottoPredictor.src.DataConverter import dataConverter

config_reader = reader.ConfigReader()
results_filename = config_reader.get_lottery_results_filename()

results_matrix = []
with open(results_filename, newline='') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)  # skip the first line (header)
    for row in csv_reader:
        results_matrix.append(row)

converter = dataConverter.DataConverter()
occurrences_analyser = numbersOccurrencesFrequencyAnalyser.NumbersOccurrencesFrequencyAnalyser(converter)

print('There have been', converter.get_draws_count(results_matrix), 'draws so far')

list_of_numbers_occurrences = occurrences_analyser.get_list_of_numbers_occurrences(results_matrix)
print("The overall list of all numbers's occurrences: ", list_of_numbers_occurrences)

most_frequent_number = occurrences_analyser.get_most_frequent_number(results_matrix)
print('The most frequent number is', most_frequent_number[0], 'and it occurred', most_frequent_number[1], 'times')

least_frequent_number = occurrences_analyser.get_least_frequent_number(results_matrix)
print('The least frequent number is', least_frequent_number[0], 'and it occurred', least_frequent_number[1], 'times')

six_most_frequent_numbers = occurrences_analyser.get_six_most_frequent_numbers(results_matrix)
print('The six most frequently appearing numbers are', six_most_frequent_numbers)

six_least_frequent_numbers = occurrences_analyser.get_six_least_frequent_numbers(results_matrix)
print('The six least frequently appearing numbers are', six_least_frequent_numbers)

most_frequent_at_position_1 = occurrences_analyser.get_most_frequent_number_at_position(1, results_matrix)
print(
    'The most frequent number at position 1 is',
    most_frequent_at_position_1[0],
    'and it occurred',
    most_frequent_at_position_1[1],
    'times'
)

most_frequent_at_position_2 = occurrences_analyser.get_most_frequent_number_at_position(2, results_matrix)
print(
    'The most frequent number at position 2 is',
    most_frequent_at_position_2[0],
    'and it occurred',
    most_frequent_at_position_2[1],
    'times'
)

most_frequent_at_position_3 = occurrences_analyser.get_most_frequent_number_at_position(3, results_matrix)
print(
    'The most frequent number at position 3 is',
    most_frequent_at_position_3[0],
    'and it occurred',
    most_frequent_at_position_3[1],
    'times'
)

most_frequent_at_position_4 = occurrences_analyser.get_most_frequent_number_at_position(4, results_matrix)
print(
    'The most frequent number at position 4 is',
    most_frequent_at_position_4[0],
    'and it occurred',
    most_frequent_at_position_4[1],
    'times'
)

most_frequent_at_position_5 = occurrences_analyser.get_most_frequent_number_at_position(5, results_matrix)
print(
    'The most frequent number at position 5 is',
    most_frequent_at_position_5[0],
    'and it occurred',
    most_frequent_at_position_5[1],
    'times'
)

most_frequent_at_position_6 = occurrences_analyser.get_most_frequent_number_at_position(6, results_matrix)
print(
    'The most frequent number at position 6 is',
    most_frequent_at_position_6[0],
    'and it occurred',
    most_frequent_at_position_6[1],
    'times'
)

print(converter.get_numbers_sets(results_matrix))
