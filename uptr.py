
import sys
from sys import stdin
import pexpect
import transcode
from pipelineresolver import PipelineResolver

SOURCE = ""
TARGET = ""
PIPELINEID = ""
REGION=""


def isValidForTranscode(path):
	if '.mts' in path and '=>' in path:
		return True
	else:
		return False

### entry point

print "This script will upload files recursively from a target and call transcode for completed uploads"
print ""
print "Please enter the source (directory only):"
SOURCE = stdin.readline().rstrip('\n')

print "Please enter the target bucket:"
TARGET = stdin.readline().rstrip('\n')

pr = PipelineResolver(TARGET)

PIPELINEID = pr.getPipelineId()
REGION = pr.getRegion()

if PIPELINEID != None:
	print "resolved pipelineid:"+PIPELINEID+"\n"
	print "resolved region:"+REGION+"\n"
	
	command = 's4cmd put '+SOURCE+'/ s3://'+TARGET+'/ -r'
	print "running command ",command
	
	child = pexpect.spawn(command, timeout=None) #do not time out
	for line in child:
		print 'got output from s4cmd:'+line
		if isValidForTranscode(line):
			path_plus_file = line.split('=>')[1].replace(' ','')
			path_plus_file = path_plus_file.replace('s3://'+TARGET+'/','')
			path_plus_file = path_plus_file.rstrip('\r\n')
			transcode.start_transcode(path_plus_file,PIPELINEID, REGION)
	child.close()
	
else:
	print "unable to resolve pipeline id with target ",TARGET

