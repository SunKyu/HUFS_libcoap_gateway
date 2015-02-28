#HUFS_libcoap_gateway 
-----
use client code, then make gateway (HTTP post and coap get)

=======
##Installation
```
$ sudo apt-get update  
$ sudo apt-get install libcurl4-openssl-dev   
$ sudo ./configure  
$ sudo make  
```

##Run the Porogram 
```
$ cd examples  
$ sudo python code.py [cycle time] [BAS_IP]   
# ex) sudo python code.py 30   
# The program send value to BAS every 30 seconds  
```

##Add the Daemon to `/etc/init.d`
```
$ cd examples  
$ sudo cp code.sh /etc/init.d/  
$ sudo sudo update-rc.d code.sh defaults  
```
    
**you must change line 19 of `code.sh`** depnding on file's path 
and then `sudo reboot` or `sudo service code.sh start`  
`ps aux | grep code`

##issue  
1. if you want coap-clinet's argument    
you should change the `examples/code.py` that script has argumnet    
  
2. if you need change the number of argumnet of copa-client, `client.c` main funciton shoud be modify   
  
3. when you need to change **tag_id**, **coap_address** and **sensor_type**, you shoud modify table.txt
  
4. The BAS Server **can't** receive the data of Seonsor's **location** type 

