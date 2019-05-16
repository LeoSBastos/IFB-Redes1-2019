from tkinter import *
from imap import Email
class MainWindow():
    
    def __init__(self):
        self.LoginVal = None
        self.SenhaVal = None
        self.login = Tk()
        self.LoginWindow()

    def LoginWindow(self):

        self.login.title("Login")
        
        welcome = Label(self.login, text="Por favor, insira suas credenciais")
        welcome.grid(row=0,column=0,sticky=N)
        
        LabelE = Label(self.login, text="Digite seu email: ")
        LabelS = Label(self.login, text="Digite sua senha: ")
        LabelE.grid(row=1,column=0,sticky=W)
        LabelS.grid(row=3,column=0,sticky=W)

        self.CampoE = Entry(self.login)
        self.CampoS = Entry(self.login,show="*")
        self.CampoE.grid(row=2,column=0,sticky=W)
        self.CampoS.grid(row=4,column=0,sticky=W)

        BotaoLogin = Button(self.login, text="Login", command=self.EmailList)
        BotaoLogin.grid(columnspan=2, sticky=W)

        self.login.mainloop()

    def EmailList(self):
        self.listwindow = Tk()
        
        self.listwindow.title("Assuntos")

        self.em = Email(self.CampoE.get(),self.CampoS.get())
        self.login.destroy()
        self.em.listaAssunto()
        self.listaemail = self.em.listaemail
        
        self.ListaEmail=Listbox(self.listwindow)
        
        for email in self.listaemail:
            self.ListaEmail.insert(END, email[1])
        self.ListaEmail.grid(row=0, column=0, columnspan=2, padx=5,pady=5, sticky="nsew")
        
        BotaoLer = Button(self.listwindow, text="Ler", command=self.EmailWindow)
        BotaoLer.grid(row=0,column=2,columnspan=2, sticky=W)
        self.listwindow.mainloop()

    def EmailWindow(self):
        aux= self.ListaEmail.get(self.ListaEmail.curselection())
        window = Tk()
        window.title("Email")
        self.listwindow.destroy()
        for email in self.listaemail:
            if(email[1] == aux):
                self.em.downloadEmail(email[0])
        LabelDe=Label(window, text="De: ")
        LabelDe.grid(row=0,column=0)

        LabelPara=Label(window, text="Para: ")
        LabelPara.grid(row=0,column=2)

        LabelAssunto=Label(window, text="Assunto: ")
        LabelAssunto.grid(row=1,column=0)

        ValDe=Label(window,text=self.em.email_de)
        ValDe.grid(row=0, column=1,sticky=W)

        ValPara=Label(window,text=self.em.email_para)
        ValPara.grid(row=0, column=3,sticky=W)

        ValAssunto=Label(window,text=self.em.email_assunto)
        ValAssunto.grid(row=1, column=1,sticky=W)

        ValEmail=Label(window,text=self.em.email)
        ValEmail.grid(row=2, column=0, columnspan=4,sticky=W)
        window.mainloop()

if __name__ == "__main__":
    mw = MainWindow()
