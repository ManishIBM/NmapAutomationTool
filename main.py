import configInfo
import nmapscan
from nmapscan import NmapScan
import logging
import nmapdialog
import sys
from PyQt5.QtWidgets import QApplication

logIPScan = logging.getLogger('IPScanLog')
logIPScan.setLevel(logging.INFO)


objConfig = configInfo.ConfigInfo()
logFile = objConfig.GetConfigParamValue('URI', 'logfileuri')
#TODO: get from config file
logIPFile = logging.FileHandler(logFile, mode='w')
logIPFile.setLevel(logging.INFO)

logIPStream = logging.StreamHandler()
logIPStream.setLevel(logging.ERROR)

formatter =  logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logIPFile.setFormatter(formatter)
logIPStream.setFormatter(formatter)

logIPScan.addHandler(logIPFile)
logIPScan.addHandler(logIPStream)

def UpdateConfig():
    objConfig = configInfo.ConfigInfo()
    
    '''objConfig.SetConfigParamValue('URI', 'LogFileURI', 'c:/python/test.log')

    objConfig.SetConfigParamValue('URI', 'OPFileURI', 'c:/temp/IPscanoutput.txt')
    
    objConfig.SetConfigParamValue('URI', 'SerializationURI', 'c:/temp/IPscan.txt')
    
    objConfig.SetConfigParamValue('THREADS', 'MaxIPThread', '5')

    objConfig.SetConfigParamValue('THREADS', 'MaxPortThread', '5')'''
    
    objConfig.SetConfigParamValue('NMAPFLAGS', 'PortDiscovery', '-Pn -sS -p- -T4 -vv -min-parallelism 8')
    
    objConfig.UpdateConfig()
    
    
     

def main():

    #UpdateConfig()
    ip = '127.0.0.1'
    objnmap = NmapScan()
    #objnmap.StartPortScan('127.0.0.1')
    objnmap.StartOsSvcScan(ip, 445)

    #UpdateConfig()
    #objConfig = configInfo.configInfo('Testconfig.ini')
    #print (objConfig.GetConfigParamValue('THREADS', 'MaxPortThread'))
    
def ui():
    app = QApplication(sys.argv)
    w = nmapdialog.AppWindow()
    w.show()
    sys.exit(app.exec_())  


if __name__ == '__main__':
    #main()
    ui()