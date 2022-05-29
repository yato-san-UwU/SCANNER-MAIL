# SCANNER-MAIL
-python version 3.10.4

le script à pour but de scanner le dernier mail recu, en prennat l'url (si une url ce trouve dans le contenut), grace l'API de https://www.virustotal.com pour pouvoir scanner l'URL

pour pouvoir utiliser le script
-il faut une boite mail ou imap est activer : https://support.google.com/mail/answer/7126229?hl=fr#zippy=%2Cétape-vérifier-quimap-est-activé
-aussi activer "less secure apps" : https://hotter.io/docs/email-accounts/secure-app-gmail/

pour pouvvoir utiliser l'API de VirusTotal il faut l'API key qui est donnais avec la création d'un compte, pour ce script cest ma cle qui est utilisé, pas besoin dans cree une.
Aussi avoir la libraire vt-py : https://github.com/VirusTotal/vt-py


programme realiser grace à ces differentes sources :

///-https://docs.python.org/3/library/email.html
///-https://docs.python.org/3/library/imaplib.html
///-https://www.youtube.com/watch?v=4iMZUhkpWAc
///-https://fr.acervolima.com/recuperer-les-details-des-e-mails-recemment-envoyes-via-un-compte-gmail-a-laide-de-python/
///-https://stackoverflow.com/questions/49654499/python-extract-urls-from-email-messages
///-https://stackoverflow.com/questions/43727583/re-sub-erroring-with-expected-string-or-bytes-like-object



lors de l'execution du script 2 problemes s'affiche :
-le resultat du script qui ne saffiche pas toujours correcttement. résultat espéré : https://github.com/yato-san-UwU/SCANNER-MAIL/blob/main/resultat-tp-secu.PNG
-et une erreur "unclosed session"  : https://github.com/yato-san-UwU/SCANNER-MAIL/blob/main/unclosed-tp-secu.PNG
