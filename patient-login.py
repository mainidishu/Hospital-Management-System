import os
import sys
import subprocess
import datetime
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
pid_file=open("loggedin.txt")
token_file=open("token.txt")
pid=pid_file.readline();
pid_file.close();
pid=pid[:-1]
now = datetime.datetime.now()
app_date=str(now.year)+"-"+str(now.month)+"-"+str(now.day+1)+" "+"12:"+str(now.minute)+":"+str(now.second)

class Form(QDialog):

	def __init__(self, parent = None):
		super(Form, self).__init__(parent)
	
		self.ql = QLabel("Enter Specification for Doctor:")
		self.le = QLineEdit()
		self.le.setObjectName("Specification")

		self.ql1 = QLabel("Enter city:")
		self.le1 = QLineEdit()
		self.le1.setObjectName("City")

		self.pb = QPushButton()
		self.pb.setObjectName("Create")
		self.pb.setText("CREATE")

		self.pb1 = QPushButton()
		self.pb1.setObjectName("Show")
		self.pb1.setText("SHOW")
		
		layout = QFormLayout()
	
		layout.addWidget(self.ql)
		layout.addWidget(self.le)

		layout.addWidget(self.ql1)
		layout.addWidget(self.le1)
			
		layout.addWidget(self.pb)
		layout.addWidget(self.pb1)

		self.setLayout(layout)
		self.connect(self.pb, SIGNAL("clicked()"),self.create_click)
		self.connect(self.pb1, SIGNAL("clicked()"),self.show_click)


		self.setWindowTitle("HOSPITAL MANAGEMENT SYSTEM")


	def create_click(self):
		spec = self.le.text()
		city = self.le1.text()
		cur.execute(str("SELECT doc_ID FROM DoctorDetails WHERE spec=\""+spec+"\";"))
		did=cur.fetchall()
		cur.execute(str("SELECT Hospital_ID FROM Hospital WHERE Hospital_address LIKE \"%"+city+"%\";"))
		hid=cur.fetchall()			
		token_file=open("token.txt")
		token=int(token_file.read());
		command="INSERT INTO Appointment VALUES (" + "\""+pid+"\"," + "\""+str(did[0][0])+"\"," + "\""+str(hid[0][0])+"\"," + "\""+str(app_date)+"\"," + "\"" +str(token) + "\");"
		token_file.close()
		token+=1
		token_file=open('token.txt','w+')
		token_file.seek(0)
		token_file.write(str(token))
		token_file.close()			
		cur.execute(command)
		conn.commit()			
	def show_click(self):
        	os.system("python3 patient-app-show.py")
	



app = QApplication(sys.argv)
form = Form()
form.resize(1000,500)
form.show()
sys.exit(app.exec_())


