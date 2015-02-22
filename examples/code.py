import subprocess, os

PIPE = subprocess.PIPE
p = subprocess.Popen("/opt/CoAP_BAS/HUFS_libcoap_gateway/examples/coap-client -m get -o result.txt -B 5 coap://[localhost]/sensors?addr=8003,type=all", stdin=PIPE, stdout=PIPE)

p.stdin.write("10")
p.stdin.flush()
print p.stdout.read() #Deadlock
print "End of Execution"
os.system("PAUSE")
