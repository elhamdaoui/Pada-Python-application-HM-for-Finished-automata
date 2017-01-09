# -*-coding:Latin-1 -*

#===============================================================================
__author__ = "abdelmajid"
__date__ = "$14 avr. 2015 03:24:08$"
__doc__="""
c'est un module qui contient tout ce qui concerne une transformation d'un
automate finis non détérministe (AFND), avec ou sans des états instantannées
(epsilon), à un automate fini détérministe (AFD).
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
            #ajouter qulq choses pour retourne au l'automate précédent
        self.automateN=automate#attention au référence. (fais une copie) !!
        self.automateD=AutoGraphe(self.automateN.master,self.automateN.largeur,self.automateN.hauteur)
        clt_ini=self.etats_cloture_etats(self.automateN.I)
        final=False
        if len(set(clt_ini[1])&set(self.automateN.F))>0:#si l'état initial du AFD,contient un état final du AFND
            final=True
        self.ajouter_etat(clt_ini[0],True,final)#état initial du nouveau automate
        print("############################################")
        print("####### algorithme de transformation #######")
        print("############################################")
        self.transformer('q0',clt_ini[1])
        print("############################################")

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def etats_vers_etats(self,ens_etats,lettre):
        """
        une méthode qui permette de déterminer (p') tel que:
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
        méthode qui permette de déterminer epsilon-clôture d'un etat (ens d'états)
        retourne [[ensembles des étiquettes],[ensemble des états]]
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
        méthode qui permette d'ajouter une transition au l'automate minimisé.
        s'elle est existée déjà, donc on l'a mis à jour.
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
        méthode qui permette d'ajouter un état s'il est non encore ajouter et retourne 'True'.
        sinon la méthode ne rien fait sauf de retourner 'False'.
        """
        etqs=list(set(lis_etq))
        if len(etqs)<1:#si on pas des transition
            return False,None
        for etat in list(self.automateD.Q):
            if len(set(list(etat.ens_etats))^set(etqs))==0:#si ont les mêmes étiquettes.
                return False,etat.etiquette
        #print('***',etqs)
        x, y = randrange(EtatGraphe.rayon + 20, \
                         self.automateD.largeur * 7 // 8-EtatGraphe.rayon), randrange(EtatGraphe.rayon, \
                                                            self.automateD.hauteur-EtatGraphe.rayon)
        e=EtatGraphe(self.automateD, (x, y),None,initial,final)
        e.dessiner()
        e.ens_etats=etqs#ajouter les étiquettes des auciennes états.
        return True,e.etiquette#retourne l'étiquette du nouvelle état créer.
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def transformer(self,etq_etat,ens_etats):
        """
        c'est la méthode qui transforme l'automate 'automateN'.
        au un automate FD, et le stocké dans l'objet 'automateD'.
        etq_etat: c'est l'étiquette de l'état où on se trouve.
        ens_etats: ensemble des états qu'il regroupe 
        """
        alp=set()
        alp.add(self.automateN.epsilon)
        lettres=list(self.automateN.A-alp)
        proch_iters=[]
        for a in lettres:
            list_ets=self.etats_vers_etats(ens_etats,a)
            etat=self.etats_cloture_etats(list_ets[1])
            final=False
            if len(set(etat[1])&self.automateN.F)>0:#si nv état contient au moins un état final du AFND.
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
        
