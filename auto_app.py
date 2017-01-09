# -*-coding:Latin-1 -*

__author__ = "abdelmajid"
__date__ = "$8 avr. 2015 23:37:00$"
#===============================================================================
__doc__ = """
c'est l'interface principale du notre application (PADA).
-- qui métriser toute l'application --
"""
#===============================================================================
from automate import *
from convertion_re_en_automate import *
from convertion_to_re import *
from minimisation_afd import *
from transformation_auto import *
from aide_cours import *
from cours.aide_fich import compiler_texte
from tkinter import *
from tkinter import tix
from tkinter import filedialog
import json
from tkinter.simpledialog import askstring



#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
class AutoApp(Toplevel):
    """
    c'est la fenetre principale qui contient l'ensembles des widgets de notre
    application 'PADA'
    """
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    nb_auts = 0#le nombre des fenetres d'automates construits
    autos = {}#les automates et leurs noms.
    fen=Tk()#la fenetre principale (aucune fct dans notre app)
    fen.attributes('-alpha',1)#transparent
    fen.overrideredirect(1)#fenetre sans border ni bandeau.
    #a.transient(a.master)#fentre modale , sans les bouttons de redimensionnement.
    im_back=PhotoImage(file='imgs/py_back_7.png')
    l=Label(fen,image=im_back,bg='#F8FC19')
    l.images=im_back
    l.pack(expand=1,fill=BOTH)
    w_screen,h_screen=int(fen.winfo_screenwidth()),int(fen.winfo_screenheight())
    #wf,hf=2*w_screen//3,h_screen//2
    wf,hf=im_back.width(),im_back.height()
    print(wf,hf)
    fen.geometry("%dx%d+%d+%d"%(wf,hf,(w_screen-wf)//2,(h_screen-hf)//2))
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def __init__(self,largeur=800, hauteur=520):
        """"""
        super().__init__(AutoApp.fen)
        self.title("PADA: construction d'un automate")
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+%d+%d" % (largeur, hauteur, (sw-largeur) // 2, (sh-hauteur) // 2))
        self.largeur, self.hauteur = largeur, hauteur
        self.automates = list()
        #
        self.automate_courant = AutoGraphe(self, self.largeur, self.hauteur)
        #self.automates.append(self.automate_courant)
        self.automate_courant.pack(expand=1,fill=BOTH)
        #l'ajout de la bare de menu----
        mn = Menu(self, fg='yellow', relief='ridge')
        m1 = Menu(mn)
        m1.add_command(label="nouveau %22s"%('CTRL+N'), command=AutoApp.nouveau_automate)
        m1.add_command(label="ouvrir %27s"%('CTRL+O'), command=self.ouvrir_automate)
        m1.add_command(label="enregistrer sous %10s"%('CTRL+S'), command=self.enregistrer_automate)
        #m1.add_command(label="enregistrer tant que PDF", command=self.save_pdf)
        m1.add_checkbutton(label="plein écran %18s"%('CTRL+L'), command=self.plein_ecran)
        m1.add_command(label="quitter %26s"%('ALT+F4'), command=self.destroy)
        mn.add_cascade(label="Options", menu=m1)
        m2 = Menu(mn)
        m2.add_command(label="convert en AFD", command=self.convert_to_AFD)
        m2.add_command(label="completer automate", command=self.completer_automate)
        m2.add_command(label="minimiser automate", command=self.minimiser_automate)
        m2.add_command(label="convert en RE", command=self.convert_to_RE)
        m2.add_command(label="convert RE en automate", command=self.convert_re_to_automate)
        mn.add_cascade(label="Conversion", menu=m2)
        m4 = Menu(mn)
        m4.add_command(label="fermeture transitive",command=self.fermeture_transitive_gest)
        m4.add_command(label="concaténation",command=lambda:self.concatener_ou_reunion())
        m4.add_command(label="réunion",command=lambda:self.concatener_ou_reunion(False))
        mn.add_cascade(label="Opérations", menu=m4)
        m3 = Menu(mn)
        m3.add_command(label="détérmination", command=self.tester_determination)
        m3.add_command(label="reconnaissance du mot", command=self.tester_reconnaissance)
        mn.add_cascade(label="Teste", menu=m3)
        m5 = Menu(mn)
        m5.add_command(label="cours automates finis", command=self.cours_auto)
        m5.add_command(label="aide", command=self.aide_app)
        m5.add_command(label="à propos", command=self.a_propos_app)
        mn.add_cascade(label="Aides", menu=m5)
        #ajout des événement du clavier
        self.bind('<Control-Key>',self.controles_click)
	    #
        self.config(menu=mn)
        #
        #self.wm_attributes('-topmost', 1)#au 1er plan.
        self.focus()
        #
        AutoApp.nb_auts += 1
        self.nom = 'Automate @{0}@'.format(AutoApp.nb_auts)
        AutoApp.autos[self.nom] = self
        self.title(self.title() + " :: [" + self.nom + "]")
        #--------------------------
        self.bind("<Destroy>",self.quitter)
        self.tk.call('wm', 'iconbitmap', self._w, '-default', 'imgs/icone.ico')

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def convert_to_AFD(self):
        """
        méthode qui permette de convertir l'automate courant en AFD.
        c'est un géqtionnaire d'événement 'click sur btn converter en AFD'.
        """
        if len(self.automate_courant.I) < 1 or len(self.automate_courant.F) < 1:
            message = ""
            if len(self.automate_courant.I) < 1:
                message += "l'automate a besoin d'état initial.\n"
            if len(self.automate_courant.F) < 1:
                message += "l'automate a besoin des états finaux.\n"
            showerror('erreur', message,parent=self)
        elif self.automate_courant.est_deterministe():
            showinfo('infos', 'cet automate est détérministe (AFD).',parent=self)
        else:
            b = TransformAuto(self.automate_courant)
            self.automate_courant.pack_forget()
            self.automate_courant = b.automateD
            self.automate_courant.dessiner()
            self.automate_courant.pack(expand=1,fill=BOTH)
            #self.automates.append(b.automateD)
            
            """
            print(b.automateD.Transitions)
            print(b.automateD.Q)
            for e in list(b.automateD.Q):
                print(e.etiquette,e.ens_etats)"""
                
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def completer_automate(self):
        """
        le géstionnaire d'événement 'click sur btn completer'.
        """
        self.automate_courant.completer()

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 

    def minimiser_automate(self):
        """
        le géstionnaire d'événement 'click sur btn minimiser automate'
        """
        if len(self.automate_courant.I) < 1 or len(self.automate_courant.F) < 1:
            message = ""
            if len(self.automate_courant.I) < 1:
                message += "l'automate a besoin d'état initial.\n"
            if len(self.automate_courant.F) < 1:
                message += "l'automate a besoin des états finaux.\n"
            showerror('erreur', message,parent=self)
        else:
            if not self.automate_courant.est_deterministe():
                self.convert_to_AFD()
                showinfo("information", "cet automate est non détérministe,\n\
                on le convert en AFD.",parent=self)
            b = MinimiserAfd(self.automate_courant)
            #self.automate_courant.destroy()
            self.automate_courant.pack_forget()
            self.automate_courant = b.automateM
            #self.automates.append(b.automateM)
            self.automate_courant.pack(expand=1,fill=BOTH)
            b.mini_automate()
            
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 

    def convert_to_RE(self):
        """
        le géstionnaire d'événement 'click sur btn convert en RE'
        """
        if len(self.automate_courant.I) < 1 or len(self.automate_courant.F) < 1:
            message = "cet automate ne peut pas se convertir en expression reguliére: \n"
            if len(self.automate_courant.I) < 1:
                message += "l'automate a besoin d'état initial.\n"
            if len(self.automate_courant.F) < 1:
                message += "l'automate a besoin des états finaux.\n"
            showerror('erreur', message,parent=self)
        else:
            b = AutomateRE(self.automate_courant)
            #self.automate_courant.destroy()
            self.automate_courant.pack_forget()
            self.automate_courant = b.automate
            #self.automates.append(b.automateM)
            self.automate_courant.pack(expand=1,fill=BOTH)
            #self.automate_courant.dessiner()
            
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def convert_re_to_automate(self):
        """
        le géstionnaire d'événement 'click sur btn convert re to automate'
        """
        c = ReToAutomate(self.automate_courant)
        self.automate_courant.pack_forget()
        self.automate_courant = c.automate
        #self.automates.append(b.automateM)
        self.automate_courant.pack(expand=1,fill=BOTH)
            
            
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def save_pdf(self):
        """
        géstionnaire d'événement click sur 'enregistrer pdf'
        """
        showinfo("erreur", "le module 'ReportLab' qui permet\n\
        de faire cela, n'est pas encore disponible sous Python 3\n\
        mais en Python 2.6 et 2.7 il est disponible !!!!",parent=self)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def get_automate_packer(self):
        """
        la méthode qui permette de retourner l'automate actuelle dans l'interface.
        """
        if len(self.automates) > 1:
            return self.automates[-1]
        return None

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def enregistrer_automate(self):
        """
        la méthode qui permette d'enregister l'automate courant.
        """
        a = filedialog.asksaveasfilename(title="enregistrer automate", filetypes=[('PADA fichier', '.pap')])
        if a is not None and a != "":
            if not a.endswith(".pap"):
                a += ".pap"
            with open(a, mode="w", encoding="latin-1") as auto:
                json.dump(self.automate_courant.get_dictionnaire_simplifie(), auto, indent=4)
        else:
            showinfo("automate non enregistré", "cet automate n'est pas enregistré !!")
        

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def ouvrir_automate(self):
        """
        la méthode qui permette d'enregister l'automate courant.
        """
        a = filedialog.askopenfilename(title="ouvrir un automate", filetypes=[('PADA fichier', '.pap')])
        if a is not None and a != "":
            try:
                with open(a, mode="r", encoding="latin-1") as auto:
                    dic = json.load(auto)
                    nvautomate = AutoGraphe.dict_to_automate(self, dic, True)
                    if nvautomate is None:
                        raise KeyError
                    self.automate_courant.pack_forget()
                    self.automate_courant = nvautomate
                    self.automate_courant.pack(expand=1,fill=BOTH)
                    self.automate_courant.dessiner()
                    self.title("PADA: "+a.split("/")[-1][:-4]+" :: ["+self.nom+"]")
            except:
                showerror("erreur", "le fichier ne contient pas un automate \n\
                ou  bien n'est pas compatible au PADA !!",parent=self)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def nouveau_automate(cls,automate=None,title=None):
        """
        le géstionnaire d'événement pour le click sur le boutton 'nouveau' du 
        menu, qui peremette de lancer nouvelle fenetre pour construire un 
        nouveau automate.
        """
        a = AutoApp()
        if automate is not None:
            if type(automate) is AutoGraphe:
                a.automate_courant.pack_forget()
                a.automate_courant = automate.copie(a)
                a.automate_courant.pack(expand=1,fill=BOTH)
                #a.automate_courant.dessiner()
                if title is not None:
                    a.title("PADA: "+title+" :: ["+a.nom+"]")
        #a.grab_set()
        #a.focus_set()
        #a.mainloop()
    #definir une méthode de classe
    nouveau_automate = classmethod(nouveau_automate)        
 
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def tester_determination(self):
        """
        le géstionaire du click sur le boutton menu (détérmination).
        """
        if self.automate_courant.est_deterministe():
            showinfo("détérmination","cet automate est détérministe (AFD)",parent=self)
        else:
            showinfo("détérmination","cet automate est non détérministe (AFN)",parent=self)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def tester_reconnaissance(self):
        """
        le géstionnaire d'événement click sur le boutton menu 'reconnaissnace du mot'.
        """
        if not self.automate_courant.est_deterministe():
            showinfo("reconnaissance du mot","Automate non déterminste:\nce test est fait pour les automates \nfinis déterministes, pensez à le déterminser",parent=self)
            return
        mot=askstring("mot","entrer un mot :",parent=self)
        reponse=self.automate_courant.a_reconnu_mot(mot)
        if reponse==True:
            showinfo("reconnaissance du mot","le mot '{0}' est reconnau par cet automate".format(mot),parent=self)
        elif reponse==False:
            showinfo("reconnaissance du mot","cet automate ne reconnu pas le mot '{0}'.".format(mot),parent=self)
        else:
            showinfo("reconnaissance du mot","cet automate ne reconnu pas le mot '{0}'.\n car {1}.".format(mot,reponse),parent=self)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def fermeture_transitive_gest(self):
        """
        le géstionnaire d'événement click sur le boutton de menu
        'fermeture transitive'.
        """
        AutoGraphe.fermeture_transitive(self.automate_courant)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def concatener_ou_reunion(self,concate=True):
        """
        le géstionnaire d'événement click sur les bouttons de menu
        'concaténation' ou 'réunion'.
        lorsque le paramétre concate=True donc cette méthode fait la concaténation
        sinon fait la réunion.
        """
        if len(AutoApp.autos.keys())<2:
            showinfo("aucun autre automate ouvré","il faut ouvrir des autres automates pour faire la concaténation.",parent=self)
            return
        top=tix.Tk()
        top.config(bg='#2E2E2E')
        dimension,xl,yl=self.geometry().split('+')
        wl,hl=dimension.split('x')
        xl,yl,wl,hl=int(xl),int(yl),int(wl),int(hl)
        top.geometry("+%d+%d"%(xl+wl//2,yl+hl//2))
        if concate:
            top.title("concaténation d'automate {0}".format(self.nom))
        else:
            top.title("réunion d'automate {0}".format(self.nom))
        Label(top,text="choisir un automate:",font="andalus 12 italic",fg='#10BEBE',bg='#2E2E2E').grid(row=0,column=0,columnspan=2,padx=1,pady=1,sticky=N+E+W+S)
        nom_auto=StringVar(top)
        nom_auto.set(list(AutoApp.autos.keys())[0])
        choix=tix.ComboBox(top,variable=nom_auto,width=22)
        #print(choix.config())
        for nom_aut in AutoApp.autos.keys():
            choix.insert(END,nom_aut)
        #nom_auto.set(list(AutoApp.autos.keys())[0])
        choix.grid(row=0,column=2,columnspan=2,padx=1,pady=1,sticky=N+E+W+S)
        def click_btn_ok():
            top.destroy()
            if AutoApp.get_automate_par_nom(self.nom) is not None and AutoApp.get_automate_par_nom(nom_auto.get()) is not None:
                _title=self.nom+" et "+nom_auto.get()
                if concate:
                    AutoGraphe.concatener(self.automate_courant,AutoApp.get_automate_par_nom(nom_auto.get()).automate_courant,title="concaténation de "+_title)
                else:
                    AutoGraphe.reunion(self.automate_courant,AutoApp.get_automate_par_nom(nom_auto.get()).automate_courant,title="réunion de "+_title)                
            else:
                showerror("erreur","automate non trouvé",parent=self)
        def click_btn_annuler():
            top.destroy()
        Button(top,text="Ok",command=click_btn_ok,bg='light green',relief='raised',font="andalus 14 bold",height=2,width=7,cursor='hand2').grid(row=1,column=1,padx=1,pady=1,sticky=N+E+W+S)
        Button(top,text="annuler",command=click_btn_annuler,bg='salmon',relief='raised',font="andalus 14 bold",height=2,width=7,cursor='hand2').grid(row=1,column=2,padx=1,pady=1,sticky=N+E+W+S)
        

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def get_automate_par_nom(cls,nom):
        """
        une méthode de classe qui permette de retourner un automate
        stocker dans 'AutoApp.autos' par son nom.
        """
        if nom in AutoApp.autos.keys():
            if type(AutoApp.autos[nom]) is AutoApp:
                return AutoApp.autos[nom]
        return None
    #définie la méthode comme méthode du classe.
    get_automate_par_nom=classmethod(get_automate_par_nom)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def quitter(self,event):
        """
        la méthode appelé lorsque quitter une fenetre.
        """
        print("~~~~~~quitter :",self.nom,"~~~~~~",type(event.widget))
        if type(event.widget) is AutoApp:
            if self.nom in AutoApp.autos.keys():
                if len(self.automate_courant.Q)>0:
                    if askyesno("enregistre automate","voulez-vouz enregistrer cet automate '{0}', avant le fermé ?".format(self.nom)):
                        self.enregistrer_automate()
                del AutoApp.autos[self.nom]
            if len(AutoApp.autos)<1:
                AutoApp.fen.destroy()
                
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def plein_ecran(self):
        """
        géstionnaire dévénement click sue le boutton de menu 'plein ecran'.
        """
        if self.wm_attributes('-fullscreen')==1:
            self.wm_attributes('-fullscreen', 0)
        else:
            self.wm_attributes('-fullscreen', 1)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def a_propos_app(self):
        """
        le géstionnaire d'événement click sur le boutton de menu 'a propos'.
        """
        t=Toplevel(self,cursor='hand2')
        t.overrideredirect(1)#fenetre sans border ni bandeau.
        lab=Label(t,bg='light green',\
        text="PADA 1.0\nPython Automates Déterminste Application",\
        font=("Arial black",20,"bold"),fg="brown",relief='groove',bd=5)
        w_screen,h_screen=int(t.winfo_screenwidth()),int(t.winfo_screenheight())
        t.geometry("+%d+%d"%(w_screen//2-300,h_screen//2-100))
        def disparaitre(event):
            t.destroy()
        t.bind("<Button-1>",disparaitre)
        lab.pack(fill=BOTH)
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def aide_app(self):
        """
        le géstionnaire d'événement click sur le boutton de menu 'aide'.
        """
        #showinfo("aide?","on va affciher des instructions d'utilisation de notre app.",parent=self)
        t=Toplevel(self)
        t.title("Aide d'application PADA")
        #t.attributes('-alpha',1)#transparent
        #t.overrideredirect(1)#fenetre sans border ni bandeau.
        txt=Text(t,width=110, height=20,tabs=('2c', '4.5c', 'right', '9c', 'center', '13c', 'numeric'))
        scroll = Scrollbar(t, command=txt.yview,width=5)
        txt.configure(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT,expand =NO,fill=Y)
        txt.tag_configure('quoi', font=('andalus', 13, 'normal', 'normal'),foreground='black')
        txt.tag_configure('titre', font=('Verdana', 14, 'bold', 'italic'),foreground='green')
        txt.tag_configure('soustitre', font=('andalus', 14, 'normal', 'italic'),foreground='blue')
        txt.tag_configure('textnormal', font=('arial', 12, 'normal', 'italic'),foreground='brown')
        compiler_texte(txt)
        txt.configure(state='disabled')
        txt.pack(fill=BOTH,expand=1)
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def cours_auto(self):
        """
        le géstionnaire d'événement click sur le boutton de menu 'a propos'.
        """
        #showinfo("aide?","on va affciher des instructions d'utilisation de notre app.",parent=self)
        CoursAuto(self)   
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def controles_click(self,event):
        """
        lorsqu'on clique dur le btn 'CTRL'.
        """
        key=event.keysym
        if key in ['n','N']:
            self.nouveau_automate()
        elif key in ['o','O']:
            self.ouvrir_automate()
        elif key in ['s','S']:
            self.enregistrer_automate()
        elif key in ['l','L']:
            self.plain_ecran()
