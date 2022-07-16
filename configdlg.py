# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Config.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import  QDialog, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import configInfo

class Ui_ConfigurationDialog(object):
    def setupUi(self, ConfigurationDialog):
        ConfigurationDialog.setObjectName("ConfigurationDialog")
        ConfigurationDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ConfigurationDialog.resize(520, 250)
        self.verticalLayoutWidget = QtWidgets.QWidget(ConfigurationDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 501, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxNmap = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBoxNmap.setObjectName("groupBoxNmap")
        self.label = QtWidgets.QLabel(self.groupBoxNmap)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label.setObjectName("label")
        self.lineEdit_Port = QtWidgets.QLineEdit(self.groupBoxNmap)
        self.lineEdit_Port.setGeometry(QtCore.QRect(95, 20, 311, 20))
        self.lineEdit_Port.setObjectName("lineEdit_Port")
        self.label_2 = QtWidgets.QLabel(self.groupBoxNmap)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_Svc = QtWidgets.QLineEdit(self.groupBoxNmap)
        self.lineEdit_Svc.setGeometry(QtCore.QRect(95, 50, 311, 20))
        self.lineEdit_Svc.setObjectName("lineEdit_Svc")
        self.label_3 = QtWidgets.QLabel(self.groupBoxNmap)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_Other = QtWidgets.QLineEdit(self.groupBoxNmap)
        self.lineEdit_Other.setGeometry(QtCore.QRect(95, 80, 311, 20))
        self.lineEdit_Other.setObjectName("lineEdit_Other")
        self.label_4 = QtWidgets.QLabel(self.groupBoxNmap)
        self.label_4.setGeometry(QtCore.QRect(410, 20, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBoxNmap)
        self.label_5.setGeometry(QtCore.QRect(410, 50, 41, 16))
        self.label_5.setObjectName("label_5")
        self.spinBox_port = QtWidgets.QSpinBox(self.groupBoxNmap)
        self.spinBox_port.setGeometry(QtCore.QRect(460, 20, 30, 20))
        self.spinBox_port.setObjectName("spinBox_port")
        self.spinBox_Discovery = QtWidgets.QSpinBox(self.groupBoxNmap)
        self.spinBox_Discovery.setGeometry(QtCore.QRect(460, 50, 30, 20))
        self.spinBox_Discovery.setObjectName("spinBox_Discovery")
        self.verticalLayout.addWidget(self.groupBoxNmap)
        self.pushButton_Done = QtWidgets.QPushButton(ConfigurationDialog)
        self.pushButton_Done.setGeometry(QtCore.QRect(430, 185, 75, 25))
        self.pushButton_Done.setObjectName("pushButton_Done")
        self.pushButton_Cancel = QtWidgets.QPushButton(ConfigurationDialog)
        self.pushButton_Cancel.setGeometry(QtCore.QRect(430, 215, 75, 25))
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(ConfigurationDialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 129, 411, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_OPDir = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_OPDir.setGeometry(QtCore.QRect(95, 20, 275, 20))
        self.lineEdit_OPDir.setObjectName("lineEdit_OPDir")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_LogFile = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_LogFile.setGeometry(QtCore.QRect(95, 50, 275, 20))
        self.lineEdit_LogFile.setObjectName("lineEdit_LogFile")
        self.pushButton_OPDir = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_OPDir.setGeometry(QtCore.QRect(380, 20, 22, 20))
        self.pushButton_OPDir.setObjectName("pushButton_OPDir")
        self.pushButton_LogFile = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_LogFile.setGeometry(QtCore.QRect(380, 50, 22, 20))
        self.pushButton_LogFile.setObjectName("pushButton_LogFile")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_Nmap = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Nmap.setGeometry(QtCore.QRect(95, 80, 275, 20))
        self.lineEdit_Nmap.setObjectName("lineEdit_Nmap")
        self.pushButton_nmap = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nmap.setGeometry(QtCore.QRect(380, 80, 22, 20))
        self.pushButton_nmap.setObjectName("pushButton_nmap")
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(ConfigurationDialog)
        QtCore.QMetaObject.connectSlotsByName(ConfigurationDialog)
        
        self.objConfigInfo = configInfo.ConfigInfo()
        
        self.dialogInstance = ConfigurationDialog
        self.pushButton_Done.clicked.connect(self.SaveConfiguration)
        self.pushButton_Cancel.clicked.connect(ConfigurationDialog.reject)
        self.pushButton_OPDir.clicked.connect(self.SetOPDirectory)
        self.pushButton_LogFile.clicked.connect(self.SetLogDirectory)
        self.pushButton_nmap.clicked.connect(self.SetNmapDirectory)
        
        
        self.SetConfigDataToUI()

    def retranslateUi(self, ConfigurationDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfigurationDialog.setWindowTitle(_translate("ConfigurationDialog", "Basic Configuration"))
        self.groupBoxNmap.setTitle(_translate("ConfigurationDialog", "NmapOptions"))
        self.label.setText(_translate("ConfigurationDialog", "PortDicovery"))
        self.lineEdit_Port.setText(_translate("ConfigurationDialog", "-Pn -sS -p- -T4 -vv -min-parallelism 8"))
        self.label_2.setText(_translate("ConfigurationDialog", "ServiceDicovery"))
        self.lineEdit_Svc.setText(_translate("ConfigurationDialog", "-Pn -sS -sV --version-all -O --script discovery -T4 -vv --min-parallelism 8 --max-retries 2"))
        self.label_3.setText(_translate("ConfigurationDialog", "Otherflags"))
        self.lineEdit_Other.setText(_translate("ConfigurationDialog", "Not required"))
        self.label_4.setText(_translate("ConfigurationDialog", "Threads"))
        self.label_5.setText(_translate("ConfigurationDialog", "Threads"))
        self.pushButton_Done.setText(_translate("ConfigurationDialog", "Done"))
        self.pushButton_Cancel.setText(_translate("ConfigurationDialog", "Cancel"))
        self.groupBox.setTitle(_translate("ConfigurationDialog", "Path Selection"))
        self.label_6.setText(_translate("ConfigurationDialog", "Output Directory"))
        self.lineEdit_OPDir.setText(_translate("ConfigurationDialog", "c:\\Temp"))
        self.label_7.setText(_translate("ConfigurationDialog", "Logfile Path"))
        self.lineEdit_LogFile.setText(_translate("ConfigurationDialog", "c:\\Logfile.txt"))
        self.pushButton_OPDir.setText(_translate("ConfigurationDialog", "..."))
        self.pushButton_LogFile.setText(_translate("ConfigurationDialog", "..."))
        self.label_8.setText(_translate("ConfigurationDialog", "Nmap Path"))
        self.lineEdit_Nmap.setText(_translate("ConfigurationDialog", "nmap"))
        self.pushButton_nmap.setText(_translate("ConfigurationDialog", "..."))

    def SetOPDirectory(self):
        dlg = QtWidgets.QFileDialog() 
        dlg.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        if dlg.exec_():
            self.lineEdit_OPDir.setText(dlg.selectedFiles()[0])
            self.lineEdit_LogFile.setText(dlg.selectedFiles()[0]+'/NetworkScan.log')

    def SetLogDirectory(self):
        dlg = QtWidgets.QFileDialog() 
        dlg.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        if dlg.exec_():
            self.lineEdit_LogFile.setText(dlg.selectedFiles()[0]+'/NetworkScan.log')

    def SetNmapDirectory(self):
        dlg = QtWidgets.QFileDialog() 
        dlg.setFileMode(QtWidgets.QFileDialog.AnyFile)
        dlg.setNameFilter("(*.exe)")
        if dlg.exec_():
            self.lineEdit_Nmap.setText(dlg.selectedFiles()[0])

    def SaveConfiguration(self):
        self.GetUiData()
        self.objConfigInfo.UpdateConfig()
        self.dialogInstance.accept()

    def GetUiData(self):
        self.objConfigInfo.SetConfigParamValue('NMAPFLAGS', 'PortDiscovery', self.lineEdit_Port.text())
        self.objConfigInfo.SetConfigParamValue('NMAPFLAGS', 'portsvcosdisc', self.lineEdit_Svc.text())
        self.objConfigInfo.SetConfigParamValue('NMAPFLAGS', 'othernmapflag', self.lineEdit_Other.text())
        self.objConfigInfo.SetConfigParamValue('THREADS', 'maxipthread', str(self.spinBox_port.value()))
        self.objConfigInfo.SetConfigParamValue('THREADS', 'maxportthread', str(self.spinBox_Discovery.value()))

        self.objConfigInfo.SetConfigParamValue('PATH', 'opscanpath', self.lineEdit_OPDir.text())
        self.objConfigInfo.SetConfigParamValue('URI', 'logfileuri', self.lineEdit_LogFile.text())
        self.objConfigInfo.SetConfigParamValue('URI', 'nmapuri', self.lineEdit_Nmap.text())

        self.objConfigInfo.SetConfigParamValue('URI', 'scanstate', self.lineEdit_OPDir.text()+'/ScanState')
        
    def SetConfigDataToUI(self):
        self.lineEdit_Port.setText(self.objConfigInfo.GetConfigParamValue('NMAPFLAGS', 'PortDiscovery'))
        self.lineEdit_Svc.setText(self.objConfigInfo.GetConfigParamValue('NMAPFLAGS', 'portsvcosdisc'))
        self.lineEdit_Other.setText(self.objConfigInfo.GetConfigParamValue('NMAPFLAGS', 'othernmapflag'))
        self.spinBox_port.setValue(int(self.objConfigInfo.GetConfigParamValue('THREADS', 'maxipthread')))
        self.spinBox_Discovery.setValue(int(self.objConfigInfo.GetConfigParamValue('THREADS', 'maxportthread')))
        
        self.lineEdit_OPDir.setText(self.objConfigInfo.GetConfigParamValue('PATH', 'opscanpath'))
        self.lineEdit_LogFile.setText(self.objConfigInfo.GetConfigParamValue('URI', 'logfileuri'))
        self.lineEdit_Nmap.setText(self.objConfigInfo.GetConfigParamValue('URI', 'nmapuri'))
        
class ConfigAppWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui1 = Ui_ConfigurationDialog()
        self.ui1.setupUi(self)
        
