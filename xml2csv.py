#!/usr/bin/env python3
# coding: utf8
# License MIT 
#    Document   : xml2csv.py 
#    Author     : Thomas Glaser
#    Description: Converts a XML-file from Fritz!Box phonebook export to an importable csv file for microSIP 
#    Version    : 0.10 
#    Build      : None  
#    Copyright  : Thomas Glaser 2020
#
#    Fritz!OS Version: 7.20 
#    microSip Version:      
#
#   TODO        
#   
#   Changelog
#
import xml.etree.ElementTree as ET
import csv
import sys
#
# open a csv file for writing 
csvData = open('microSipImport.csv', 'w')
# create the csv writer object
csvwriter = csv.writer(csvData)
#
# Set and write header row for the microSIP csv format
csv_head = ['Name', 'Number', 'First Name', 'Last Name', 'Phone Number', 'Mobile Number', 'E-mail Address', 
    'Address', 'City' , 'State','Postal Code','Comment', 'Id',	'Info','Presence', 'Directory' ]
csvwriter.writerow(csv_head)

# open XML file for input and get the phonebook for scanning contacts   
inputFile = './Telefonbuch.xml'
if len(sys.argv) > 0:
    if sys.argv[1] == "help":
        print(" Help ")
        sys.exit(0)
    else:    
        inputFile = sys.argv[1]
#
tree = ET.parse(inputFile)
root = tree.getroot()
phonebook = root.find('phonebook') 
#
# scanning contacts in the phonebook
for contact in phonebook.findall('contact'):
    # find person / company and get the name (FB=realName) 
    person = contact.find('person')
    name = (person.find('realName').text)
    # find all telephony entries for that person (landline, mobile, work, privat...)
    tel = contact.findall('telephony')
    # iter about the entries an save it to the csv file 
    for t in tel:
        for n in t.findall('number'):
            # clear row / new list
            csvRow = []
            number = n.text
            # get type of phone number 
            type = (n.attrib['type'])
            # add type to the name 
            nameType = name + ' (' + type + ')'
            # appent content to list and write a row 
            csvRow.append(nameType)
            csvRow.append(number)
            csvwriter.writerow(csvRow)
    #

csvData.close()