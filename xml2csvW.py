import sys
from PyQt5 import QtWidgets
import csv
import xml.etree.ElementTree as ET
import xml2csvGUI


class ArticleApp(QtWidgets.QMainWindow, xml2csvGUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #
        self.inputFileName = ""
        self.pushButton_input.clicked.connect(self.openInput)
        self.outputFileName = ""
        self.pushButton_output.clicked.connect(self.openOutput)
        self.pushButton_start.clicked.connect(self.xml2csv)
        self.pushButton_exit.clicked.connect(self.close)
        
    def openInput(self):
      self.inputFileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file','',"XML Files (*.xml *.gif)")	        
      self.lineEdit.setText(self.inputFileName[0])

    def openOutput(self):
      self.outputFileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Open file','',"CSV Files (*.csv)")	        
      self.lineEdit_2.setText(self.outputFileName[0])
    
    def xml2csv(self):
        #
        # open a csv file for writing 
        #
        # print (self.outputFileName)
        if self.inputFileName == "" :
            #print('error')
            status = "Bitte Fritz!Box XML-Datei auswählen!" 
            self.label_status.setStyleSheet("QLabel { background-color : white; color : red; }");
            self.label_status.setText(status)
            return()
        if self.outputFileName == "" :
            #print('error')
            status = "Bitte Ausgabe Datei eingeben!" 
            self.label_status.setStyleSheet("QLabel { background-color : white; color : red; }");
            self.label_status.setText(status)
            return()
        csvData = open(self.outputFileName[0], 'w')
        # create the csv writer object
        csvwriter = csv.writer(csvData)
        #
        # Set and write header row for the microSIP csv format
        csv_head = ['Name', 'Number', 'First Name', 'Last Name', 'Phone Number', 'Mobile Number', 'E-mail Address', 
            'Address', 'City' , 'State','Postal Code','Comment', 'Id',	'Info','Presence', 'Directory' ]
        csvwriter.writerow(csv_head)

        # open XML file for input and get the phonebook for scanning contacts   
        #inputFile = './Telefonbuch.xml'
        #
        tree = ET.parse(self.inputFileName[0])
        root = tree.getroot()
        phonebook = root.find('phonebook') 
        #
        # scanning contacts in the phonebook
        personCount = 0
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
            personCount += 1
        status = "Einträge für "+str(personCount) + " Personen gefunden und konvertiert"  
        self.label_status.setStyleSheet("QLabel { background-color : white; color : green; }");
        self.label_status.setText(status)
        csvData.close()


        
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ArticleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
