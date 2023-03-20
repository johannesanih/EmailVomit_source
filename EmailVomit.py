import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import emailgen

def cssLoader(fileName):
    with open(fileName, 'r') as rs:
        content = rs.read()
        rs.close()
        return content

class window(QWidget):
    def __init__ (self, parent = None):
        super(window, self).__init__(parent)

        self.setWindowTitle('EmailVomit')
        self.setGeometry(275,100,800,500)
        self.windowIcon = QIcon('emailvomiticon.png')
        self.setWindowIcon(self.windowIcon)
        self.setObjectName("mainWindow")
        self.setStyleSheet(cssLoader('main.css'))


        self.hbox = QHBoxLayout(self)
        self.formBox = QFormLayout(self)

        self.viewpanel = QVBoxLayout(self)
        self.formpanel = QVBoxLayout(self)

        self.topMenuBar = QMenuBar(self)

        self.viewEmailTxt = QTextEdit()
        self.habtnLayout = QHBoxLayout()
        self.helpBtn = QPushButton('Help')
        self.helpBtn.setObjectName('helpBtn')
        self.aboutBtn = QPushButton('About')
        self.aboutBtn.setObjectName('aboutBtn')
        self.habtnLayout.addWidget(self.helpBtn)
        self.habtnLayout.addWidget(self.aboutBtn)
        self.viewEmailTxt.setOverwriteMode(True)
        self.viewpanel.addLayout(self.habtnLayout)
        self.viewpanel.addWidget(self.viewEmailTxt)

        self.helpBtn.clicked.connect(self.showHelp)
        self.aboutBtn.clicked.connect(self.showAbout)

        #self.copyEmailsButton = QPushButton('Copy Emails')
        #self.copyEmailsButton.clicked.connect(self.copyEmails)
        #self.viewpanel.addWidget(self.copyEmailsButton)

        #self.downloadTXTButton = QPushButton('Download As .txt')
        #self.downloadTXTButton.clicked.connect(self.downloadEmails)
        #self.viewpanel.addWidget(self.downloadTXTButton)

        #----Email Generator Form----------------

        self.f_country_l = QLabel('Country')
        self.f_country_e = QComboBox()
        self.f_country_e.addItems(['afghanistan', 'argentina', 'australia', 'bangladesh', 'belgium', 'brazil', 'canada', 'china', 'denmark', 'egypt', 'france', 'gambia', 'germany', 'ghana', 'guinea', 'india', 'israel', 'kenya', 'malaysia', 'namibia', 'netherland', 'nigeria', 'southafrica', 'spain', 'tanzania', 'uganda', 'uk', 'usa', 'zambia', 'zimbabwe'])
        self.f_country_e.setObjectName('country')
        self.formBox.addRow(self.f_country_l, self.f_country_e)

        self.f_domain_l = QLabel('Custom Domain\n(Type "all" to use\ndefault domain list)')
        self.f_domain_e = QLineEdit()
        self.f_domain_e.setObjectName('domain')
        self.formBox.addRow(self.f_domain_l, self.f_domain_e)

        self.f_quantity_l = QLabel('Quantity')
        self.f_quantity_e = QSlider(Qt.Horizontal)
        self.f_quantity_e.setMinimum(1)
        self.f_quantity_e.setMaximum(10000)
        self.f_quantity_e.setValue(5)
        self.f_quantity_e.setSingleStep(5)
        self.f_quantity_e.setTickInterval(1)
        self.f_quantity_e.setTickPosition(QSlider.NoTicks)
        self.f_quantity_e.setObjectName('quantity')
        self.f_quantity_e.valueChanged.connect(self.sliderQuantityChange)
        
        self.formBox.addRow(self.f_quantity_l, self.f_quantity_e)

        self.emailFormatButtonLayout = QHBoxLayout()

        self.f_emailFormat_l = QLabel('Include Special Characters')
        self.f_emailFormat_1 = QRadioButton()
        self.f_emailFormat_1.setText('Yes')
        self.f_emailFormat_2 = QRadioButton()
        self.f_emailFormat_2.setText('No')

        self.rbGroup = QButtonGroup()
        self.rbGroup.addButton(self.f_emailFormat_1)
        self.rbGroup.addButton(self.f_emailFormat_2)
        self.rbGroup.buttonClicked[QAbstractButton].connect(self.emailFormatBtnSet)

        self.emailFormatButtonLayout.addWidget(self.f_emailFormat_1)
        self.emailFormatButtonLayout.addWidget(self.f_emailFormat_2)

        self.formBox.addRow(self.f_emailFormat_l, self.emailFormatButtonLayout)

        self.generateButton = QPushButton('Generate')
        self.generateButton.setObjectName('generateBtn')
        self.generateButton.clicked.connect(self.generate)
        
        self.formpanel.addLayout(self.formBox)
        self.infoText = QLabel("Copy And Save The Generated Emails")
        self.infoText.setObjectName('infoText')
        self.formpanel.addWidget(self.infoText)
        self.formpanel.addWidget(self.generateButton)
        

        #----------------------------------------



        self.hbox.addLayout(self.formpanel)
        self.hbox.addLayout(self.viewpanel)


        self.setLayout(self.hbox)

        self.g = emailgen.EmailGen()

    def showHelp (self):
        detailedText = """

            Step 1
            CHOOSE A COUNTRY
            You can currently generate emails from 30 different countries inluding the popular ones

            Step 2
            ADD A CUSTOM DOMAIN
            You can add your own email domian "example.com" or you can generate only from one specific popular email domain e.g "gmail.com" or to generate from all popular email service provider (gmail.com, yahoo.com, aol.com, hotmail.com) type in "all"

            Step 3
            CHOOSE THE AMOUNT OF EMAILS TO GENERATE
            You can generate a maximum of 10,000 email IDs at a time

            Step 4
            CHOOSE THE FORMAT OF THE EMAIL IDs
            Choose if you want special characters in your email IDs or not

            STEP 5
            CLICK THE GENERETE BUTTON
            Click The "Generate" button to generate your email IDs

            STEP 6
            COPY THE GENERATED EMAIL IDs
            Copy your generated email IDs, and use it.

        """
        helpMessage = QMessageBox()
        helpMessage.setWindowTitle('Help')
        helpMessage.setIcon(QMessageBox.Information)
        helpMessage.setText('Quick Guide On EmailVomit')
        helpMessage.setInformativeText('EmailVomit is a simple to use orangic email IDs generator tool, to use it, fill the form on the main window, follow the steps'+detailedText)
        helpMessage.setStandardButtons(QMessageBox.Ok)

        helpMessage.exec_()

    def showAbout (self):
        aboutMessage = QMessageBox()
        aboutMessage.setWindowTitle('About')
        aboutMessage.setIcon(QMessageBox.Information)
        aboutMessage.setText('Version: 1.0')
        aboutMessage.setInformativeText('Software Manufacturer: Johannes Anih\nIf you have any issues or suggestions send a mail to ibukunanih@gmail.com\nHire Me: +2349028412277, +2348069355436\nGitHub: https://www.github.com/johannesanih\nPortfolio: https://johannes.w3spaces.com')
        aboutMessage.setStandardButtons(QMessageBox.Ok)

        aboutMessage.exec_()
    
    def emailFormatBtnSet (self, btn):
        if btn.text() == 'Yes':
            self.g.typeOfEmail = "y"
        elif btn.text() == "No":
            self.g.typeOfEmail = "n"

    def sliderQuantityChange (self):
        self.f_quantity_l.setText('')
        quantityText = 'Quantity' + self.f_quantity_l.text() + ' ' + str(self.f_quantity_e.value())
        self.f_quantity_l.setText(quantityText)

    def generate (self):
        self.viewEmailTxt.clear()
        self.g.country_input = self.f_country_e.currentText().lower()
        self.g.domain_input = self.f_domain_e.text().lower()
        self.g.number_of_emails = self.f_quantity_e.value()

        """
        if self.f_emailFormat_1.isChecked:
            self.g.typeOfEmail = "y"
        elif self.f_emailFormat_2.isChecked:
            self.g.typeOfEmail = "n"
        
        """

        validationStatus = self.g.validateInputs()

        emails = ""
        if validationStatus is True:
            emails = self.g.generateEmail(self.g.typeOfEmail)

        self.viewEmailTxt.setText(emails)

        emailTempFile = open('tempEmailList.txt', 'w+')
        emailTempFile.write(emails)
        emailTempFile.close()
        
    """
    def copyEmails (self):
        #QClipboard.setText(self.viewEmailTxt.text())
        self.viewEmailTxt.copy()
        print(QClipboard.text())
    """

    def downloadEmails(self):
        fileName = QFileDialog.getSaveFileName(self, 'Save Email List', 'tempEmailList.txt', 'Text File (*.txt)')
    
def main ():
    app = QApplication(sys.argv)
    w = window()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()