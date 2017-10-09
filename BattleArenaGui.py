#!/usr/bin/python3
#Above line is only if you try to run it on Linux. This is originally meant for Windows.

import sys
from PyQt5.QtCore import QCoreApplication #For getting to the application instance
from PyQt5.QtWidgets import (QApplication, QWidget,
	QPushButton, QToolTip, QMessageBox, 
	QDesktopWidget, QMainWindow, QAction, qApp,
	QTextEdit)

	#QWidget is for windows other than main window
	#Main window allows for menu bars and such
from PyQt5.QtGui import (QIcon, QFont)

class Arena(QMainWindow):

	def __init__(self):
		super().__init__() #call the superclass's __init__ function.
		self.initUI() #then call the initUI function you design
		#self.createGame()

	def initUI(self):
		QToolTip.setFont(QFont('SansSerif', 10))

		textEdit = QTextEdit()
		self.setCentralWidget(textEdit)
		
		startAct = QAction(QIcon('startBattle.png'), '&New Game', self)
		startAct.setShortcut('Ctrl+N')
		startAct.setStatusTip('New Game')
		startAct.triggered.connect(qApp.quit)

		exitAct = QAction(QIcon('shattered-sword.png'), '&Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.setStatusTip('Exit Application')
		exitAct.triggered.connect(qApp.quit)

		gameMenu = self.addToolBar('&Main Menu')
		gameMenu.addAction(startAct)
		gameMenu.addAction(exitAct)

		self.statusBar()

		self.resize(600, 400)
		self.center()
		self.setWindowTitle('Battle Arena RPG')
		self.setWindowIcon(QIcon('sword.ico'))
		self.show()

	def center(self):
		qr = self.frameGeometry()
		#We get a rectangle specifying the geometry of the main window. This includes any window frame. 
		cp = QDesktopWidget().availableGeometry().center()
		#We figure out the screen resolution of our monitor. And from this resolution, we get the center point. 
		qr.moveCenter(cp)
		#Our rectangle has already its width and height. Now we set the center of the rectangle to the center 
		#of the screen. The rectangle's size is unchanged. 
		self.move(qr.topLeft())
		#Finally, we move the top-left point of the application window to the top-left point of the qr rectangle, 
		#thus centering the window on our screen. 

	def closeEvent(self, event):

		reply = QMessageBox.question(self, 'Leaving so soon?',
			"Are you sure you want to forefeit?", QMessageBox.Yes |
			QMessageBox.No, QMessageBox.No)

		'''
		From zetcode.com/gui/pyqt5/firstprograms:
		We show a message box with two buttons: Yes and No. The first string appears on the titlebar. The second string 
		is the message text displayed by the dialog. The third argument specifies the combination of buttons appearing 
		in the dialog. The last parameter is the default button. It is the button which has initially the keyboard focus.
		The return value is stored in the reply variable. 
		'''

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	#def createGame(self):

if __name__== '__main__':

	app = QApplication(sys.argv) 
	#An application is a superclass provided the system arguments
	#w = QWidget() #A default widget like this is a window.
	ba = Arena()

	sys.exit(app.exec_()) #Execution loop wrapped inside a safe exit method.
	#Will keep track of reasons for application closing