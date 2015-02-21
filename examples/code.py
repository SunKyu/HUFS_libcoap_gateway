import subprocess, os

PIPE = subprocess.PIPE
p = subprocess.Popen("/Users/leesunkyu/Dropbox/Soucecode/2015-1/test/hello", stdin=PIPE, stdout=PIPE)

p.stdin.write("10")
p.stdin.flush()
print p.stdout.read() #Deadlock
print "End of Execution"
os.system("PAUSE")
