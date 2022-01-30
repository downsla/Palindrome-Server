# Palindrome-Server
CPSC 4317 Computer Networks - Python Concurrent Palindrome Server 11/10/2021

Create a client - server program using TCP/IP socket programming in the Python language that will satisfy the following requirements:  
1. Clients must input arrays of strings of ASCII characters from a file in the client process and send them to the server process on the host using the TCP/IP protocols and sockets implemented in the Python language. The server checks whether the string is a palindrome and returns the string with an answer of "YES" or "No". The client and the server must be on separate processes.
2. The server should be able to handle multiple connections from many clients concurrently 2using the select() command.  In other words, the server will not block every time one request arrives and satisfy that request before going to the next one.  Instead, it will ask the operating system through select to receive the requests asynchronously.  Also, the server must use the accept() system call in order to process multiple requests concurrently.
