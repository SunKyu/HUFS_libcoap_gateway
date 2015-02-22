import subprocess, os
import sys

arg = ["-m", "get" ,"-o", "result.txt","coap://[aaa::0212:7400:15d5:a731]/sensors?addr=8003,type=all"]
pathname = os.path.dirname(sys.argv[0])
path = os.path.abspath(pathname)
path = path + "/coap-client"
print path
>>>>>>> e45f03ed49db12b808a6ad8b50084c8b6ac187b1

p = subprocess.Popen([path]+ arg)
p.wait()
print "End of Execution"
