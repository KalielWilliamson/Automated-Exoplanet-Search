'''
Created on Aug 8, 2015

@author: Kaliel
'''
import PyQt4
class GUI():
    '''
    classdocs
    '''


    def makeButton(self):
            self.pushButton = QtGui.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(20, 540, 75, 23))
            self.pushButton.setObjectName(_fromUtf8("pushButton"))
            self.pushButton.setText(_translate("ExoplanetAnalysis", "Generate PDF", None))