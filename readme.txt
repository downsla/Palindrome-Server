run the server (server.py) with the following command arguments:
host port
example: python server.py 192.168.0.1 8080

run the client (client.py) with the following command arguments:
host port filepath
example: python client.py 192.168.0.1 8080 client1.dat

There are two included client files (client1.dat, client2.dat).
Both the server and client output to the console what they are doing.
There will be an output file placed in the same location as the client file named *filename*output.dat showing the results.
The server accepts multiple clients running simultaneously.