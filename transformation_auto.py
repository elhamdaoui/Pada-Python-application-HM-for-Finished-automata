# -*-coding:Latin-1 -*

#===============================================================================
__author__ = "abdelmajid"
__date__ = "$14 avr. 2015 03:24:08$"
__doc__="""
c'est un module qui contient tout ce qui concerne une transformation d'un
automate finis non d�t�rministe (AFND), avec ou sans des �tats instantann�es
(epsilon), � un automate fini d�t�rministe (AFD).
"""
#===============================================================================
from tkinter import messagebox
from random import randrange
from automate import *
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class TransformAuto:
    """
    c'est la classe qui permette de transformer un automate AFND
    au un automate AFD.
    """
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def __init__(self,automate):
        """
        initialisateur du classe avec un objet (AutoGraphe) 
        """
        if type(automate) is not AutoGraphe:
            messagebox.showwarning("erreur","il faut transformer un automate et pas d'autre chose ?!!!")
            #ajouter qulq choses pour retourne au l'automate pr�c�dent
        self.automateN=automate#attention au r�f�rence. (fais une copie) !!
        self.automateD=AutoGraphe(self.automateN.master,self.automateN.largeur,self.automateN.hauteur)
        clt_ini=self.etats_cloture_etats(self.automateN.I)
        final=False
        if len(set(clt_ini[1])&set(self.automateN.F))>0:#si l'�tat initial du AFD,contient un �tat final du AFND
            final=True
        self.ajouter_etat(clt_ini[0],True,final)#�tat initial du nouveau automate
        print("############################################")
        print("####### algorithme de transformation #######")
        print("############################################")
        self.transformer('q0',clt_ini[1])
        print("############################################")

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def etats_vers_etats(self,ens_etats,lettre):
        """
        une m�thode qui permette de d�terminer (p') tel que:
        p={e1,e2,e3} --------> p'={ei,ek,...}  avec e dans A.
        """
        etats=list(ens_etats)
        letq,lets=[],[]
        for etat in etats:
            nv_ens=etat.lit_lettre(lettre)
            letq+=nv_ens[0]
            lets+=nv_ens[1]
        letq=list(set(letq))
        lets=list(set(lets))
        return [letq,lets]
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def etats_cloture_etats(self,ens_etats):
        """
        m�thode qui permette de d�terminer epsilon-cl�ture d'un etat (ens d'�tats)
        retourne [[ensembles des �tiquettes],[ensemble des �tats]]
        """
        etats=list(ens_etats)
        letq,lets=[],[]
        for etat in etats:
            clot=etat.cloture()
            letq+=clot[0]
            lets+=clot[1]
        letq=list(set(letq))
        lets=list(set(lets))
        return [letq,lets]

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def ajouter_transition(self,etq_q1,etq_q2,lettre):
        """
        m�thode qui permette d'ajouter une transition au l'automate minimis�.
        s'elle est exist�e d�j�, donc on l'a mis � jour.
        """
        lis=list()
        lis.append(lettre)
        for tr in list(self.automateD.Transitions):
            if tr.etatDepart.etiquette==etq_q1 and tr.etatFin.etiquette==etq_q2:
                tr.lettres=set(list(tr.lettres)+lis)
                return
        TransitionGraphe(self.automateD,self.automateD.get_etat(etq_q1),\
        self.automateD.get_etat(etq_q2),set(lis))

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def ajouter_etat(self,lis_etq,initial=False,final=False):
        """
        m�thode qui permette d'ajouter un �tat s'il est non encore ajouter et retourne 'True'.
        sinon la m�thode ne rien fait sauf de retourner 'False'.
        """
        etqs=list(set(lis_etq))
        if len(etqs)<1:#si on pas des transition
            return False,None
        for etat in list(self.automateD.Q):
            if len(set(list(etat.ens_etats))^set(etqs))==0:#si ont les m�mes �tiquettes.
                return False,etat.etiquette
        #print('***',etqs)
        x, y = randrange(EtatGraphe.rayon + 20, \
                         self.automateD.largeur * 7 // 8-EtatGraphe.rayon), randrange(EtatGraphe.rayon, \
                                                            self.automateD.hauteur-EtatGraphe.rayon)
        e=EtatGraphe(self.automateD, (x, y),None,initial,final)
        e.dessiner()
        e.ens_etats=etqs#ajouter les �tiquettes des auciennes �tats.
        return True,e.etiquette#retourne l'�tiquette du nouvelle �tat cr�er.
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def transformer(self,etq_etat,ens_etats):
        """
        c'est la m�thode qui transforme l'automate 'automateN'.
        au un automate FD, et le stock� dans l'objet 'automateD'.
        etq_etat: c'est l'�tiquette de l'�tat o� on se trouve.
        ens_etats: ensemble des �tats qu'il regroupe 
        """
        alp=set()
        alp.add(self.automateN.epsilon)
        lettres=list(self.automateN.A-alp)
        proch_iters=[]
        for a in lettres:
            list_ets=self.etats_vers_etats(ens_etats,a)
            etat=self.etats_cloture_etats(list_ets[1])
            final=False
            if len(set(etat[1])&self.automateN.F)>0:#si nv �tat contient au moins un �tat final du AFND.
                final=True
            etq=self.ajouter_etat(etat[0],False,final)#bool,etq/None
            #if final:
                #print("final",etq[1])
            if etq[1] is not None:
                if etq[0]!=FALSE:
                    self.ajouter_transition(etq_etat,str(etq[1]),a)
                    proch_iters.append([str(etq[1]),etat[1]])
                else:
                    self.ajouter_transition(etq_etat,str(etq[1]),a)
            #####
            print("***",etq_etat,"-->",etq[1],"***")
            print(self.get_etiquettes(ens_etats),"--",a,"-->",list_ets[0],"--{0}-->".format(self.automateN.epsilon),etat[0])

        if len(proch_iters)<1:
            return
        for ens in proch_iters:
            self.transformer(ens[0],ens[1])
 
#------------------------------------
    def get_etiquettes(self,ens_etats):
        """"""
        l=list()
        for etat in list(ens_etats):
          l.append(etat.etiquette)
        return l
        
