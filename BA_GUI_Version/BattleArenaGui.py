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
from PyQt5.QtGui import (QIcon, QFont, QTextCursor)

#My modules
from BADataObjects import Battle, HumanCombatant, AICombatant
from BAHelpFunctions import createMoveset, createMoveGuide
from PartialObserveArena import Partial_Observe

class Arena(QMainWindow):

	def __init__(self):
		super().__init__() #call the superclass's __init__ function.
		self.initUI() #then call the initUI function you design
		#self.createGame()

	def initUI(self):
		QToolTip.setFont(QFont('SansSerif', 10))

		#Output Widget
		battleStatus = QTextEdit()
		battleStatus.setReadOnly(True)
		battleStatus.moveCursor(QTextCursor.End)
		sb = battleStatus.verticalScrollBar()
		sb.setValue(sb.maximum())
		self.setCentralWidget(battleStatus)

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

	#Create the necessary objects for attack moves and store them
	Available_Moves = createMoveset()
	#Create human player stats
	Human = HumanCombatant("Stefan")
	#Create AI player stats
	ai_algo = Partial_Observe(2)
	AI = AICombatant(ai_algo, "Computer")

	'''Create game object and operate.'''
	ArenaMatch = Battle( Available_Moves, [Human, AI])
	'''Need to functionally convert this to the GUI version.
	while not ArenaMatch.is_over():
		print("\n")
		ArenaMatch.show()
		print("\n")
		if ArenaMatch.nplayer==1:  # we are assuming player 1 is a Human_Player
			poss = ArenaMatch.possible_moves()
			for index, move in enumerate(poss):
				print("{} : {}".format(index, move.NAME))
			print("\n")
			index = int(input("Choose attack number: "))
			move = poss[index]
			print("\n")
			print("You used '{}'.".format(move.NAME))
			print("\n")
		else:  # we are assuming player 2 is an AI_Player
			move = ArenaMatch.get_move()
			print("\n")
			print("The Computer used '{}'.".format(move.NAME))
			print("\n")

		damage = ArenaMatch.play_move(move) #Method returns damage for us.
		print("It did {} points in {} and {} damage.".format(damage, move.ELEMENT, move.TYPE))

		if move.ELEMENT == ArenaMatch.player.ELEMENTAL_WEAKNESS and move.ELEMENT == ArenaMatch.opponent.ELEMENTAL_AFFINITY:
			print("It was super effective and enhanced!")
		elif move.ELEMENT == ArenaMatch.player.ELEMENTAL_WEAKNESS:
			print("It was super effective!")
		elif move.ELEMENT == ArenaMatch.opponent.ELEMENTAL_AFFINITY:
			print("It was enhanced!")
	print("\n")
	if AI.HP == 0:
		print("Congratulations, human. You beat me.")
	elif Human.HP == 0:
		print("Game Over. You lost.")

	'''
	app = QApplication(sys.argv)
	#An application is a superclass provided the system arguments
	#w = QWidget() #A default widget like this is a window.
	ba = Arena()
	statusArea = ba.centralWidget()
	statusArea.append("Hello")
	statusArea.append("\nI am working.")


	sys.exit(app.exec_()) #Execution loop wrapped inside a safe exit method.
	#Will keep track of reasons for application closing
