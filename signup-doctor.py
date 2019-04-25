import os
import sys
import subprocess
from time import sleep
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import (QMainWindow, QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout, QWidget, QSound)
from PyQt4.QtGui import QSound
import subprocess
import pymysql as sql
conn=sql.connect(host="localhost" , user="root" , password="" , database="hms")
cur = conn.cursor()

class Form(QDialog):

	def __init__(self, parent = None):
		super(Form, self).__init__(parent)

		self.ql1 = QLabel("Doctor Name:")
		self.le1 = QLineEdit()
		self.le1.setObjectName("Doctor_Name")

		self.ql2 = QLabel("Password:")
		self.le2 = QLineEdit()
		self.le2.setObjectName("Password")

		self.ql3 = QLabel("Phone Number:")
		self.le3 = QLineEdit()
		self.le3.setObjectName("Phone_Number")

		self.ql4 = QLabel("Address:")
		self.le4 = QLineEdit()
		self.le4.setObjectName("Address")

		self.ql5 = QLabel("Gender:")
		self.le5 = QLineEdit()
		self.le5.setObjectName("Gender")

		self.ql6 = QLabel("Specification:")
		self.le6 = QLineEdit()
		self.le6.setObjectName("Specification")

		self.pb = QPushButton()
		self.pb.setObjectName("Signup")
		self.pb.setText("SIGNUP")

		layout = QFormLayout()

		layout.addWidget(self.ql1)
		layout.addWidget(self.le1)

		layout.addWidget(self.ql2)
		layout.addWidget(self.le2)

		layout.addWidget(self.ql3)
		layout.addWidget(self.le3)

		layout.addWidget(self.ql4)
		layout.addWidget(self.le4)

		layout.addWidget(self.ql5)
		layout.addWidget(self.le5)

		layout.addWidget(self.ql6)
		layout.addWidget(self.le6)

		layout.addWidget(self.pb)

		self.setLayout(layout)
		self.connect(self.pb, SIGNAL("clicked()"),self.signup_click)


		self.setWindowTitle("HOSPITAL MANAGEMENT SYSTEM")


	def signup_click(self):

		name = self.le1.text()
		pwd = self.le2.text()
		ph = self.le3.text()
		addr = self.le4.text()
		sex = self.le5.text()
		spec = self.le6.text()
		hours="3"
		intime="08:00:00"
		id=name[0:3]+"_"+str(ph[0:5])
		command="INSERT INTO DoctorDetails VALUES (" + "\""+str(id)+"\"," + "\""+str(name)+"\"," + "\""+str(ph)+"\"," + "\""+str(pwd)+"\"," + "\"" +str(addr) + "\"," + "\""+str(sex)+ "\"," +"\"" +str(spec) + "\"," + "\"" +intime+ "\" ,"+str(hours)+");"
		print(command)
		cur.execute(command)
		conn.commit()	
		os.system("python3 Main.py")



app = QApplication(sys.argv)
form = Form()
form.resize(1000,500)
form.show()
sys.exit(app.exec_())

