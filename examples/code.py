import subprocess, os

PIPE = subprocess.PIPE
arg = "-m get -o result.txt coap://[aaa::0212:7400:15d5:a731]/sensors?addr=8003,type=all"
p = subprocess.Popen(["/Users/leesunkyu/Dropbox/Soucecode/2015-1/HUFS_libcoap_gateway/examples/coap-client", arg ], stdin=PIPE, stdout=PIPE)

p.stdin.write("10")
p.stdin.flush()
print p.stdout.read() #Deadlock
print "End of Execution"
os.system("PAUSE")
