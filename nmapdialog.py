# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Assignments\Python\UI\nmapdialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QListWidgetItem, QTableWidgetItem
from PyQt5.Qt import QPixmap
import threading
import copy
import pathlib
import pymsgbox
import logging
import threadedscan
import configInfo
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, pyqtSignal
import outputfileanalysis
import webbrowser
import configdlg
import subprocess

objConfig = configInfo.ConfigInfo()

logIPScan = logging.getLogger('IPScanLog')
logIPScan.setLevel(logging.INFO)

#TODO: get from config file
logIPFile = logging.FileHandler(objConfig.GetConfigParamValue('URI', 'logfileuri'), mode='w')
logIPFile.setLevel(logging.INFO)

logIPStream = logging.StreamHandler()
logIPStream.setLevel(logging.ERROR)

formatter =  logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logIPFile.setFormatter(formatter)
logIPStream.setFormatter(formatter)

logIPScan.addHandler(logIPFile)
logIPScan.addHandler(logIPStream)

class Ui_Dialog(QObject):
    trigger = pyqtSignal()
    scanDone = pyqtSignal()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.resize(682, 512)
        Dialog.setFixedSize(682, 534)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 661, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_Top = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_Top.setTitle("")
        self.groupBox_Top.setObjectName("groupBox_Top")
        self.label_PTCImage = QtWidgets.QLabel(self.groupBox_Top)
        self.label_PTCImage.setGeometry(QtCore.QRect(0, 0, 661, 91))
        self.label_PTCImage.setObjectName("label_PTCImage")
        #self.label_PTCImage.raise_()
        

        self.verticalLayout.addWidget(self.groupBox_Top)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 109, 151, 341))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_Left = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_Left.setObjectName("groupBox_Left")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_Left)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 130, 309))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFontPointSize(10)
        self.horizontalLayout.addWidget(self.groupBox_Left)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 483, 661, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_Bottom = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_Bottom.setTitle("")
        self.groupBox_Bottom.setObjectName("groupBox_Bottom")
        self.pushButton_Scan = QtWidgets.QPushButton(self.groupBox_Bottom)
        self.pushButton_Scan.setGeometry(QtCore.QRect(490, 8, 75, 23))
        self.pushButton_Scan.setObjectName("pushButton_Scan")
        self.pushButton_Cancel = QtWidgets.QPushButton(self.groupBox_Bottom)
        self.pushButton_Cancel.setGeometry(QtCore.QRect(577, 8, 75, 23))
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.pushButton_Config = QtWidgets.QPushButton(self.groupBox_Bottom)
        self.pushButton_Config.setGeometry(QtCore.QRect(10, 8, 75, 23))
        self.pushButton_Config.setObjectName("pushButton_Config")
        self.label_location = QtWidgets.QLabel(self.groupBox_Bottom)
        self.label_location.setGeometry(QtCore.QRect(100, 8, 371, 20))
        self.label_location.setObjectName("label_location")
        self.verticalLayout_2.addWidget(self.groupBox_Bottom)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(160, 109, 511, 341))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_Right = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_Right.setObjectName("groupBox_Right")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_Right)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 121, 309))
        self.listWidget.setObjectName("listWidget")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 457, 661, 18))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(0)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_Right)
        self.tableWidget.setGeometry(QtCore.QRect(130, 20, 370, 309))
        self.tableWidget.setAutoFillBackground(True)
        #self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setHorizontalHeaderLabels(['Port', 'Service', 'Path'])
        self.tableWidget.setColumnWidth(0, 60)  
        self.tableWidget.setColumnWidth(1, 90)  
        self.tableWidget.setColumnWidth(2, 200)  
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.groupBox_Right)
        self.verticalLayoutWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.groupBox_Bottom.raise_()

        self.pushButton_Scan.clicked.connect(self.ScanButtonClicked)
        self.pushButton_Cancel.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.pushButton_Config.clicked.connect(self.LaunchConfigDialog)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.outputPath = objConfig.GetConfigParamValue('PATH', 'opscanpath')
        self.listWidget.clicked.connect(self.UpdatePortTable)
        self.label_location.setText('Scan Output Directory:'+ self.outputPath)
        
        self.tableWidget.doubleClicked.connect(self.OpenPortFile)
        #self.tableWidget.setEditTriggers(QtGui.QAbstractTextDocumentLayout.)

        pixmap = QPixmap('PTC.jpg')
        #pixmap = pixmap.scaledToHeight(61)
        pixmap = pixmap.scaledToWidth(661)
        self.label_PTCImage.setPixmap(pixmap)

        self.threadLock = threading.Lock()
        self.scannedIp = {}
        self.completedScan = []
        self.init = False
        
        self.log = logging.getLogger('IPScanLog.UIDialog')
        self.log.info('IPScan UIDialog started')     
        
        self.progressBar.setTextVisible(True)   

        inputIPs = objConfig.GetConfigParamValue('IPTOSCAN', 'ips')
        if len(inputIPs) > 0:
            self.init = True
            self.textEdit.setText(inputIPs)
            self.ips = inputIPs.split()
            self.UpdateScannedIP()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NetworkScanner"))
        self.groupBox_Left.setTitle(_translate("Dialog", "IP(s)"))
        self.pushButton_Scan.setText(_translate("Dialog", "Scan"))
        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))
        self.pushButton_Config.setText(_translate("Dialog", "Configure"))
        self.label_location.setText(_translate("Dialog", "TextLabel"))
        self.label_PTCImage.setText(_translate("Dialog", "TextLabel"))
        
        self.groupBox_Right.setTitle(_translate("Dialog", "ScanStatus"))
        self.tableWidget.setSortingEnabled(True)
        
         
    def ScanButtonClicked(self):        
        #Get IP list
        ips = self.textEdit.toPlainText().strip()
        objConfig.SetConfigParamValue('IPTOSCAN', 'ips', ips)
        objConfig.UpdateConfig()
        self.ips = ips.split()
        self.UpdateScannedIP()
        
        ipsToScan = list(set(self.ips) - set(self.completedScan))
        if len(ipsToScan) <= 0:
            buttonReply = pymsgbox.confirm("All IPs are already scanned. Do you want to rescan?", 'Network Scan', ['Yes, rescan', 'No'])
            if buttonReply == 'No':
                return
            self.RescanInit()
            return
            
        self.InitiateScan(self.ips)
        #self.textEdit.setReadOnly(True)
        self.pushButton_Scan.setEnabled(False)
        
    def UpdateScannedIP(self): 
        objThreadedScan = threadedscan.MultiThreadedIPScan('')   
        scannedIPs = objThreadedScan.ReadOpFile()
        if len(scannedIPs):
            self.scannedIp = scannedIPs
            self.init = True
            self.UpdateWidgets()
            
    def RescanInit(self):
        self.scannedIp = []
        self.init = False
        
        try:
            fileHandle = open(objConfig.GetConfigParamValue('URI', 'scanstate'), 'wb') 
            fileHandle.close()
        except FileNotFoundError:
            logging.info("Failed to write content in file")

        while(self.tableWidget.rowCount()>0):
            self.tableWidget.removeRow(0)
            
        self.listWidget.clear()
        self.progressBar.setValue(0)
        

       
    def InitiateScan(self, ips):
        #Creating object to read the state file
        #self.objThreadedScanStatus = threadedscan.MultiThreadedIPScan(self.ips)
        #self.objThreadedScanStatus.SetConditionalLock(self.threadLock)
        if len(ips) <= 0:
            return
        
        self.init = False
        scanThread = threading.Thread(target=self.StartScan, args=([self.threadLock,ips]))
        scanThread.start()
        
    def StartScan(self, lockObj, ips):
        objThreadedScan = threadedscan.MultiThreadedIPScan(ips)
        objThreadedScan.SetPointer(self)
        objThreadedScan.SetConditionalLock(lockObj)
        objThreadedScan.FindPortsOfIPs()
                    
    def IsIPScanning(self, dicPorts):
        count = 0
        for port, flag in dicPorts.items():
            if flag:
                count = count+1
        return count
       

    def UpdateWidgets(self):
                    
        if not self.init:
            self.threadLock.acquire()
            self.scannedIp = copy.copy(threadedscan.MultiThreadedIPScan.staticScannedIps)
            self.threadLock.release()
        
        if len(self.scannedIp) == len(self.completedScan):
            #self.log.info('set: %s %s', self.scannedIp.keys(), self.completedScan)
            return
        
        completionPercentage = 100*(len(self.scannedIp)-1)/len(self.ips)
        
        count = 0
        scanningDictPort = {}
        for ipKey, dictPort in self.scannedIp.items():
            
            if ipKey in self.completedScan:
                continue
            foundItem = self.listWidget.findItems(ipKey, QtCore.Qt.MatchExactly)
            if len(foundItem) <= 0:
                keyItem = QListWidgetItem(ipKey)
                keyItem.setBackground(QtGui.QColor(255,255,0))
                self.listWidget.addItem(keyItem)
            #self.textEdit.setPlainText(ipKey)
            #if we get scanning IP, no need to get count for others
            count = self.IsIPScanning(dictPort)
            scanningDictPort = dictPort

            if count == len(dictPort):
                self.completedScan.append(ipKey)
                if not foundItem:
                    foundItem = self.listWidget.findItems(ipKey, QtCore.Qt.MatchExactly)
                for item in foundItem:
                    item.setBackground(QtGui.QColor(0,255,0))
                
        self.log.info('completionPercentage %d  %d', completionPercentage, count)    
        if count:
            portscancompletion = 100*count/len(scanningDictPort)
        else:
            portscancompletion = 0
        #self.log.info('completionPercentage %s', completionPercentage)
        completionPercentage = completionPercentage + portscancompletion* 1/len(self.ips)
        self.progressBar.setValue(completionPercentage)
        
        ipSelected = self.listWidget.selectedItems()
        if len(ipSelected):
            ip = ipSelected[0].text()
            if ip not in self.completedScan:
                self.UpdatePortTable()
        
    #UPdate table for selected IP
    def UpdatePortTable(self):
        ip = self.listWidget.selectedItems()[0].text().strip()
        
        outputPath = pathlib.Path(self.outputPath).joinpath(ip)
        if not outputPath.exists():
            self.log.info('Output file for IP %s does not exist: ', ip)
            return
        outputFile = outputPath.joinpath(ip+'.txt')
        outputFileData = outputfileanalysis.ExtractPorts()
        
        portDataList = outputFileData.GetTcpPortInfo(outputFile)
        
        row = 0
        totalRows = len(self.scannedIp[ip])
        
        while(self.tableWidget.rowCount()>0):
            self.tableWidget.removeRow(0)
        #totalRows = 20
        self.tableWidget.setRowCount(totalRows)
        for portData in portDataList:
            if portData.lower().find('tcp') or portData.lower().find('udp'):
                portDataInfo = portData.split()
                port = portDataInfo[0].split('/')[0]
                
                if not self.IsPortScanned(ip, port):
                    continue
                self.tableWidget.setItem(row, 0, QTableWidgetItem(portDataInfo[0]))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(portDataInfo[2]))
               
                filePathCol = QTableWidgetItem()
                #filepath = outputPath.joinpath(ip+'_'+port+'.txt')
                
                filePathCol.setText(ip+'/'+ip+'_'+port+'.txt')
                self.tableWidget.setItem(row, 2, filePathCol)
                row = row+1
            else:
                break
    
    def IsPortScanned(self, ip, port): 
        portDic = self.scannedIp[ip]
        if port in portDic:
            return portDic[port]
        return False          
    
    def OpenPortFile(self):
        selectedItem = ''
        if self.tableWidget.currentColumn() == 2:
            selectedItem = self.tableWidget.selectedItems()[0].text()
            outputPortFile = pathlib.Path(self.outputPath).joinpath(selectedItem)
            webbrowser.open(outputPortFile)
        return
    def LaunchConfigDialog(self):
        objConfigDlg = configdlg.ConfigAppWindow()
        if objConfigDlg.exec_():
            subprocess.run('NetworkScanner.exe')
            exit(0)
    
    def ScanFinishAct(self):
        #self.textEdit.setReadOnly(False)
        self.pushButton_Scan.setEnabled(True)
        return
        
class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
       
def ui():
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())  


if __name__ == '__main__':
    #main()
    ui()
