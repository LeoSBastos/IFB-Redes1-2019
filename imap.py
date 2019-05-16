import imaplib
import email
import base64
from email.parser import HeaderParser as hp

class Email:
    def __init__(self, login, senha, server = 'imap.gmail.com'):
        self.server = server
        self.login = login
        self.senha = senha
        self.mailbox = imaplib.IMAP4_SSL(self.server)
        self.mailbox.login(self.login,self.senha)
        self.mailbox.select("inbox")
        self.email_de = None
        self.email_para = None
        self.email_assunto = None
        self.email = None
        self.listaemail=[]
    
    def listaAssunto(self):
        ids_messages = self.mailbox.uid("search",None,"ALL")[1][0].split()
        print("Total de emails: {}".format(len(ids_messages)))
        print("Carregando ultima mensagem")
        for i in ids_messages:
            msglinhas = self.mailbox.uid("fetch",i,"(RFC822)")[1][0][1]
            em = email.message_from_bytes(msglinhas+b'\r\n')
            self.listaemail.append([i,em.get("Subject")])

    def downloadEmail(self, uid):
        msglinhas = self.mailbox.uid("fetch",uid,"(RFC822)")[1][0][1]
        em = email.message_from_bytes(msglinhas+b'\r\n')
        if em.is_multipart():
                for part in em.get_payload():
                    if not part.is_multipart():
                        self.email = em.get_payload()[0]
                        # if self.email[-3] == "=":
                        #     self.email=base64.b64decode(self.email).decode("utf-8")
        else:
            self.email = em.get_payload()[0]
            # if self.email[-3] == "=":
            #     self.email=base64.b64decode(self.email).decode("utf-8")

        self.email_de = em.get("From")
        self.email_para = em.get("To")
        self.email_assunto = em.get("Subject")
        self.mailbox.close()
        # return em.get("From"), em.get("To"), em.get("Subject")