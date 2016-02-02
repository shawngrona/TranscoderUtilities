class PipelineResolver(object):
	def __init__(self,target):
		file = open('./config','r')
		content = file.read()
		paths = content.split('\n')
		self.pipelineid = None
		for path in paths:
			configline = path.split('=')
			if target == configline[0]:
				self.pipelineid = configline[1].split(',')[0]
				self.region = configline[1].split(',')[1]
				self.bucket = configline[0]
	def getRegion(self):
		return self.region			
	def getPipelineId(self):
		return self.pipelineid
	def getBucket(self):
		return self.bucket