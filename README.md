#HUFS_libcoap_gateway 
-----
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
$ sudo python code.py [cycle time]  
# ex) sudo python code.py 30   
# The program send value to BAS every 30 seconds  
```
##issue  
1. if you want coap-clinet's argument    
you should change the `examples/code.py` that script has argumnet    
  
2. if you need change the number of argumnet of copa-client, `client.c` main funciton shoud be modify   
  
3. when you need to change **tag_id**, **coap_address** and **sensor_type**, you shoud modify table.txt
  

author SunKyu Lee
