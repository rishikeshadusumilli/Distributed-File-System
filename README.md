# Distributed-File-System
DFS (Distributed File System) using python3.5 to handle multiple requests and response between web-server and client.

Requirements:
1.	Web-server and client implementation requires python3.5 for scripting
2.	Server must handle only GET, PUT, LIST, and EXIT request methods.
3.	Client should be able to successfully transfer files from client location to server location.
4.	File transferred from client should be split into 4 parts and each part should be individually stored in 4 different servers.
5.	Redundant copies of the same part of file should be stored in different servers so to avoid data loss in the event of server failure.
6.	Client will request contents of server using LIST command and server will respond accordingly.
7.	Client will request back files stored on server using GET command and server should send individual parts back to the client.
8.	Client should be able to distinguish if original file can be reconstructed using list command.
9.	Server will store file in individual folders according to user name specified.
10.	We must be able to kill server by sending a keyboard interrupt.

How to start:
1.	Start client using python3.5 dfs.py dfc.conf
2.	Start different 4 servers using python3.5 server.py /DFS1
3.	Select different command from PUT, GET, LIST and EXIT from the menu displayed on the client to perform various operations.

Functionalities Implemented:
1.	PUT - Client will request storage of files on the different servers using PUT command.
2.	GET - Client will request files stored on different servers using GET command.
3.	LIST - Client will request contents of different servers using LIST command.
4.	EXIT - Client will request exiting the client program.

Procedure:
1.	When the client program is ran, client will be given various command options like PUT, GET, LIST and EXIT.
2.	Client will select the required command as required. 
3.	Client will select PUT command if client wishes to store files on the different servers. When client selects command and file name, file will be selected from client directory and split into 4 equal parts. 
4.	File after being split into 4 equal parts will be sent to different servers using hashing. 
5.	After successful storage of files on the different directories, client will again be displayed menu with different commands.
6.	If client selects LIST command, servers will display all the files present in different locations and so client can select the file required.
7.	Client will verify if file parts received are sufficient to reconstruct the original file, if yes then client will display the file name and part else client will display Incomplete against that particular file.
8.	After successfully receiving all parts of file, client will write the files onto client client directory as received.
9.	After completion of GET command, client will again be displayed menu for selecting different options.
10.	Client can exit the client program using EXIT command.
11.	Server will always be running.
