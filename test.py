from bs4 import BeautifulSoup
import os
import csv

inputPath = 'files/'
outputPath = './out/Messages.csv'

inputPathCases = 'files/Cases'
outputPathCases = './out/Cases.csv'

header = ['file', 'name', 'description']

dataMessages = []
dataCases = []


#Normal
for filename in os.listdir(inputPath):
    f = os.path.join(inputPath, filename)
    if os.path.isfile(f):
        print(f)
        with open(f, 'r', encoding='UTF8') as file:

            contents = file.read()


            soup = BeautifulSoup(contents, 'lxml')

            name = soup.find("td", {"class": "messageshortcut"}).text
            desc = soup.find("td", {"class": "messagetext"}).text

            dataMessages.append([f, name, desc])

with open(outputPath, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    for row in dataMessages:
        writer.writerow(row)

#Cases
for filename in os.listdir(inputPathCases):
    f = os.path.join(inputPathCases, filename)
    if os.path.isfile(f):
        print(f)
        with open(f, 'r', encoding='UTF8') as file:

            contents = file.read()


            soup = BeautifulSoup(contents, 'lxml')

            name = soup.find("a", {"class": "messageshortcut"}).text
            desc = soup.find("a", {"class": "messagetext"}).text

            dataCases.append([f, name, desc])

with open(outputPathCases, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    for row in dataCases:
        writer.writerow(row)