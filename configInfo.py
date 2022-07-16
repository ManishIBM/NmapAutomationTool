import configparser

class ConfigInfo():

	def __init__(self, configName=''):
		
		if len(configName):
			self.configFile = configName
		else:
			self.configFile = 'NWPenConfig.ini'
			
		self.config = configparser.ConfigParser()
		self.configData = {}
		self.config.read(self.configFile)
		#self.configData = self.config
		
	def SetConfigParamValue(self, section, param, value):
		if not self.config.has_section(section):		
			self.config[section] = {}
		self.config[section][param] = value
		
	def UpdateConfig(self):
		'''for section, value in self.configData.items():
			self.config[section][] = value'''
		
		with open(self.configFile, 'w') as configFp:
			self.config.write(configFp)
			configFp.close()
	
	def GetConfigParamValue(self, section, param):
		return self.config[section][param]
	
