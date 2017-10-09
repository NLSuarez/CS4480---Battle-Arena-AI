#!/usr/bin/python3
#Above line is only if you try to run it on Linux. This is originally meant for Windows.

import sys
#from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
	QPushButton, QToolTip)
from PyQt5.QtGui import (QIcon, QFont)

class Arena(QWidget):

	def __init__(self):
		super().__init__() #call the superclass's __init__ function.
		self.initUI() #then call the initUI function you design

	def initUI(self):
		QToolTip.setFont(QFont('SansSerif', 10))
		self.setToolTip('This is a <b>QWidget</b> widget')

		btn = QPushButton('Button', self)
		btn.setToolTip('This is a <b>QPushButton</b> widget')
		btn.resize(btn.sizeHint()) #sizeHint gives a recommended size
		btn.move(50, 50)

		self.setGeometry(200, 200, 600, 400)
		#combination of the following two lines with different parameters
		'''
		w.move(300, 300)
		w.resize(300, 220)
		'''
		self.setWindowTitle('Battle Arena RPG')
		self.setWindowIcon(QIcon('sword.ico'))
		self.show()


if __name__== '__main__':

	app = QApplication(sys.argv) 
	#An application is a superclass provided the system arguments
	#w = QWidget() #A default widget like this is a window.
	ba = Arena()

	sys.exit(app.exec_()) #Execution loop wrapped inside a safe exit method.
	#Will keep track of reasons for application closing