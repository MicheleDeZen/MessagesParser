"""
Date: 15/01/2023
Author: Michele De Zen
Description: Script to extract 2 types of "error messages" from single files
"""

#Imports
from bs4 import BeautifulSoup
import os
import csv

#Paths
inputPath = 'files/'
outputPath = './out/Messages.csv'

inputPathCases = 'files/Cases'
outputPathCases = './out/Cases.csv'

#Headers for the csv output
header = ['file', 'name', 'description']

#Temporary storage for extracted data
dataMessages = []
dataCases = []

#First type of files
for filename in os.listdir(inputPath):
    f = os.path.join(inputPath, filename)
    #check if it's a file
    if os.path.isfile(f):
        #log the file name to console
        print(f)
        with open(f, 'r', encoding='UTF8') as file:

            contents = file.read()
            soup = BeautifulSoup(contents, 'lxml')

            name = soup.find("td", {"class": "messageshortcut"}).text
            desc = soup.find("td", {"class": "messagetext"}).text

            dataMessages.append([f, name, desc])

#Save extracted data to csv file
with open(outputPath, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    for row in dataMessages:
        writer.writerow(row)

#Second type of file
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

#Save extracted data to csv file
with open(outputPathCases, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    for row in dataCases:
        writer.writerow(row)