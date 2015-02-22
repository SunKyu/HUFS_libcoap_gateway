import subprocess, os
import sys

i = 3
f = open("table.txt",'r')
cycle =10
while i: 
  line = f.readline()
  if not line:
    f.seek(0)
    print "cycle time is %d" %cycle
    sleep(cycle)
    continue
  linetable = line.split('/')
  url = "coap://[%s]/sensors?addr=%s,type=%s" %(linetable[1], linetable[3], linetable[3]
  arg = ["-m", "get" ,"-o", "result.txt","-B","3", url]
  pathname = os.path.dirname(sys.argv[0])
  path = os.path.abspath(pathname)
  path = path + "/coap-client"
  print path

  p = subprocess.Popen([path]+ arg)
  p.wait()
  print "End of Execution"
  i = i-1
