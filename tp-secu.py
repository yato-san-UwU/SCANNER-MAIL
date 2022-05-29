import imaplib                               
import email 
from email.header import decode_header 
import webbrowser 
import os 
import re
import vt


server ="imap.gmail.com"                     
imap = imaplib.IMAP4_SSL(server) 
  
username = input("entrer votre email :")
password =  input("entre votre mdp :")
imap.login(username, password)

res, messages = imap.select('Inbox')    
messages = int(messages[0])   
n = 1
  
for i in range(messages, messages - n, -1): 
    res, msg = imap.fetch(str(i), "(RFC822)")      
    for response in msg: 
        if isinstance(response, tuple): 
            msg = email.message_from_bytes(response[1]) 
            From = msg["From"]  
            subject = msg["Subject"]  
            content = msg["Content"]
            
            print("From : ", From) 
            print("subject : ", subject) 
            print (f"Content : ")
            for part in msg.walk():
                if part.get_content_type() == "text/html":
                    print(part)
                    #print(part.as_string())
    print("-----------------------------------------------------------------------------")

imap.close()

email = str(part)
regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
match = re.findall(regex, email)

for url in match:
    print(url)

key = '49fae1b1118da71be726fc10380dba8c231f98ab16fdef0d757df61dd6e0e96b'
client = vt.Client(key)

analysis = client.scan_url(url)
analysis.to_dict()


#clientV2 =client.get_object(f'/analyses/{analysis.id}')
clientV2 =client.get_object("/analyses/{}", analysis.id)
print(clientV2.to_dict())


print("--------------------------------------------")