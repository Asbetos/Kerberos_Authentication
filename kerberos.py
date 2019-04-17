import random, string
import time


public_keys={'Kca':4,'Kct':5,'Kcs':6}
public_repo={1:'alpha',2:'beta',3:'charlie',4:'delta',5:'epsilon',}

class client:
    def __init__(self,id,passwd,server_id):
        self.id=id
        self.password=passwd
        self.server_id=server_id
        


class KeyDistro:
  

    def __init__(self,id,passwd,server_id):
        self.client=client(id,passwd,server_id)

    def authenticate(self,client):
        if client.id in public_repo:
            if(client.password==public_repo[self.client.id]):
                print("Client Authenticated!")
                print()
                print('Generating ticket granting ticket')
                client.TGT=gen_TGT(client,auth=True)
                self.temp_TGT=client.TGT
                self.auth=True
                print("Generated TGT for client:",client.id,'\n',self.temp_TGT)
            else:
                print("Client's password is incorrect\nEXITING...",)
                exit(0)

    def ticket_granting(self,client):
        if hasattr(client,'TGT') and self.auth:
            if client.TGT==self.temp_TGT:
                 print("Client has been granted the keys to communicate with the server:",client.server_id)
                 print()
                 client.server_key=public_repo[client.server_id]


            




        
def gen_TGT(client,auth=False):
    if(auth):
        x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        return(x)




class server:
    def __init__(self,id=1):
        self.id=id
    
    def connect(self,client,KeyDistro):
        if hasattr(client,'server_key'):
            if client.server_key==public_repo[server_id]:
                print("Connection established with server")



id=int(input("Enter your client id"))
passwd=input("Enter the password for client: ")
server_id=int(input("Enter the server id to communicate"))

cl1=client(id,passwd,server_id)

print("Initiating communication with key distribution centre...")
print()
time.sleep(2)
keydist1=KeyDistro(id,passwd,server_id)

print("Requesting for the TGT....")
print()
time.sleep(2)
keydist1.authenticate(cl1)

print("Initiating communication with the Ticket granting Server....")
print()
time.sleep(2)
keydist1.ticket_granting(cl1)


print("Connecting to the server...")
print()
time.sleep(2)


serv1=server(server_id)
serv1.connect(cl1,keydist1)
