import subprocess, os
import sys

arg = ["-m", "get" ,"-o", "result.txt","-B","3","coap://[aaa::0212:7400:15d5:a731]/sensors?addr=8003,type=all"]
pathname = os.path.dirname(sys.argv[0])
path = os.path.abspath(pathname)
path = path + "/coap-client"
print path

p = subprocess.Popen([path]+ arg)
p.wait()
print "End of Execution"
