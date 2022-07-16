import subprocess
import configInfo
import pathlib
import logging

class NmapScan:
    _nmapPath = ''
    
    def __init__(self):
        
        self.log = logging.getLogger('IPScanLog.NmapScan')
        self.log.info('IPScan log started')        
        
        self.objConfig = configInfo.ConfigInfo()
        self.outputPath = pathlib.Path(self.objConfig.GetConfigParamValue('PATH', 'OPScanPath'))
        
        self.nmapPortFlags = self.NmapConfigOptions('NMAPFLAGS', 'PortDiscovery')
        self.nmapOsSvcFlags = self.NmapConfigOptions('NMAPFLAGS', 'portsvcosdisc')
        self.nmapOtherFlags = self.NmapConfigOptions('NMAPFLAGS', 'othernmapflag')
        
    def GetOPPath(self):
        return self.outputPath
        
    def NmapConfigOptions(self, section, param):
        strFlags = self.objConfig.GetConfigParamValue(section, param)
        nmapFlags = strFlags.split()
        nmapURI = self.objConfig.GetConfigParamValue('URI', 'nmapuri')
        nmapFlags.insert(0, nmapURI)
        nmapFlags.append('-oN')
        
        return nmapFlags
    
    def RunNmapCmd(self, nmapCmd):
        try:
            result = subprocess.run(nmapCmd)

            if result.returncode == 0:
                self.log.info('Response of subprocess: %s', result.stdout)
            else:
                self.log.info('Unsuccessfull :%s', result.returncode)
        except :
            #nmapCmd.kill()
            self.log.info('exception found')

                
    def StartPortScan(self, ip):
       
        #Create folder with ip and output filename        
        outputPath = self.outputPath.joinpath(ip)
        if not outputPath.exists():
            outputPath.mkdir(parents=True)
        outputFile = outputPath.joinpath(ip+'.txt')
        
        nmapCmd = self.nmapPortFlags
        nmapCmd.append(str(outputFile))
        nmapCmd.append(ip)
        
        self.log.info('nmap cmd: %s', str(nmapCmd))
        self.RunNmapCmd(nmapCmd)
        
    def StartOsSvcScan(self, ip, port):
        
        self.PortSpecificScan(ip, port, self.nmapOsSvcFlags)
        
    def StartNmapFlagPortScan(self, ip, port):
        self.PortSpecificScan(ip, port, self.nmapOtherFlags)
        
    def PortSpecificScan(self,ip, port, nmapFlags):
        
        outputPath = self.outputPath.joinpath(ip)
        
        if not outputPath.exists():
            outputPath.mkdir(parents=True)
        outputFile = outputPath.joinpath(ip + '_' + str(port) +'.txt')
        
        nmapCmd = nmapFlags
        nmapCmd.append(str(outputFile))
        nmapCmd.append('-p')
        nmapCmd.append(str(port))
        nmapCmd.append(ip)
        
        self.log.info('nmap cmd: %s', str(nmapCmd))
        self.RunNmapCmd(nmapCmd)    
        
        
           
        
        
