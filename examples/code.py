import subprocess, os
import sys

arg = "-m get -o result.txt coap://[aaa::0212:7400:15d5:a731]/sensors?addr=8003,type=all"
pathname = os.path.dirname(sys.argv[0])
path = os.path.abspath(pathname)
path = path + "/coap-client"
print path

p = subprocess.Popen([path, arg ])

print "End of Execution"
