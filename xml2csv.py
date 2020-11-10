import xml.etree.ElementTree as ET
import csv

tree = ET.parse("/home/newnas/thomas/Projekte/TelefonbuchXML2csv/Telefonbuch3.xml")
root = tree.getroot()

# open a file for writing

csv_data = open('importfile.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(csv_data)
csv_head = ['Name', 'Number', 'First Name', 'Last Name', 'Phone Number', 'Mobile Number', 'E-mail Address', 
    'Address', 'City' , 'State','Postal Code','Comment', 'Id',	'Info','Presence', 'Directory' ]
csvwriter.writerow(csv_head)

phonebook = root.find('phonebook') 

for contact in phonebook.findall('contact'):
    #print(root.tag)
    #print(root.attrib)
    
    #address_list = []
    #print(contact)
    #print(contact.tag)
    #print(contact.attrib)
    person = contact.find('person')
    name = (person.find('realName').text)
    #
    tel = contact.findall('telephony')
    for t in tel:
        for n in t.findall('number'):
            number = n.text
            csv = []
            print(n.text)
            type = (n.attrib['type'])
            pos_name = name + ' (' + type + ')'
            csv.append(pos_name)
            csv.append(number)
            csvwriter.writerow(csv)
    #

csv_data.close()