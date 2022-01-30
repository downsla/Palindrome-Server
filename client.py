'''
Created on 4 Nov 2021

@author: Liam
'''

import socket
import sys

#input validation
if len(sys.argv) != 4:
    print('must input: host port filename')
    sys.exit(1)
    
try:
    file = open(sys.argv[3], "r")
except:
    print('invalid filename')
    sys.exit(1)

#setup socket    
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#input validation    
try:
    print('connecting to (\'%s\', %s)' %(sys.argv[1], sys.argv[2]))
    client.connect((sys.argv[1], int(sys.argv[2])))
except:
    print('invalid host/port')
    sys.exit(1)

#open output file
output = open(sys.argv[3].split('.', 1)[0] + 'output.dat', "w")

#loop            
while (line := file.readline().rstrip()):
    #send line
    print('\n%s sending \'%s\' from %s' %(client.getsockname(), line, sys.argv[3]))
    client.sendall(bytes(line, 'utf-8'))
    
    #receive line
    data = str(client.recv(1024))[2:-1]
    print(client.getsockname(), 'received')
    print('%s writing to %s' %(client.getsockname(), output.name))
    
    #write results        
    if data == 'true':
        output.write(line + ' is a palindrome\n')
    else:
        output.write(line + ' is not a palindrome\n')
    
    if not data:
        print('closing', client.getsockname())
        client.close()

