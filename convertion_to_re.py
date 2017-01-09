# -*-coding:Latin-1 -*

#===============================================================================
__author__ = "abdelmajid"
__date__ = "$21 avr. 2015 04:01:45$"
__doc__ = """
c'est un module qui contient tout ce que concerne la technique de concvertion 
d'un automate en une expression r�guli�re.
"""
#===============================================================================
from etat import *
from random import randrange
from tkinter import *
from tkinter.messagebox import showinfo
from transition import *
from transformation_auto import *
#===============================================================================

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class AutomateRE:
    """
    c'est la classe qui permette de convertir un automate 
    en une expression r�guli�re.
    """
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def __init__(self, automate):
        """
        initialisateur du classe qui prend en param�tres l'automate � convertir.
        """
        self.automate_origine=automate.copie(automate.master)
        self.automate_afd=TransformAuto(automate).automateD.copie(automate.master)
        self.automate = automate.copie(automate.master)
        #self.automateRE = AutoGraphe(self.automate.master, self.automate.largeur, self.automate.hauteur)
        self.generateur_convertion = iter(self.algo_convert_to_re())
        #---------------
        self.frame = Frame(self.automate.toile, relief='groove', bg='light blue')
        Button(self.frame, text="suivant", command=self.etape_suivante, relief="groove", bg='#88F633', width=10, cursor="hand2").grid(row=0, column=0, sticky=N + E + S + W, padx=2, pady=1)
        Button(self.frame, text="tous", command=self.finir_algo, relief="groove", bg='yellow', width=10, cursor="hand2").grid(row=0, column=1, sticky=N + E + S + W, padx=2, pady=1)
        self.num_frame = self.automate.toile.create_window(90, 20, window=self.frame)
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def algo_convert_to_re(self):
        """
        l'algorithme de convertion d'un automate en une expression r�guli�re.
        algrorithme: --�limination des �tats--
        """
        
        while True:
            n_fi = list(self.automate.Q-(self.automate.I | self.automate.F))#liste des �tats ni final ni initial.
            n_fi = n_fi.copy()
            for etat in n_fi:
                trans_r = list(set(etat.transDepart) & set(etat.transFin))#les transition r�flexive.au plus une.
                trans_d = list(set(etat.transDepart)-set(trans_r))##les transition partant d'etat.
                trans_f = list(set(etat.transFin)-set(trans_r))##les transition arrivant � l'etat.
                r = ""
                if len(trans_r) > 0:
                    r = "+".join(trans_r[0].lettres)
                if r == self.automate.epsilon:
                    r = ""
                elif len(r) > 0:
                    if len(r) > 1:
                        r = "(" + r + ")"
                    r += "*"
                
                for tf in trans_f:
                    f = "+".join(tf.lettres)
                    if f == self.automate.epsilon:
                        f = ""
                    elif len(tf.lettres) > 1:
                        f = "(" + f + ")"
                    f += r
                    for td in trans_d:
                        d = "+".join(td.lettres)
                        if d == self.automate.epsilon:
                            d = ""
                        elif len(td.lettres) > 1:
                            d = "(" + d + ")"
                        d = f + d
                        if d == "":
                            d = self.automate.epsilon
                        print("chemin : ", tf.etatDepart.etiquette, "--->"\
                              , etat.etiquette, "--->", td.etatFin.etiquette, " , � �tiquet par :'", d, "'")
                        for tr in list(self.automate.Transitions):
                            if tr.etatDepart == tf.etatDepart and tr.etatFin == td.etatFin:
                                lsttrs=tr.lettres.copy()
                                lsttrs.add(d)
                                ex="+".join(lsttrs)
                                if len(lsttrs)>1:
                                    ex="("+ex+")"
                                tr.lettres = set([ex])
                                break
                        else:TransitionGraphe(self.automate, tf.etatDepart, td.etatFin, set([d]))
                        #yield
                etat.supprimer()
                self.automate.dessiner()
                self.num_frame = self.automate.toile.create_window(90, 20, window=self.frame)
                yield
            #continuation(�liminer les �tats finaux et initiaux)
            #on ajoute un �tat initial (qi) et un �tat final (qf) � l'automate
            #et epsilon-transitions de (qi) vers tout �tat initial de l'automate, 
            #et de chaque �tat final vers qf.
            if not(len(self.automate.I) == 1 and len(self.automate.F) == 1\
                   and len(self.automate.Q ^ (self.automate.I | self.automate.F)) == 0\
                   and len(self.automate.Transitions) == 1 and len(self.automate.Q) != 1\
                       and len(list(self.automate.Transitions)[0].lettres)<2):
                xi, yi = randrange(EtatGraphe.rayon + 20, \
                                   self.automate.largeur * 7 // 8-EtatGraphe.rayon), randrange(EtatGraphe.rayon, \
                                                           self.automate.hauteur-EtatGraphe.rayon)
                xf, yf = randrange(EtatGraphe.rayon + 20, \
                                   self.automate.largeur * 7 // 8-EtatGraphe.rayon), randrange(EtatGraphe.rayon, \
                                                           self.automate.hauteur-EtatGraphe.rayon)
                etat_initial = EtatGraphe(self.automate, (xi, yi), 'qi')
                etat_final = EtatGraphe(self.automate, (xf, yf), 'qf')
                for etat_i in list(self.automate.Q):
                    if etat_i.initial:
                        TransitionGraphe(self.automate, etat_initial, etat_i, set())
                        etat_i.initial = False
                    if etat_i.final:
                        TransitionGraphe(self.automate, etat_i, etat_final, set())
                        etat_i.final = False
                etat_final.final = True
                etat_initial.initial = True
                etat_final.dessiner()
                etat_initial.dessiner()
            else:
                break#fin d'algorithme;; 
            yield
        xi, yi = EtatGraphe.rayon * 2, self.automate.hauteur-EtatGraphe.rayon * 2
        xf, yf = self.automate.largeur * 7 // 8-EtatGraphe.rayon * 2, self.automate.hauteur-EtatGraphe.rayon * 2
        for ei in list(self.automate.I):
            ei.set_centre(xi, yi)
        for ei in list(self.automate.F):
            ei.set_centre(xf, yf)
        self.automate.dessiner()
        frame=Frame(self.automate.toile)
        txt = Text(frame, width=30, height=6, bg='light green',\
        relief='groove',font="arial 12 bold",fg='dark blue',bd=2)
        exp = "".join(list(self.automate.Transitions)[0].lettres)
        txt.insert(END, "l'expression r�guli�re est:\n")
        txt.insert(END, exp)
        
            
        frame_verification=self.cadre_verfication_mot(frame)
        txt.grid(row=0,padx=0,pady=1,sticky=N+E+S+W)
        frame_verification.grid(row=1,padx=0,pady=1,sticky=N+E+S+W)
        self.automate.toile.create_window(self.automate.largeur * 7 // 8 // 2, \
                                              self.automate.hauteur // 2, window=frame)
        yield
        

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def etape_suivante(self):
        """
        le g�stionnaire du boutton 'suivant'
        """
        #try:
        next(self.generateur_convertion)
        #except:
        #    self.automate.toile.delete(self.num_frame)
        #    showinfo("algorithme t�rmin�", "toutes les �tapes sont faites.")
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def finir_algo(self):
        """
        le g�stionnaire du boutton 'tous'
        """
        while True:
            try:
                next(self.generateur_convertion)
            except:
                self.automate.toile.delete(self.num_frame)
                break

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def cadre_verfication_mot(self,frame):
        """
        une m�thode qui permette de retourner un cadre (Frame).
        c'est un interfece qui permet de v�rifier un mot s'il est 
        reconnu par un automate ou non.
        � l'aide de l'expression r�guli�re 'expres' d'automate.
        """
        f=Frame(frame,relief='groove',bd=2,bg='light green')
        mot,message=StringVar(),StringVar()
        label=Label(f,textvariable=message,bg='light yellow',relief='ridge')
        def verifier():
            """
            c'est une fonction interne, qui g�rer l'�v�nement click sur le
            boutton 'v�rifier'.
            """
            reponse=self.automate_afd.a_reconnu_mot(mot.get())
            if reponse==True:
                message.set("mot reconnu")
                label['fg']='green'
            elif reponse==False:
                message.set("mot non reconnu.")
                label['fg']='orange'
            else:
                message.set(reponse)
                label['fg']='red'
        Label(f,text="entrer un mot").grid(row=0,column=0,sticky=E+S+N+W,padx=0,pady=1)
        Entry(f,textvariable=mot,width=30,font="arial 12 bold",relief='ridge').grid(row=0,column=1,sticky=E+S+N+W,padx=0,pady=1)
        Button(f,text='verifi�r',bg='light blue',command=verifier).grid(row=1,column=0,columnspan=2,sticky=E+S+N+W,padx=0,pady=1)
        label.grid(row=2,column=0,columnspan=2,sticky=E+S+N+W,padx=0,pady=1)
        
        return f
        
        
        
        
        