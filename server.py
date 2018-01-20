import socket, sys, os, traceback, threading

###########################Get Function##########################
def getOption(location, userName, request, fileMsg1, delim, newLine):
    fileMsg=[]
    fileName=request.split(delim)[2].rstrip(newLine).decode()

    for files in os.listdir(os.path.abspath("."+location+"/"+userName+"/")):
        if(fileName==(files.split(".")[0]+"."+files.split(".")[1])):
            fh=open(os.path.abspath("."+location+"/"+userName+"/"+files), 'rb')
            part=fh.read()
            DFS=("*?!!?*GET*?!!?*"+files+"*?!!?* *?!!?*").encode()+part+("*?!!?* *?!!?*").encode()
            fileMsg.append(DFS)
        
    if(len(fileMsg)==0):
        fileMsg1="Error*?!!?*File part not present in server...".encode()
        return fileMsg1
    else:
        delim1="$$##$$".encode()
        fileMsg1=delim1.join(fileMsg)
        return fileMsg1

############################List##################################
def listOption(statusMsg1, location, userName):
    statusMsg=[]
    for files in os.listdir(os.path.abspath("."+location+"/"+userName+"/")):
        statusMsg.append(files)
    statusMsg1="\n".join(statusMsg)
    return statusMsg1

############################Put Receive############################
def putReceive(request, portInfo1, userName, location, delim):
    currentDir=".".encode()
    part="part".encode()
    fileName=request.split(delim)[2].split(currentDir)[0].decode()
    extension=request.split(delim)[2].split(currentDir)[1].decode()
    part1=request.split(delim)[3].split(part)[1].decode()
    filePart1=request.split(delim)[4]
    part2=request.split(delim)[5].split(part)[1].decode()
    filePart2=request.split(delim)[6]
    if not os.path.exists("."+location+"/"+userName):
        os.makedirs("."+location+"/"+userName)
        filePath1=os.path.abspath("."+location+"/"+userName+"/"+fileName+"."+extension+"."+part1)
        filePath2=os.path.abspath("."+location+"/"+userName+"/"+fileName+"."+extension+"."+part2)
        fh1=open(filePath1, "wb")
        fh2=open(filePath2, "wb")
        fh1.write(filePart1)
        fh1.close()
        fh2.write(filePart2)
        fh2.close()

    else:
        filePath1=os.path.abspath("."+location+"/"+userName+"/"+fileName+"."+extension+"."+part1)
        filePath2=os.path.abspath("."+location+"/"+userName+"/"+fileName+"."+extension+"."+part2)
        fh1=open(filePath1, "wb")
        fh2=open(filePath2, "wb")
        fh1.write(filePart1)
        fh1.close()
        fh2.write(filePart2)
        fh2.close()

###################################User Process####################

def userProcess(cconn, auth, location, statusMsg1, portInfo1, fileMsg1):
    while 1:
        print("Waiting to receive initially...")
        request=cconn.recv(102400)
        try:
            while request:
                print("waiting to receive additionally")
                cconn.settimeout(1)
                request+=cconn.recv(102400)
        except socket.timeout:
            print("Received request from server------>")
            cconn.settimeout(None)
        
        if request:
            #decodedRequest=request.decode()
            print("Request received from "+str(caddr[1]))
            fs=open("sdfc.conf")
            delim="*?!!?*".encode()
            newLine="\n".encode()
            fileName=request.split(delim)[1].decode()
            userName=request.split(delim)[7].rstrip(newLine).decode()
            print("userName---->",userName)
            passWord=request.split(delim)[8].rstrip(newLine).decode()
            print("passWord---->", passWord)
            for lines in fs.readlines():
                print("username---->",lines.split()[0])
                print("password---->",lines.split()[1])
                if(userName==lines.split()[0]):
                    if(passWord==lines.split()[1]):
                        auth="yes"
                        print("username and password valid")
                        break
                    else:
                        print("password invalid")
                        auth="no"
                else:
                    print("username invalid")
                    auth="no"
        
            if((fileName=="PUT") and (auth=="yes")):
                mesg="PUT command processing and authentication success..."
                cconn.sendall(mesg.encode())
                putReceive(request, portInfo1, userName, location, delim)
            elif((fileName=="LIST") and (auth=="yes")):
                listContents=listOption(statusMsg1, location, userName)
                cconn.sendall(listContents.encode())
            elif((fileName=="GET") and (auth=="yes")):
                fileMsgString=getOption(location, userName, request, fileMsg1, delim, newLine)
                cconn.sendall(fileMsgString)
            else:
                error="Command not recognized or Invalid Username/Password.  Please  try again."
                cconn.sendall(error.encode())

        else:
            print("##################Blank Request Receiv     ed#######################")
            break
    
    s.close()
    cconn.close()

############################Command Arguments#######################
def progInputs():
    if(len(sys.argv)!=3):
        print("Enter port information for server to start!!!")
        quit()
    else:
        return sys.argv[1], sys.argv[2]

############################MAIN FUNCTION###########################

if __name__ == '__main__':                                                      #Main function
    statusMsg1=""
    fileMsg1=""
    serverUsername=""
    serverPassword=""
    auth=""
    hostInfo=""
    location, portInfo1=progInputs()
    portInfo=int(portInfo1)
    while 1:
        if(portInfo>1024):
        
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((hostInfo, portInfo))
            s.listen(10)
            print("Waiting to accept connection...")
            cconn, caddr=s.accept()
            try:
    
                thread1=threading.Thread(target=userProcess, args=(cconn, auth, location, statusMsg1, portInfo1, fileMsg1, ))
                thread1.start()

            except KeyboardInterrupt:
                s.close()
                print("\nProxy server is exitting upon request of administrator, thank you running me !!!")
                quit()

            except Exception as e:
                s.close()
                print(traceback.format_exc())
    
        else:
            print("Enter only port numbers greater than 1024")
            quit()



