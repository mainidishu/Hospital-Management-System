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
import datetime
import pymysql as sql
conn=sql.connect(host="localhost" , user="root" , password="" , database="hms")
cur = conn.cursor()

class Form(QDialog):

	def __init__(self, parent = None):
		super(Form, self).__init__(parent)

		did_file=open("loggedin.txt")
		did=did_file.readline()
		print(did)
		if did[-1]=='\n':
			did=did[:-1]
		now = datetime.datetime.now()
		command="SELECT * FROM Appointment WHERE Doctor_ID=\""+did+"\";"
		print(command)
		cur.execute(command)
		res=cur.fetchall()
		rep='Patient ID          Doctor ID          Hospital ID      Appointment DateTime        Token Number\n'
		for row in res:
			print(row)
			rep=rep+str(row[0]).upper()+"      "
			rep=rep+str(row[1]).upper()+"      "
			rep=rep+str(row[2]).upper()+"             "
			rep=rep+str(row[3]).upper()+"               "
			rep=rep+str(row[4]).upper()	
			rep+="\n"
		self.ql = QLabel(rep)
		layout = QFormLayout()

		layout.addWidget(self.ql)
		self.setLayout(layout)
		self.setWindowTitle("HOSPITAL MANAGEMENT SYSTEM")

app = QApplication(sys.argv)
form = Form()
form.resize(1000,500)
form.show()
sys.exit(app.exec_())

