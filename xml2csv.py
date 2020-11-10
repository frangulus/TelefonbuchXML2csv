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
#   TODO        
#   
#   Changelog
#
import xml.etree.ElementTree as ET
import csv
#
# open a csv file for writing 
csvData = open('importfile.csv', 'w')
# create the csv writer object
csvwriter = csv.writer(csvData)
#
# Set and write header row for the microSIP csv format
csv_head = ['Name', 'Number', 'First Name', 'Last Name', 'Phone Number', 'Mobile Number', 'E-mail Address', 
    'Address', 'City' , 'State','Postal Code','Comment', 'Id',	'Info','Presence', 'Directory' ]
csvwriter.writerow(csv_head)

# open XML file for input and get the phonebook for scanning contacts   
inputFile = './Telefonbuch3.xml'
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
            number = n.text
            csv = []
            type = (n.attrib['type'])
            pos_name = name + ' (' + type + ')'
            csv.append(pos_name)
            csv.append(number)
            csvwriter.writerow(csv)
    #

csvData.close()