# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import urllib.request
from DataGrabber import DataGrabber
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ExoplanetAnalysis(object):
    def setupUi(self, ExoplanetAnalysis):
        ExoplanetAnalysis.setObjectName(_fromUtf8("ExoplanetAnalysis"))
        ExoplanetAnalysis.resize(750, 600)
        self.centralwidget = QtGui.QWidget(ExoplanetAnalysis)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(400, 270, 331, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(270, 440, 82, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(270, 470, 82, 17))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 510, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 20, 701, 231))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.Options = QtGui.QTabWidget(self.centralwidget)
        self.Options.setGeometry(QtCore.QRect(400, 290, 331, 221))
        self.Options.setObjectName(_fromUtf8("Options"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 0, 331, 201))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.textBrowser = QtGui.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 331, 201))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.Options.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.frame_2 = QtGui.QFrame(self.tab_2)
        self.frame_2.setGeometry(QtCore.QRect(-1, -1, 331, 201))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.frame_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 331, 201))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.Options.addTab(self.tab_2, _fromUtf8(""))
        self.tableWidget = QtGui.QListWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 310, 101, 191))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        
        

        
        
        tableNames = ["exoplanets","cumulative","q1_q17_dr24_koi","q1_q16_koi","q1_q12_koi",
                      "q1_q8_koi","q1_q6_koi","q1_q17_dr24_tce","q1_q16_tce","q1_q12_tce","keplerstellar","q1_q17_dr24_stellar",
                      "q1_q16_stellar","q1_q12_stellar","keplertimeseries","k2targets","k2names","missionstars","mission_exocat"]
        n = 0
        for i in tableNames:
            item = QtGui.QListWidgetItem(tableNames[n])
            self.tableWidget.addItem(item)
            n += 1
        
        
        self.columnWidget = QtGui.QListWidget(self.centralwidget)
        self.columnWidget.setGeometry(QtCore.QRect(140, 310, 101, 191))
        self.columnWidget.setObjectName(_fromUtf8("columnWidget"))
        self.processWidget = QtGui.QListWidget(self.centralwidget)
        self.processWidget.setGeometry(QtCore.QRect(260, 310, 101, 121))
        self.processWidget.setObjectName(_fromUtf8("processWidget"))
        self.tableLine = QtGui.QLineEdit(self.centralwidget)
        self.tableLine.setGeometry(QtCore.QRect(20, 280, 101, 20))
        self.tableLine.setReadOnly(True)
        self.tableLine.setObjectName(_fromUtf8("tableLine"))
        self.columnLine = QtGui.QLineEdit(self.centralwidget)
        self.columnLine.setGeometry(QtCore.QRect(140, 280, 101, 20))
        self.columnLine.setReadOnly(True)
        self.columnLine.setObjectName(_fromUtf8("columnLine"))
        self.processLine = QtGui.QLineEdit(self.centralwidget)
        self.processLine.setGeometry(QtCore.QRect(260, 280, 101, 20))
        self.processLine.setReadOnly(True)
        self.processLine.setObjectName(_fromUtf8("processLine"))
        ExoplanetAnalysis.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ExoplanetAnalysis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        ExoplanetAnalysis.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ExoplanetAnalysis)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ExoplanetAnalysis.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(ExoplanetAnalysis)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(ExoplanetAnalysis)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionGenerate_Que = QtGui.QAction(ExoplanetAnalysis)
        self.actionGenerate_Que.setObjectName(_fromUtf8("actionGenerate_Que"))
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionGenerate_Que)
        self.menubar.addAction(self.menuFile.menuAction())
        
        
        self.retranslateUi(ExoplanetAnalysis)
        self.Options.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ExoplanetAnalysis)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), self.tableCopy)
        QtCore.QObject.connect(self.columnWidget, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), self.columnCopy)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Analyze)
        QtCore.QMetaObject.connectSlotsByName(ExoplanetAnalysis)
    
    
    def Analyze(self):
        table = self.tableLine.text()
        column = self.columnLine.text()
        order = ""
        if self.radioButton_2.isChecked():
            order = "dec"
        if self.radioButton_3.isChecked():
            order = "asc"
        matrix = DataGrabber(table,column,order)
        #matrix.printMatrix()
        self.textBrowser.setHtml(_translate("ExoplanetAnalysis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">"+matrix.text+"</span></p></body></html>", None))
        print(matrix.text)
    def getColumns(self,tableName):
        url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table="+tableName+"&getDefaultColumns"
        #bytes
        data = urllib.request.urlopen(url).read() 
        #decoded now
        text = data.decode('utf-8') 
        self.matrix = []
        #all rows in the text separated by newline
        columns = text.split(',')
        n = 0
        for i in columns:
            item = QtGui.QListWidgetItem(columns[n])
            self.columnWidget.addItem(item)
            n += 1
        

    def tableCopy(self):
        msg = self.tableWidget.currentItem().text()
        self.tableLine.setText(msg)
        self.columnWidget.clear()
        self.columnLine.clear()
        self.columnLine.show()
        self.columnWidget.show()

        self.getColumns(msg)
        
    def columnCopy(self):
        try:
            msg = self.columnWidget.currentItem().text()
        except:
            msg = ""
        prev = self.columnLine.text()
        if prev == "":
            if msg not in prev:
                self.columnLine.setText(msg)
        else:
            if msg not in prev:
                self.columnLine.setText(prev+','+msg)


    def retranslateUi(self, ExoplanetAnalysis):
        ExoplanetAnalysis.setWindowTitle(_translate("ExoplanetAnalysis", "ExoplanetAnalysis", None))
        self.radioButton_2.setText(_translate("ExoplanetAnalysis", "Descending", None))
        self.radioButton_3.setText(_translate("ExoplanetAnalysis", "Ascending", None))
        self.pushButton.setText(_translate("ExoplanetAnalysis", "Analyze", None))
        self.textBrowser.setHtml(_translate("ExoplanetAnalysis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Options...</span></p></body></html>", None))
        self.Options.setTabText(self.Options.indexOf(self.tab), _translate("ExoplanetAnalysis", "EXONEST Options", None))
        self.textBrowser_2.setHtml(_translate("ExoplanetAnalysis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Output...</span></p></body></html>", None))
        self.Options.setTabText(self.Options.indexOf(self.tab_2), _translate("ExoplanetAnalysis", "EXONEST Text Output", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(True)
        
        
        
        
        
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("ExoplanetAnalysis", "File", None))
        self.actionSave.setText(_translate("ExoplanetAnalysis", "Save", None))
        self.actionExit.setText(_translate("ExoplanetAnalysis", "Exit", None))
        self.actionGenerate_Que.setText(_translate("ExoplanetAnalysis", "Generate Que", None))
    

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ExoplanetAnalysis = QtGui.QMainWindow()
    ui = Ui_ExoplanetAnalysis()
    ui.setupUi(ExoplanetAnalysis)
    ExoplanetAnalysis.show()
    sys.exit(app.exec_())

