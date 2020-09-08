import json
import requests
from bs4 import BeautifulSoup
import numpy as np
import csv

pages = np.arange(1, 300)

min = 600001
max = 650000
sequences = 1
type_de_bien = "appartement"

while max < 1000000:

    for page in pages:

        print(str(sequences) + ' : ' + str(page))

        url = 'https://www.immoweb.be/fr/recherche/' + type_de_bien + '/a-vendre?countries=BE&minPrice=' \
              + str(min) + '&maxPrice=' + str(max) + '&page=' + str(page) + '&orderBy=relevance'

        soup = BeautifulSoup(requests.get(url).content, 'html.parser')

        data = json.loads(soup.find('iw-search')[':results'])

        for d in data:
            url = 'https://www.immoweb.be/en/classified/{}'.format(d['id'])

            with open('links2.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([url])

    min += 50000
    max += 50000
    sequences += 1

