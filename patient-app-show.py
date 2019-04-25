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
import pymysql as sql
conn=sql.connect(host="localhost" , user="root" , password="" , database="hms")
cur = conn.cursor()
pid_file=open("loggedin.txt")
token_file=open("token.txt")
pid=pid_file.readline();
pid_file.close();
now = datetime.datetime.now()
if pid[-1]=='\n':
	pid=pid[:-1]	
print(pid)
class Form(QDialog):

	def __init__(self, parent = None):
		super(Form, self).__init__(parent)
		layout = QFormLayout()
		
		command="SELECT * FROM Appointment WHERE Patient_ID=\""+pid+"\";"
		print(command)
		cur.execute(command)
		res=cur.fetchall()
		rep='Patient ID          Doctor ID          Hospital ID      Appointment DateTime        Token Number\n'
		for row in res:
			rep=rep+str(row[0]).upper()+"      "
			rep=rep+str(row[1]).upper()+"      "
			rep=rep+str(row[2]).upper()+"             "
			rep=rep+str(row[3]).upper()+"               "
			rep=rep+str(row[4])	
			rep+="\n"
		self.ql = QLabel(rep)
		layout.addWidget(self.ql)
		self.setLayout(layout)
app = QApplication(sys.argv)
form = Form()
form.resize(1000,500)
form.show()
sys.exit(app.exec_())
