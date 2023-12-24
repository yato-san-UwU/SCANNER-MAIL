import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import re
import vt
import urllib.parse
from bs4 import BeautifulSoup

def is_valid_url(url):
    try:
        # Utilisez urlparse pour analyser l'URL
        parsed_url = urllib.parse.urlparse(url)
        # Vérifiez si le schéma (par exemple, http ou https) et le netloc (par exemple, le nom de domaine) sont présents
        return all([parsed_url.scheme, parsed_url.netloc])
    except Exception:
        # En cas d'erreur lors de l'analyse de l'URL, considérez-la comme invalide
        return False

# Configuration de la connexion IMAP
server = "imap.gmail.com"
imap = imaplib.IMAP4_SSL(server)

username = input("Entrez votre email : ")
password = input("Entrez votre mot de passe : ")
imap.login(username, password)

# Demandez à l'utilisateur de choisir la boîte de réception
mailbox_name = input("Entrez le nom de la boîte de réception (par exemple, 'inbox', 'sent', etc.) : ")
res, messages = imap.select(mailbox_name)

# Vérifiez si la boîte de réception sélectionnée est valide
if res != 'OK':
    print("La boîte de réception spécifiée n'existe pas.")
else:
    # Demandez à l'utilisateur de choisir le numéro du message à analyser
    # Utilisez la méthode search pour obtenir les IDs des e-mails dans l'ordre inverse
    res, email_ids = imap.search(None, 'ALL')
    email_ids = email_ids[0].split()

    # Demandez à l'utilisateur de choisir le numéro du message à analyser
    message_number = input("Entrez le numéro du message à analyser (1 pour le plus récent) : ")

    try:
        # Obtenez l'ID de l'e-mail correspondant au numéro fourni par l'utilisateur
        selected_email_id = email_ids[-int(message_number)]
    
        # Analyse le message sélectionné
        res, msg_data = imap.fetch(selected_email_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        # Extrait les informations de l'e-mail (From, Subject, Content)
        From = msg["From"]
        subject = msg["Subject"]
        print("From : ", From)
        print("Subject : ", subject)

        # Analyse du contenu de l'e-mail (si c'est un e-mail au format HTML)
        print("Content : ")
        for part in msg.walk():
            if part.get_content_type() == "text/html":
                print(part)

        # Extrait les URL de l'e-mail
        email_content = str(part)
        regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        match = re.findall(regex, email_content)

        # Nettoyez les URL extraites
        cleaned_urls = []
        for url in match:
            # Utilisez Beautiful Soup pour extraire l'URL proprement
            soup = BeautifulSoup(url, 'html.parser')
            cleaned_url = soup.get_text()
    
            cleaned_urls.append(cleaned_url)

        # Analyse des URL avec VirusTotal
        key = '49fae1b1118da71be726fc10380dba8c231f98ab16fdef0d757df61dd6e0e96b'
        client = vt.Client(key)

        try:
            for url in cleaned_urls:
                print("voici l'URL : ", url)
                # Vérifiez si l'URL est correcte avant de l'envoyer à VirusTotal
                if is_valid_url(url):
                    analysis = client.scan_url(url)
                    analysis_info = analysis.to_dict()
                    
                    # Voir si l'URL est sûre ou non
                    if 'data' in analysis_info and 'attributes' in analysis_info['data']:
                        stats = analysis_info['data']['attributes']['last_analysis_stats']
                        if 'malicious' in stats and stats['malicious'] > 0:
                            print(f"L'URL {url} est potentiellement dangereuse.")
                        else:
                            print(f"L'URL {url} est considérée comme sûre.")
                    else:
                        print(f"Impossible d'obtenir les informations de sécurité pour l'URL {url}.")
                else:
                    print(f"L'URL {url} n'est pas valide.")

        except Exception as e:
            print("Une erreur s'est produite lors de l'analyse de l'e-mail :", str(e))

    finally:
        # Assurez-vous de fermer la session client après utilisation
        client.close()

# Fermez la connexion IMAP
imap.close()
