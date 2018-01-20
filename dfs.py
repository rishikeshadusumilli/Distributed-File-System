import socket, os, sys, traceback, hashlib, base64


################################Other Commands####################
def otherC(COMMAND):
    print("Command not recognized, please select between, PUT, GET, LIST and EXIT")
            
###############################Get Function########################
def getFi(COMMAND, fileI):
    part1=""
    part2=""
    part3=""
    part4=""
    delim1="*?!!?*".encode()
    delim2="$$##$$".encode()
    currentDir=".".encode()
    command1=COMMAND.upper()
    commandSend=("*?!!?*"+command1+"*?!!?*"+fileI+"*?!!?* *?!!?* *?!!?* *?!!?* *?!!?*"+userName+"*?!!?*"+passWord).encode()
    try:
        s1.sendall(commandSend)
        mesg1=s1.recv(102400000)
        if(mesg1.split(delim1)[0].decode()=="Error"):
            print(mesg1.split(delim1)[1].decode())
        else:
            for lines in mesg1.split(delim2):
                if(lines.split(delim1)[2].split(currentDir)[2].decode()=="1"):
                    part1=lines.split(delim1)[4]
                elif(lines.split(delim1)[2].split(currentDir)[2].decode()=="2"):
                    part2=lines.split(delim1)[4]
                elif(lines.split(delim1)[2].split(currentDir)[2].decode()=="3"):
                    part3=lines.split(delim1)[4]
                elif(lines.split(delim1)[2].split(currentDir)[2].decode()=="4"):
                    part4=lines.split(delim1)[4]
    except Exception as e:
        #print(traceback.format_exc())
        print("****DFS1 is down****")

    try:
        s2.sendall(commandSend)
        mesg2=s2.recv(102400000)
        if(mesg2.split(delim1)[0].decode()=="Error"):
            print(mesg2.split(delim1)[1].decode())
        else:
            for lines in mesg2.split(delim2):
                if(lines.split(delim1)[2].split(currentDir)[2].decode()=="1"):
                    part1=lines.split(delim1)[4]
                elif(lines.split(delim1)[2].split(currentDir)[2].decode()=="2"):
                    part2=lines.split(delim1)[4]
                elif(lines.split(delim1)[2].split(currentDir)[2].decode()=="3"):
                    part3=lines.split(delim1)[4]
                elif(lines.split(delim1)[2].split(currentDir)[2].decode()=="4"):
                    part4=lines.split(delim1)[4]
    except Exception as e:
        #print(traceback.format_exc())
        print("****DFS2 is down****")

    try:
        s3.sendall(commandSend)
        mesg3=s3.recv(102400000)
        if(mesg3.split(delim1)[0].decode()=="Error"):
            print(mesg3.split(delim1)[1].decode())
        else:
            for lines in mesg3.split(delim2):
                if(lines.split(delim1)[2].split(currentDir)[2].decode()=="1"):
                    part1=lines.split(delim1)[4]
                elif(lines.split(delim1)[2].split(currentDir)[2].decode()=="2"):
                    part2=lines.split(delim1)[4]
                elif(lines.split(delim1)[2].split(currentDir)[2].decode()=="3"):
                    part3=lines.split(delim1)[4]
                elif(lines.split(delim1)[2].split(currentDir)[2].decode()=="4"):
                    part4=lines.split(delim1)[4]
    except Exception as e:
        #print(traceback.format_exc())
        print("****DFS3 is down****")


    try:
        s4.sendall(commandSend)
        mesg4=s4.recv(102400000)
        if(mesg4.split(delim1)[0].decode()=="Error"):
            print(mesg4.split(delim1)[1].decode())
        else:
            for lines in mesg4.split(delim2):
                if(lines.split(delim1)[2].split(currentDir)[2].decode()=="1"):
                    part1=lines.split(delim1)[4]
                elif(lines.split(delim1)[2].split(currentDir)[2].decode()=="2"):
                    part2=lines.split(delim1)[4]
                elif(lines.split(delim1)[2].split(currentDir)[2].decode()=="3"):
                    part3=lines.split(delim1)[4]
                elif(lines.split(delim1)[2].split(currentDir)[2].decode()=="4"):
                    part4=lines.split(delim1)[4]
    except Exception as e:
        #print(traceback.format_exc())
        print("****DFS4 is down****")

    try:
        fileO=fileI.split(".")[0]
        if((len(part1)==0)or(len(part2)==0)or(len(part3)==0)or(len(part4)==0)):
            print("File is incomplete...")
            return
        else:
            fw=open(fileO+"_received."+fileI.split(".")[1], "wb")
            writeFile=[part1, part2, part3, part4]
            for files in writeFile:
                fw.write(files)
    
            fw.close()
    except Exception as e:
        #print(traceback.format_exc())
        print("Get writing file...")

###############################Exit Function########################
def exitOption():
    sys.exit()

#################################List Function######################
def listOption(COMMAND, userName, passWord):
    part1=""
    part2=""
    part3=""
    part4=""
    fileCheck={}
    files=[]
    command1=COMMAND.upper()
    commandSend=("*?!!?*"+command1+"*?!!?* *?!!?* *?!!?* *?!!?* *?!!?* *?!!?*"+userName+"*?!!?*"+passWord).encode()
    try:
        s1.sendall(commandSend)
        mesg1=s1.recv(102400)
        for lines in mesg1.decode().splitlines():
            fileName=lines.split(".")[0]+"."+lines.split(".")[1]
            if(fileName not in files):
                files.append(fileName)
            if(lines.split(".")[2]==1):
                fileCheck[fileName+".part1"]="1"
            elif(lines.split(".")[2]==2):
                fileCheck[fileName+".part2"]="2"
            elif(lines.split(".")[2]==3):
                fileCheck[fileName+".part3"]="3"
            elif(lines.split(".")[2]==4):
                fileCheck[fileName+".part4"]="4"
    except Exception as e:
        #print(traceback.format_exc())
        print("****DFS1 is down****")

    try:
        s2.sendall(commandSend)
        mesg2=s2.recv(102400)
        for lines in mesg2.decode().splitlines():
            fileName=lines.split(".")[0]+"."+lines.split(".")[1]
            if(fileName not in files):
                files.append(fileName)
            if(lines.split(".")[2]=="1"):
                fileCheck[fileName+".part1"]="1"
            elif(lines.split(".")[2]=="2"):
                fileCheck[fileName+".part2"]="2"
            elif(lines.split(".")[2]=="3"):
                fileCheck[fileName+".part3"]="3"
            elif(lines.split(".")[2]=="4"):
                fileCheck[fileName+".part4"]="4"
    except Exception as e:
        #print(traceback.format_exc())
        print("****DFS2 is down****")
    
    try:
        s3.sendall(commandSend)
        mesg3=s3.recv(102400)
        for lines in mesg3.decode().splitlines():
            fileName=lines.split(".")[0]+"."+lines.split(".")[1]
            if(fileName not in files):
                files.append(fileName)
            if(lines.split(".")[2]=="1"):
                fileCheck[fileName+".part1"]="1"
            elif(lines.split(".")[2]=="2"):
                fileCheck[fileName+".part2"]="2"
            elif(lines.split(".")[2]=="3"):
                fileCheck[fileName+".part3"]="3"
            elif(lines.split(".")[2]=="4"):
                fileCheck[fileName+".part4"]="4"
    except Exception as e:
        #print(traceback.format_exc())
        print("****DFS3 is down****")

    try:
        s4.sendall(commandSend)
        mesg4=s4.recv(102400)
        for lines in mesg4.decode().splitlines():
            fileName=lines.split(".")[0]+"."+lines.split(".")[1]
            if(fileName not in files):
                files.append(fileName)
            if(lines.split(".")[2]=="1"):
                fileCheck[fileName+".part1"]="1"
            elif(lines.split(".")[2]=="2"):
                fileCheck[fileName+".part2"]="2"
            elif(lines.split(".")[2]=="3"):
                fileCheck[fileName+".part3"]="3"
            elif(lines.split(".")[2]=="4"):
                fileCheck[fileName+".part4"]="4"
    except Exception as e:
        #print(traceback.format_exc())
        print("****DFS4 is down****")

    print("*************LIST**************")
    
    for values in files:
        print("-----------------------------")
        try:
            if(fileCheck[values+".part1"]=="1"):
                print(values+".part1")
        except:
            print(values+".part1 [Incomplete]")

        try:
            if(fileCheck[values+".part2"]=="2"):
                print(values+".part1")
        except:
            print(values+".part2 [Incomplete]")

        try:
            if(fileCheck[values+".part3"]=="3"):
                print(values+".part3")
        except:
            print(values+".part3 [Incomplete]")

        try:
            if(fileCheck[values+".part4"]=="4"):
                print(values+".part4")
        except:
            print(values+".part4 [Incomplete]")

        print("-----------------------------")

    print("*******************************")

#################################Hashing Function##################
def hashing(fname):
    fileHash=hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            fileHash.update(chunk)
    return fileHash.hexdigest()

#################################Put Function######################
def putFile(COMMAND, fileI, s1, s2, s3, s4, userName, passWord):

    #s1.settimeout(2)
    #s2.settimeout(2)
    #s3.settimeout(2)
    #s4.settimeout(2)
    part1=""
    part2=""
    part3=""
    part4=""
    if(os.path.isfile(fileI)):
        fh=open(fileI, 'rb')
        fSize=os.stat(fileI).st_size
        print("Total file size---->",fSize)
        filePart1=fSize/4
        filePart=int(filePart1)
        filePart4=fSize-filePart*3
        part1=fh.read(filePart)
        part2=fh.read(filePart)
        part3=fh.read(filePart)
        part4=fh.read(filePart4)

        fileHash=hashing(fileI)
        xValue1=int(fileHash, 16)
        xValue=xValue1%4
        print("xValue---->",xValue)
        
        if(xValue==0):
            DFS1=("*?!!?*PUT*?!!?*"+fileI+"*?!!?*part1*?!!?*").encode()+part1+("*?!!?*part2*?!!?*").encode()+part2+("*?!!?*"+userName+"*?!!?*"+passWord).encode()
            DFS2=("*?!!?*PUT*?!!?*"+fileI+"*?!!?*part2*?!!?*").encode()+part2+("*?!!?*part3*?!!?*").encode()+part3+("*?!!?*"+userName+"*?!!?*"+passWord).encode()
            DFS3=("*?!!?*PUT*?!!?*"+fileI+"*?!!?*part3*?!!?*").encode()+part3+("*?!!?*part4*?!!?*").encode()+part4+("*?!!?*"+userName+"*?!!?*"+passWord).encode()
            DFS4=("*?!!?*PUT*?!!?*"+fileI+"*?!!?*part4*?!!?*").encode()+part4+("*?!!?*part1*?!!?*").encode()+part1+("*?!!?*"+userName+"*?!!?*"+passWord).encode()
            
            try:
                s1.sendall(DFS1)
            except:
                print("DFS1 is not available")
            try:
                s2.sendall(DFS2)
            except:
                print("DFS2 is not available") 
            try:
                s3.sendall(DFS3)
            except:
                print("DFS3 is not available") 
            try:
                s4.sendall(DFS4)
            except:
                print("DFS4 is not available") 
            
            try:
                mesg1=s1.recv(102400)
                print("s1 message---->",mesg1.decode())
            except socket.timeout:
                print("No connection to DFS1")
            except:
                print("DFS1 timed-out")
            try:
                mesg2=s2.recv(102400)
                print("s2 message---->",mesg2.decode())
            except socket.timeout:
                print("No connection to DFS2")
            except:                                 
                print("DFS2 timed-out")
            try:
                mesg3=s3.recv(102400)
                print("s3 message---->",mesg3.decode())
            except socket.timeout:
                print("No connection to DFS3")
            except:                                 
                print("DFS3 timed-out")
            try:
                mesg4=s4.recv(102400)
                print("s4 message---->",mesg4.decode())
            except socket.timeout:
                print("No connection to DFS4")
            except:
                print("DFS4 timed-out")

        elif(xValue==1):
            DFS1=("*?!!?*PUT*?!!?*"+fileI+"*?!!?*part4*?!!?*").encode()+part4+("*?!!?*part1*?!!?*").encode()+part1+("*?!!?*"+userName+"*?!!?*"+passWord).encode()
            DFS2=("*?!!?*PUT*?!!?*"+fileI+"*?!!?*part1*?!!?*").encode()+part1+("*?!!?*part2*?!!?*").encode()+part2+("*?!!?*"+userName+"*?!!?*"+passWord).encode()
            DFS3=("*?!!?*PUT*?!!?*"+fileI+"*?!!?*part2*?!!?*").encode()+part2+("*?!!?*part3*?!!?*").encode()+part3+("*?!!?*"+userName+"*?!!?*"+passWord).encode()
            DFS4=("*?!!?*PUT*?!!?*"+fileI+"*?!!?*part3*?!!?*").encode()+part3+("*?!!?*part4*?!!?*").encode()+part4+("*?!!?*"+userName+"*?!!?*"+passWord).encode()
            
            try:
                s1.sendall(DFS1)
            except:
                print("DFS1 is not available")
            try:
                s2.sendall(DFS2)
            except:
                print("DFS2 is not available") 
            try:
                s3.sendall(DFS3)
            except:
                print("DFS3 is not available") 
            try:
                s4.sendall(DFS4)
            except:
                print("DFS4 is not available") 
            
            try:
                mesg1=s1.recv(102400)
                print("s1 message---->",mesg1.decode())
            except socket.timeout:
                print("No connection to DFS1")
            except:                                 
                print("DFS1 timed-out")
            try:
                mesg2=s2.recv(102400)
                print("s2 message---->",mesg2.decode())
            except socket.timeout:
                print("No connection to DFS2")
            except:                                 
                print("DFS2 timed-out")
            try:
                mesg3=s3.recv(102400)
                print("s3 message---->",mesg3.decode())
            except socket.timeout:
                print("No connection to DFS3")
            except:                                 
                print("DFS3 timed-out")
            try:
                mesg4=s4.recv(102400)
                print("s4 message---->",mesg4.decode())
            except socket.timeout:
                print("No connection to DFS4")
            except:                                 
                print("DFS4 timed-out")

        elif(xValue==2):
            DFS1=("*?!!?*PUT*?!!?*"+fileI+"*?!!?*part3*?!!?*").encode()+part3+("*?!!?*part4*?!!?*").encode()+part4+("*?!!?*"+userName+"*?!!?*"+passWord).encode()
            DFS2=("*?!!?*PUT*?!!?*"+fileI+"*?!!?*part4*?!!?*").encode()+part4+("*?!!?*part1*?!!?*").encode()+part1+("*?!!?*"+userName+"*?!!?*"+passWord).encode()
            DFS3=("*?!!?*PUT*?!!?*"+fileI+"*?!!?*part1*?!!?*").encode()+part1+("*?!!?*part2*?!!?*").encode()+part2+("*?!!?*"+userName+"*?!!?*"+passWord).encode()
            DFS4=("*?!!?*PUT*?!!?*"+fileI+"*?!!?*part2*?!!?*").encode()+part2+("*?!!?*part3*?!!?*").encode()+part3+("*?!!?*"+userName+"*?!!?*"+passWord).encode()
                        
            try:
                s1.sendall(DFS1)
            except:
                print("DFS1 is not available")
            try:
                s2.sendall(DFS2)
            except:
                print("DFS2 is not available") 
            try:
                s3.sendall(DFS3)
            except:
                print("DFS3 is not available") 
            try:
                s4.sendall(DFS4)
            except:
                print("DFS4 is not available") 
            
            try:
                mesg1=s1.recv(102400)
                print("s1 message---->",mesg1.decode())
            except socket.timeout:
                print("No connection to DFS1")
            except:                                 
                print("DFS1 timed-out")
            try:
                mesg2=s2.recv(102400)
                print("s2 message---->",mesg2.decode())
            except socket.timeout:
                print("No connection to DFS2")
            except:                                 
                print("DFS2 timed-out")
            try:
                mesg3=s3.recv(102400)
                print("s3 message---->",mesg3.decode())
            except socket.timeout:
                print("No connection to DFS3")
            except:                                 
                print("DFS3 timed-out")
            try:
                mesg4=s4.recv(102400)
                print("s4 message---->",mesg4.decode())
            except socket.timeout:
                print("No connection to DFS4")
            except:                                 
                print("DFS4 timed-out")

        elif(xValue==3):
            DFS1=("*?!!?*PUT*?!!?*"+fileI+"*?!!?*part2*?!!?*").encode()+part2+("*?!!?*part3*?!!?*").encode()+part3+("*?!!?*"+userName+"*?!!?*"+passWord).encode()
            DFS2=("*?!!?*PUT*?!!?*"+fileI+"*?!!?*part3*?!!?*").encode()+part3+("*?!!?*part4*?!!?*").encode()+part4+("*?!!?*"+userName+"*?!!?*"+passWord).encode()
            DFS3=("*?!!?*PUT*?!!?*"+fileI+"*?!!?*part4*?!!?*").encode()+part4+("*?!!?*part1*?!!?*").encode()+part1+("*?!!?*"+userName+"*?!!?*"+passWord).encode()
            DFS4=("*?!!?*PUT*?!!?*"+fileI+"*?!!?*part1*?!!?*").encode()+part1+("*?!!?*part2*?!!?*").encode()+part2+("*?!!?*"+userName+"*?!!?*"+passWord).encode()
            
            try:
                s1.sendall(DFS1)
            except:
                print("DFS1 is not available")
            try:
                s2.sendall(DFS2)
            except:
                print("DFS2 is not available") 
            try:
                s3.sendall(DFS3)
            except:
                print("DFS3 is not available") 
            try:
                s4.sendall(DFS4)
            except:
                print("DFS4 is not available") 
            
            try:
                mesg1=s1.recv(102400)
                print("s1 message---->",mesg1.decode())
            except socket.timeout:
                print("No connection to DFS1")
            except:                                 
                print("DFS1 timed-out")
            try:
                mesg2=s2.recv(102400)
                print("s2 message---->",mesg2.decode())
            except socket.timeout:
                print("No connection to DFS2")
            except:                                 
                print("DFS2 timed-out")
            try:
                mesg3=s3.recv(102400)
                print("s3 message---->",mesg3.decode())
            except socket.timeout:
                print("No connection to DFS3")
            except:                                 
                print("DFS3 timed-out")
            try:
                mesg4=s4.recv(102400)
                print("s4 message---->",mesg4.decode())
            except socket.timeout:
                print("No connection to DFS4")
            except:                                 
                print("DFS4 timed-out")
    
    else:
        print("file is not present")


###############################Server Connect#######################
def serverConnect(confFile, searchWord):
    portInfo=""
    userName=""
    passWord=""
    if(os.path.isfile(confFile)):
        fh=open(confFile)
        for lines in fh.readlines():
            if(searchWord in lines):
                portInfo=lines.split(":")[1] 
                return portInfo
            elif(searchWord in lines):
                userName=lines.split(":")[1]
                return userName
            elif(searchWord in lines):
                passWord=lines.split(":")[1]
                return passWord

    else:
        print("File is not found")

#######################################Start Program#################
def startProgram():
    if(len(sys.argv)==2):
        return sys.argv[1]
    else:
        print("Enter client file and configuration file, eg: python dfc dfc.conf")
        quit()


########################################CLient-Main##################
if __name__ == '__main__':

    confFile=startProgram()
    print("configuration file---->",confFile)

    userName=serverConnect(confFile, "Username")
    #print("username---->",userName)
    passWord=serverConnect(confFile, "Password")
    #print("password---->",passWord)

    ipInfo="127.0.0.1"

    portInfoFile=serverConnect(confFile, "DFS1")
    print("port1---->",portInfoFile)
    portInfo1=int(portInfoFile)

    portInfoFile=serverConnect(confFile, "DFS2")
    print("port2---->",portInfoFile)
    portInfo2=int(portInfoFile)

    portInfoFile=serverConnect(confFile, "DFS3")
    print("port3---->",portInfoFile)
    portInfo3=int(portInfoFile)
    
    portInfoFile=serverConnect(confFile, "DFS4")
    print("port4---->",portInfoFile)
    portInfo4=int(portInfoFile)
    
    try:
        s1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addr1=(ipInfo, portInfo1)
        s1.connect(server_addr1)
    except Exception as e:
        #print(traceback.format_exc())
        print("Failed to connect socket server 1")
    
    try:
        s2=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addr2=(ipInfo, portInfo2)
        s2.connect(server_addr2)
    except Exception as e:
        #print(traceback.format_exc())
        print("Failed to connect socket server 2")
        
    try:
        s3=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addr3=(ipInfo, portInfo3)
        s3.connect(server_addr3)
    except Exception as e:
        #print(traceback.format_exc())
        print("Failed to connect socket server 3")
        
    try:
        s4=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addr4=(ipInfo, portInfo4)
        s4.connect(server_addr4)
    except Exception as e:
        #print(traceback.format_exc())
        print("Failed to connect socket server 4")
        
    while(1):
        print("Please enter the command with spaces:\nThe options presented to the user are:\nget[file_name]\nput[file_name]\nlist\nexit")
        COMMAND1 = input("Input: ")
        COMMAND3 = COMMAND1.lower()
        if(COMMAND3=="list"):
            listOption(COMMAND3, userName, passWord)
        elif(COMMAND3=="exit"):
            print("Client is closing as requested")
            s1.close()
            s2.close()
            s3.close()
            s4.close()
            exitOption()
        elif(COMMAND3==""):
            otherC(COMMAND3)
        else:
            COMMAND2 = COMMAND3.split()
            COMMAND = COMMAND2[0]
            if(COMMAND=="put"):
                try:
                    if(COMMAND2[1] != ""):
                        fileI=COMMAND2[1]
                    else:
                        print("Enter proper filename")
                except:
                    print("Enter proper filename")
                putFile(COMMAND, fileI, s1, s2, s3, s4, userName, passWord)
            elif(COMMAND=="get"):
                try:
                    if(COMMAND2[1] != ""):
                        fileI=COMMAND2[1]
                    else:
                        print("Enter Proper filename")
                except:
                    print("Enter proper filename")
                getFi(COMMAND, fileI)
            else:
                otherC(COMMAND3)




