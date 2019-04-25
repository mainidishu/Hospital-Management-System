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
file=open("loggedin.txt",'w+')
file.seek(0)
flag=-1;

class Form(QDialog):
	def __init__(self, parent = None):
		super(Form, self).__init__(parent)

		self.ql = QLabel("--::Enter D for Doctor / Enter P for Patient::--")
		self.le = QLineEdit()
		self.le.setObjectName("User")

		self.ql1 = QLabel("User_ID:")
		self.le1 = QLineEdit()
		self.le1.setObjectName("User_ID")

		self.ql2 = QLabel("Password:")
		self.le2 = QLineEdit()
		self.le2.setObjectName("Password")

		self.pb = QPushButton()
		self.pb.setObjectName("Login")
		self.pb.setText("LOGIN")

		self.pb1 = QPushButton()
		self.pb1.setObjectName("Signup")
		self.pb1.setText("SIGNUP")

		layout = QFormLayout()

		layout.addWidget(self.ql)
		layout.addWidget(self.le)

		layout.addWidget(self.ql1)
		layout.addWidget(self.le1)

		layout.addWidget(self.ql2)
		layout.addWidget(self.le2)

		layout.addWidget(self.pb)
		layout.addWidget(self.pb1)

		self.setLayout(layout)
		self.connect(self.pb, SIGNAL("clicked()"),self.login_click)
		self.connect(self.pb1, SIGNAL("clicked()"),self.signup_click)


		self.setWindowTitle("HOSPITAL MANAGEMENT SYSTEM")

	def login_click(self):
		user = self.le.text()
		user_name = self.le1.text()
		password = self.le2.text()
		if user=="P":
			flag=0
		elif user=="D":
			flag=1
		if flag==0:
			cur.execute(str("SELECT Patient_pwd FROM Patient WHERE Patient_ID=\""+user_name+"\""));
			res=cur.fetchall()
			if(res!=()):
				if(res[0][0]==password):
					print(user_name)
					file.seek(0)
					file.write(user_name)
					file.close()
					os.system("python3 patient-login.py")
		elif flag==1:
			cur.execute(str("SELECT doc_pwd FROM DoctorDetails WHERE doc_ID=\""+user_name+"\""));
			res=cur.fetchall()
			if(res!=()):
				if(res[0][0]==password):
					print(user_name)
					file.seek(0)
					file.write(user_name)
					file.close()
					os.system("python3 doctor-login.py")




	def signup_click(self):
		user = self.le.text()
		flag=0
		if user=="P":
			flag=3
		elif user=="D":
			flag=2

		if flag==2:
			os.system("python3 signup-doctor.py")
		elif flag==3:
			os.system("python3 signup-patient.py")


app = QApplication(sys.argv)
form = Form()
form.resize(1000,500)
form.show()
sys.exit(app.exec_())
