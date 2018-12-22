import csv

import urllib.request as urllib
from bs4 import BeautifulSoup

from src.Config import reader

print('Loading config...')

config_reader = reader.ConfigReader()
csv_file_name = config_reader.get_lottery_results_filename()

print('Scrapping lottery results page...')
results_page_url = 'http://megalotto.pl/wyniki/lotto/losowania-od-1-Stycznia-1957-do-31-Grudnia-2018'
results_page = urllib.urlopen(results_page_url)
content = BeautifulSoup(results_page, 'html.parser')
print('scrapping successful')

csv_file = open(csv_file_name, 'w', newline='')
writer = csv.writer(csv_file)

print('Saving results to file')
writer.writerow(['no', 'date', 'position 1', 'position 2', 'position 3', 'position 4', 'position 5', 'position 6'])
results = content.find('div', attrs={'class': 'lista_ostatnich_losowan'})

for ul in results.children:
    row = ul.find('li', attrs={'class': 'date_in_list'}).parent

    number = row.find('li', attrs={'class': 'nr_in_list'})
    date = row.find('li', attrs={'class': 'date_in_list'})
    list_of_numbers = row.find_all('li', attrs={'class': 'numbers_in_list'})

    writer.writerow([
        number.text.strip(),
        date.text.strip(),
        *[x.text.strip() for x in list_of_numbers]
    ])

print('results successfully saved into ', csv_file_name)
