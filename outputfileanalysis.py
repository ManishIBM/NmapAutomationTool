import logging
import re
from fileinput import filename

class ExtractPorts:
    def __init__(self):
        self.content=''
        self.log = logging.getLogger('IPScanLog.ExtractPort')
        

    def readFile(self):
        logging.info(self.filePath)
        if self.filePath:
            try:
                file = open(self.filePath)
                self.content = file.read()
                file.close()
            except FileNotFoundError:
                logging.info("output file not found")
            return self.content
            #logging.info(self.content)


    def getTCPOpenPorts(self, fileName):
         
        self.log.info('inside getTcpopenports')
        if fileName:
            self.filePath = fileName
            self.readFile()
        else:
            return
        if self.content:
            #self.log.info(self.content)
            reFind = re.findall(r'(\d+)/tcp', self.content)
            #logging.info(reFind)
            return reFind

    def GetTcpPortInfo(self, fileName):
        if fileName:
            self.filePath = fileName
            self.readFile()
        else:
            return
        if self.content:
            #reFind =  self.content.split('PORT     STATE SERVICE       REASON')[1]
            
            reFind = (re.findall(r'.*/tcp.*', self.content))
            return reFind
    '''def PrintPort(self):
        ports = self.getTCPOpenPorts():
        if ports:
            print (ports)
        else:
            print ('No open port found')'''
                
