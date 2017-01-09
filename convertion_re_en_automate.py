# -*-coding:Latin-1 -*

#===============================================================================
__author__ = "abdelmajid"
__date__ = "$26 avr. 2015 08:12:32$"
__doc__ = """
c'est un module qui contient tout ce que concerne la technique de concvertion 
d'une expression régulière en un automate.
"""
#===============================================================================
from automate import *
from tkinter.simpledialog import *
import re

#===============================================================================
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class ReToAutomate:
    """
    la classe qui permette de tconvertir une expression régulière en un automate.
    """
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def __init__(self,automate):
        """
        l'initialisateur du classe
        """
        self.automate=AutoGraphe(automate.master,automate.largeur,automate.hauteur)
        #while True:
        #    try:
        self.expression=askstring(parent=automate,title="expression régulière",prompt="entrez une éxpression régulière")
        #re.compile(self.expression)
        #        break
        #    except:
        #        showerror("erreur","expression régulière non valide !!")
        
        #self.convertir_to_automate(self.expression)
        print("+:",self.diviser_reunion(self.expression))
        print(".:",self.diviser_concatenation(self.expression))
        print("*:",self.diviser_fermeture_kleene(self.expression))
        #generateur
        self.generateur_etapes=None
        self.convertir_to_automate(self.expression)
        #---------------les bouttons pour voir les étapes de convertions
        self.frame=Frame(self.automate.toile,relief='groove',bg='salmon')
        Button(self.frame,text="suivant",command=self.etape_suivante,relief="ridge",bg='light green',width=10,cursor="hand2").grid(row=0,column=0,sticky=N+E+S+W,padx=2,pady=1)
        Button(self.frame,text="tous",command=self.finir_algo,relief="ridge",bg='yellow',width=10,cursor="hand2").grid(row=0,column=1,sticky=N+E+S+W,padx=2,pady=1)
        self.num_frame=self.automate.toile.create_window(90,20,window=self.frame)
#ab+c((ab(c+d)*(ab)*)*c*)+(a+b)c

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def convertir_to_automate(self,expression):
        """
        c'est la méthode qui décrit l'algorithme de convertion d'une expression
        régulière en un automate.
        """
        etat_i=EtatGraphe(self.automate,centre=None,initial=True)
        etat_f=EtatGraphe(self.automate,centre=None,final=True)
        if expression=="" or len(expression)==1:
            if len(expression)==1:
                TransitionGraphe(self.automate,etat_i,etat_f,set(expression))
            self.automate.dessiner()
        else:
            tr=TransitionGraphe(self.automate,etat_i,etat_f,set([expression]))
            self.automate.dessiner()
            self.generateur_etapes=iter(self.etapes_convertion(tr))
                
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def etapes_convertion(self,transition_d):
        """
        méthode qui fait toutes les étapes pour la convertion d'une expression
        régulière en automate.
        """
        transit=list()
        transit.append(transition_d)
        print("entrant")
        while len(transit)>0:
            for transition in transit:
                #------------------------réunions---------------------------------------
                r=list(transition.lettres)[0]#l'expression portée par la transition.
                exprs=self.diviser_reunion(r)
                print("union  '{0}'".format(exprs))
                transitions1=list()#les transitions feront en les réunions
                if len(exprs)>1:
                    for exp in exprs:
                        ei=EtatGraphe(self.automate,centre=None);ei.dessiner()
                        ef=EtatGraphe(self.automate,centre=None);ef.dessiner()
                        tu=TransitionGraphe(self.automate,ei,ef,set([exp]));tu.dessiner()
                        TransitionGraphe(self.automate,ef,transition.etatFin).dessiner()#epsilon transition
                        TransitionGraphe(self.automate,transition.etatDepart,ei).dessiner()#epsilon transition
                        transitions1.append(tu)
                    transition.supprimer()
                else:
                    transition.lettres=set(exprs)
                    transition.dessiner()
                    transitions1.append(transition)
                yield
                #------------------------concaténations---------------------------------
                transitions2=list()#les transitions feront en les concaténations.
                for tr in transitions1:
                    r=list(tr.lettres)[0]#l'expression portée par la transition.
                    exprs=self.diviser_concatenation(r)
                    print("concat  '{0}'".format(exprs))
                    if len(exprs)>1:
                        ei,ef=tr.etatDepart,tr.etatFin
                        for exp in exprs:
                            ej=EtatGraphe(self.automate,centre=None);ej.dessiner()
                            tc=TransitionGraphe(self.automate,ei,ej,set([exp]));tc.dessiner()
                            ei=ej
                            transitions2.append(tc)
                        TransitionGraphe(self.automate,ei,ef).dessiner()
                        tr.supprimer()
                    else:
                        tr.lettres=set(exprs)
                        tr.dessiner()
                        transitions2.append(tr)
                yield
                #------------------------fermeture de kleene----------------------------
                for tr in transitions2:
                    r=list(tr.lettres)[0]#l'expression portée par la transition.
                    exprs=self.diviser_fermeture_kleene(r)
                    print("kleene  '{0}'".format(exprs))
                    if len(exprs)>1 and exprs.count('*')>0:
                        for exp in exprs:
                            if exp!='*':
                                tr.lettres=set([self.automate.epsilon])
                                tr.dessiner()
                                ei=EtatGraphe(self.automate,centre=None);ei.dessiner()
                                ej=EtatGraphe(self.automate,centre=None);ej.dessiner()
                                TransitionGraphe(self.automate,ei,ej,set([exp])).dessiner()
                                TransitionGraphe(self.automate,tr.etatDepart,ei).dessiner()
                                TransitionGraphe(self.automate,ej,tr.etatFin).dessiner()
                                #ajouter une epsilon-transition
                                TransitionGraphe(self.automate,tr.etatFin,tr.etatDepart).dessiner()
                    else:
                        tr.lettres=set(exprs)
                        tr.dessiner()
                yield
            
            #-------------les transition non completement convertée-----------------
            transions=list()#liste des transitions que sera converté.
            for tr in list(self.automate.Transitions):
                if len(list(tr.lettres)[0])>1:
                    transions.append(tr)
            transit=transions.copy()
            """for tr in transions:
                #self.generateur_etapes+=iter(self.etapes_convertion(tr))
                """
            yield

        

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def diviser_reunion(self,r):
        """
        méthode qui permette de diviser une expression régulière sous forme du
        réunion des plusieurs regExpressions. 
        """
        r=self.supprimer_parentheses(r)#supprimer les parenthéses depart fin s'ils est unitules.
        exprs=list()#la liste à retourner
        nb_para=0#le nombre de paranthéses.
        ch,i="",0
        for l in r:
            ch+=l
            if l=="(":nb_para+=1
            if l==")":nb_para-=1
            if l=='+':
                if nb_para==0:
                    ch=ch[:-1]
                    exprs.append(ch)
                    ch=""
        if ch!="":exprs.append(ch)
        if len(exprs)==0:exprs.append(r)
        #exprs=[self.supprimer_parentheses(ch) for ch in exprs]#supprimer les parenthéses unitules
        return exprs

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def diviser_concatenation(self,r):
        """
        méthode qui permette de diviser une expression régulière sous forme du
        concaténation des plusieurs regExpressions. 
        """
        #r=self.supprimer_parentheses(r)#supprimer les parenthéses depart fin s'ils est unitules.
        exprs=list()#la liste à retourner
        nb_para=0#le nombre de paranthéses.a(ab)*b*(a+b)(ab)
        ch=""
        for l in r:
            ch+=l
            if l=='(':nb_para+=1
            if l==')':nb_para-=1
            if nb_para==0:
                if l!='*':
                    exprs.append(ch)
                else:
                    if len(exprs)>0:
                        exprs[-1]+='*'
                ch=""
        if len(exprs)==0:exprs.append(r)
        #exprs=[self.supprimer_parentheses(ch) for ch in exprs]#supprimer les parenthéses unitules
        return exprs
        
                    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def diviser_fermeture_kleene(self,r):
        """
        méthode qui permette de diviser une expression régulière sous forme du
        fermeture de kleene des plusieurs regExpressions. 
        """
        #r=self.supprimer_parentheses(r)#supprimer les parenthéses depart fin s'ils est unitules.
        exprs=list()#la liste à retourner
        nb_para=0#le nombre de paranthéses.
        ch,i="",0
        for l in r:
            ch+=l
            if l=='(':nb_para+=1
            if l==')':nb_para-=1
            if l=='*':
                if nb_para==0:
                    ch=ch[:-1]
                    exprs.append(ch)
                    exprs.append('*')
                    ch=""
        if len(exprs)==0:exprs.append(r)
        #exprs=[self.supprimer_parentheses(ch) for ch in exprs]#supprimer les parenthéses unitules
        return exprs

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def supprimer_parentheses(self,chaine):
        """
        une méthode  qui permette de supprimer les parenthéses unitules.
        (a+b)=>a=b, (ab(a+b)a)=>ab(a+b)a , (ab)(ab)=(ab)(ab)
        """
        if len(chaine)>1:
            if chaine[0]=='(' and chaine[-1]==')':
                nb_p=1
                for i in range(1,len(chaine)):
                    if chaine[i]=='(':nb_p+=1
                    if chaine[i]==')':nb_p-=1
                    if nb_p==0:
                        if i==len(chaine)-1:
                            return chaine[1:-1]
                        else:
                            return chaine
        return chaine
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def etape_suivante(self):
        """
        le géstionnaire du boutton 'suivant'
        """
        try:
            next(self.generateur_etapes)
        except:
            self.automate.toile.delete(self.num_frame)
            #supprimer les lettres (expres)
            lise=[]
            for e in list(self.automate.A):
                if len(e)>1:
                   lise.append(e)
            self.automate.A-=set(lise)
            showinfo("algorithme términé","toutes les étapes sont faites.")
            
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def finir_algo(self):
        """
        le géstionnaire du boutton 'tous'
        """
        while True:
            try:
                next(self.generateur_etapes)
            except:
                self.automate.toile.delete(self.num_frame)
                lise=[]
                #supprimer les lettres (expres)
                for e in list(self.automate.A):
                    if len(e)>1:
                       lise.append(e)
                self.automate.A-=set(lise)
                break

