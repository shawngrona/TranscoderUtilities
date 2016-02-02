
import pexpect
import transcode
from pipelineresolver import PipelineResolver
import sys 
from sys import stdin

SOURCE = ""
TARGET = ""
PIPELINEID = ""
REGION=""
BUCKET=""

def isValidForTranscode(path):
	if '.mts' in path:
		return True
	else:
		return False


### entry point

print "This script will insert transcode jobs for all files recursively beneath a bucket and path"
print ""
print "Please enter the target bucket with path (ie <bucket>/<path>"
TARGET = stdin.readline().rstrip('\n')

pr = PipelineResolver(TARGET.split('/')[0])

PIPELINEID = pr.getPipelineId()
REGION = pr.getRegion()
BUCKET = pr.getBucket()

if PIPELINEID != None:
	print "resolved pipelineid:"+PIPELINEID+"\n"
	print "resolved region:"+REGION+"\n"
	
	command = 's4cmd ls s3://'+TARGET+'/ -r'
	print "running command ",command
	
	child = pexpect.spawn(command, timeout=None) #do not time out
	for line in child:
		print line
		if isValidForTranscode(line):
			path_plus_file = line.split(' ')[3].replace(' ','')
			path_plus_file = path_plus_file.replace('s3://'+BUCKET+'/','')
			path_plus_file = path_plus_file.rstrip('\r\n')
			transcode.start_transcode(path_plus_file,PIPELINEID, REGION)
	child.close()
	
else:
	print "unable to resolve pipeline id with target ",TARGET

