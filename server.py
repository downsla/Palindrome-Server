'''
Created on 4 Nov 2021

@author: Liam
'''
import socket
import select
import queue
import sys

#input validation
if len(sys.argv) != 3:
    print('must input: host port')
    sys.exit(1)

#setup socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

#input validation
try:
    print('starting up on (\'%s\', %s)' %(sys.argv[1], sys.argv[2]))
    server.bind((sys.argv[1], int(sys.argv[2])))
except:
    print('invalid host/port')
    sys.exit(1)
    
server.listen()

inputs = [server]
outputs = []
msg_qs = {}

#loop
while inputs:
    print('\nwaiting for client')
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    
    #sockets to read
    for socket in readable:
        if socket is server:
            connection, client_address = socket.accept()
            print('new connection from', client_address)
            connection.setblocking(0)
            inputs.append(connection)
            msg_qs[connection] = queue.Queue()
        else:
            data = str(socket.recv(1024))[2:-1].replace(' ', '')
            
            #check if data
            if data:
                print('received \'%s\' from %s' %(data, socket.getpeername()))
                msg_qs[socket].put(data)
                
                if socket not in outputs:
                    outputs.append(socket)
            else:
                print('closing', client_address)
                
                if socket in outputs:
                    outputs.remove(socket)
                    
                inputs.remove(socket)
                socket.close()
                del msg_qs[socket]
    
    #sockets to write            
    for socket in writable:
        try:
            next_msg = msg_qs[socket].get_nowait()
        except queue.Empty:
            print('output queue for', socket.getpeername(), 'is empty')
            outputs.remove(socket)
        else:
            print('sending \'%s\' to %s' %(data, socket.getpeername()))
            backward = data[::-1]
            
            #check if palindrome
            if data.casefold() == backward.casefold():
                socket.send(b'true')
            else :
                socket.send(b'false')
                
    #socket exceptions
    for socket in exceptional:
        inputs.remove(socket)
        
        if socket in outputs:
            outputs.remove(socket)
            
        socket.close()
        del msg_qs[socket]
