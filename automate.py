# -*-coding:Latin-1 -*

__author__ = "abdelmajid"
__date__ = "$7 avr. 2015 02:31:42$"

#===============================================================================
__doc__ = """
c'est le module qui contient notre programme qui va traiter un automate
finis détérministe ou bien non detérministe avec ou sans ep-transitions.
"""
#===============================================================================
from etat import *
from random import randrange
from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import askstring
from transition import *


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
class Automate:
    """
    c'est la classe qui représente un automate
    """
    epsilon = '£'
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def __init__(self):
        """
        initialisateur d'un automate
        """
        self._nb_etats = -1#le nombre d'états créer
        self.A = set()#l'ensemble des alphabets (:str)
        self.Q = set()#l'ensemble des états (:EtatGraphe)
        self.F = set()#l'ensemble des états finaux (:EtatGraphe)
        self.I = set()#l'ensemble des états initiaux (:EtatGraphe)
        self.Transitions = set()#l'ensemble des transitions (:TransitionGraphe)
        self.Auto = {}#table de transitions
        #================T=============
        #{
        #'0':{'a':['1','2'],'b':['0'],'c':[]},
        #'1':{'a':['2'],'b':[],'c':['1','2']},
        #'2':{'a':['2','0'],'b':[],'c':[]}
        #}
        #==============================
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    
    def _get_nb_etats(self):
        """"""
        self._nb_etats += 1
        return self._nb_etats
    
    def _set_nb_etats(self, nb):
        """"""
        self._nb_etats = nb
    
    nb_etats = property(_get_nb_etats, _set_nb_etats)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    
    def est_deterministe(self):
        """
        méthode qui permette de vérifier, si u automate est déterministe ou non.
        retourne:: bool.
        """
        if len(self.Q) < 1 or len(self.F) < 1 or len(self.I) < 1:
            return False
        for ligne in self.Auto.values():
            for liste_etats in ligne.values():
                if len(liste_etats) > 1:
                    return False
        if self.epsilon in list(self.A):
            return False
        return True

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    
    def get_etat(self, etq):
        """
        méthode qui permette de retourner l'état par son étiquette.
        """
        for etat in list(self.Q):
            if etat.etiquette == etq:
                return etat
        return None
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    
    def actualiser(self):
        """"""
        #actualiser l'ensemble d'alphabet de l'automate
        alph = set()
        for ligne in self.Auto.values():
            alph = alph | set(ligne.keys())#ajouter les alphabets d'un état
        self.A = alph#maintenant les alphabets d'automate est seul qui ont éxistés dans Auto.

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def est_complet(self, affiche_info=False):
        """
        une méthode qui permette de vérifier si l'automate déterministe ou non.
        """
        rebuts = []
        for etat in list(self.Q):
            print("--", etat.etiquette)
            for a in list(self.A):
                print("--", etat.etiquette, "---", a)
                if a not in self.Auto[etat.etiquette].keys():
                    self.Auto[etat.etiquette][a] = []
                    rebuts.append((etat.etiquette, a))
                elif len(self.Auto[etat.etiquette][a]) < 1:
                    rebuts.append((etat.etiquette, a))
        rebuts = list(set(rebuts))
        if affiche_info:
            if len(rebuts) < 1:
                showinfo("automate complet", "cet automate est complet.")
        return rebuts
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def completer(self, affiche_info=True):
        """
        une méthode qui permette de completer un automate. s'il est incomplet.
        càd permette d'un état rebut.
        le paramétre ',affiche_info' permette d'afficher une information 
        dans un boit de dialogue signifie que l'automate est complet.
        """        
        rebuts = self.est_complet(affiche_info)
        if len(rebuts) > 0:
            x, y = randrange(EtatGraphe.rayon + 20, \
                             self.largeur * 7 // 8-EtatGraphe.rayon), randrange(EtatGraphe.rayon, \
                                                  self.hauteur-EtatGraphe.rayon)
            etat_rebut = EtatGraphe(self, (x, y), 'rebut')#l'ajout d'état rebut.
            for a in list(self.A):
                lts = set()
                lts.add(a)
                for tr in list(self.Transitions):
                    if tr.etatDepart is etat_rebut and tr.etatFin is etat_rebut:
                        lts = lts | tr.lettres
                        tr.lettres = lts
                        break
                else:TransitionGraphe(self, etat_rebut, etat_rebut, lts)#lorsque break du for n'est pas executer.
            for couple in rebuts:
                etat1 = self.get_etat(couple[0])
                lts = set()
                lts.add(couple[1])
                for tr in list(self.Transitions):
                    if tr.etatDepart is etat1 and tr.etatFin is etat_rebut:
                        lts = lts | tr.lettres
                        tr.lettres = lts
                        break
                else:TransitionGraphe(self, etat1, etat_rebut, lts)#lorsque break du for n'est pas executer.                
            etat_rebut.dessiner()
            
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def a_reconnu_mot(self, mot):
        """
        une méthode qui permette de vérifier si un mot est reconnu ou non
        par cet automate.
        """
        if len(self.I) < 1 or len(self.F) < 1:
            return "autome a besion des états initiaux et acceptants."
        etats = [etat.etiquette for etat in list(self.Q)]
        etat_i = list(self.I)[0].etiquette
        etats_f = [etat.etiquette for etat in list(self.F)]
        alphabet = list(self.A)
        if len(mot) == 0:
            if etat_i in etats_f:
                return True
            return False
        alphs_non_reconnu = set(mot)-self.A
        if len(alphs_non_reconnu) > 0:
            return "le mot contient les lettres '" + ",".join(list(alphs_non_reconnu)) + "' qui sont hors d'alphabet."#mot contient des lettres hors d'alphabet.
        return self.reconnu_mot(etats, etats_f, alphabet, etat_i, mot)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def reconnu_mot(self, etats, etats_f, alphabet, etat, mot):
        """
        méthode récursive qui utilier par la méthode 'a_reconnu_mot'.
        """
        if len(mot) == 0:
            if etat in etats_f:
                return True
            return False
        a = mot[0]#la 1ere lettre du mot.
        mot = mot[1:]#empiler la première lettre du mot.
        if etat not in self.Auto.keys()\
            or a not in self.Auto[etat].keys()\
                or len(self.Auto[etat][a]) == 0:
                    return False
        etats_a = self.Auto[etat][a]#l'ensemble des états d'arrivés de la transition partant d'etat et portant la lettre a.
        if len(mot) == 0:#si la lettre et la dérinère.
            if len(set(etats_a) & set(etats_f)) > 0:#si l'auto trouvant dans un état final.
                return True
            else:
                return False
        val_retourner = False
        for etat in etats_a:
            val_retourner = val_retourner or self.reconnu_mot(etats, etats_f, alphabet, etat, mot)
        return val_retourner
            
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
#===============================================================================
class AutoGraphe(Automate, PanedWindow):
    """
    c'est une classe (widget) qui représete un automate .
    attributs:
    toile: Canvas qui permette de dessiner une représentation graphique d'automate.
    des bouttons pour les choix de dessin.
    """
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def __init__(self, master=None, largeur=500, hauteur=400):
        """
        initialisateur du classe 
        """
        PanedWindow.__init__(self, master, orient=HORIZONTAL, width=largeur, height=hauteur, bg='black')
        Automate.__init__(self)
        
        self.largeur, self.hauteur = largeur, hauteur
        self.frame = Frame(self, bg='light yellow', height=hauteur)
        self.toile = Canvas(self.frame, height=hauteur, relief='ridge', bd=2, bg='white')
        self.choix_dessin = 'editer' #attribut porte le texte du boutton clické
        self.defaires = []#liste utiliser par le boutton 'Défaire'.
        self.refaires = []#liste utiliser par le boutton 'Refaire'.
        self.re_de_faires = []#liste utiliser par les bouttons 'Refaire' et 'Défaire'.
        self.index = 0#l'index dans la liste re_de_faires
        self.click1 = None#
        self.click2 = None#
        self.forme_mouse_motion = None
        self.update_etat = None#le num du frame 'modifier un etat' dans le canvas 'self.toile'
        self.pane_btns = PanedWindow(self, opaqueresize=1, sashcursor='', width=largeur * 1 // 8, \
                                     showhandle=1, handlesize=0, handlepad=1, \
                                     sashrelief='sunken', sashpad=1, sashwidth=1, \
                                     orient=VERTICAL, relief='ridge', bd=2, bg='#5FBCA3')
        texts = ["editer", "etat", "transition", "supprimer", "undo", "redo", "vider"]
        crs = ["arrow", "tcross", "target", "pirate", "hand1", "hand1", "hand2"]
        imgs = ["imgs/config.png", "imgs/etat.png", "imgs/trans.png", "imgs/drop.png", "imgs/undo.png", "imgs/redo.png", "imgs/vider.png"]
        self.btns = []
        for i in range(len(texts)):
            #b = Button(self.pane_btns, text=texts[i], relief='groove', bg='#0B1577', cursor=crs[i], fg='white', height=4)
            img = PhotoImage(file=imgs[i], master=self.pane_btns)
            b = Button(self.pane_btns, text=texts[i], relief='groove', image=img, bg='#0B1577', cursor=crs[i], fg='white', width=largeur * 1 // 8, height=hauteur // 7-9)
            b.image = img
            self.btns.append(b)
            #b.grid(row=i, sticky=N + W + S + E, ipady=5, pady=2, ipadx=1, padx=1)
            self.pane_btns.add(b, pady=0)
            b.bind("<Button-1>", self.click_btn)
        self.toile.bind("<Button-1>", self.click_toile)
        self.toile.bind("<B1-Motion>", self.mouse_motion_toile)
        self.toile.bind("<ButtonRelease>", self.btn1_lacher)
        self.toile.bind("<Button-3>", self.click_btn_droite_toile)
        #====ajoute des bares de difilements
        """scroll = Scrollbar(self.frame, orient =VERTICAL, command=self.toile.yview,width=2)
        scrollw = Scrollbar(self.frame, orient =HORIZONTAL, command=self.toile.xview,width=5)
        self.toile.configure(scrollregion =(0, 0, self.largeur, self.hauteur),\
        yscrollcommand=scroll.set,xscrollcommand=scrollw.set)
        scroll.pack(side=RIGHT,expand =NO,fill=Y)
        scrollw.pack(side=BOTTOM,expand =NO,fill=X)"""
        #====
        self.toile.pack(padx=0, pady=0, expand=1, fill=BOTH)
        self.add(self.pane_btns)
        self.add(self.frame)
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def click_btn(self, event):
        """gestionnaire d'événemet click dur btn"""
        self.choix_dessin = event.widget['text']
        for btn in self.btns:
            btn['bg'] = '#0B1577'
        event.widget['bg'] = "#F56925"
        self.toile['cursor'] = event.widget['cursor']
        if self.choix_dessin == 'vider':
            if askyesno("confirmation", "étes-vous sûr de recommencer\n\
            la construction de cet automate ?", parent=self):
            #if True:
                self.vider()
                self.click1 = self.click2 = self.forme_mouse_motion = None
        elif self.choix_dessin in ['undo','redo']:
            ln_lis = len(self.re_de_faires)
            #print("on a --- ",ln_lis,"-index-->",self.index)
            if ln_lis > 0 and 0 <= self.index < ln_lis:
                op = self.re_de_faires[self.index]
                #print(op)
                if op[0] == 'ajout_etat':
                    eta = self.ajouter_etat_par_dict(op[1])
                    if eta is not None:
                        self.re_de_faires[self.index] = ['supp_etat', eta]  
                elif op[0] == 'ajout_trans':
                    trs = self.ajouter_transition_par_dict(op[1])
                    if trs is not None:
                        self.re_de_faires[self.index] = ['supp_trans', trs]
                elif op[0] == 'supp_trans':
                    dic = op[1].get_dictionnaire()
                    op[1].supprimer()
                    self.re_de_faires[self.index] = ['ajout_trans', dic]
                elif op[0] == 'supp_etat':
                    dic = op[1].get_dictionnaire()
                    op[1].supprimer()
                    self.re_de_faires[self.index] = ['ajout_etat', dic]
                    self.dessiner()
                
            if self.choix_dessin=='undo' and self.index<ln_lis:
                self.index += 1
            elif self.choix_dessin=='redo' and self.index>=0:
                self.index -= 1
        
            
        
            
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def click_toile(self, event):
        """
        géstionnaire d'événement de click sur la toile
        """
        x, y = event.x, event.y
        text = self.choix_dessin
        if self.update_etat is not None:#si une boite de modification d'un état est dans 'canvas'
            self.toile.delete(self.update_etat)
            self.update_etat = None
        if text == 'etat':
            eta = EtatGraphe(self, (x, y))
            eta.dessiner()
            self.re_de_faires.insert(self.index, ['supp_etat', eta])
        elif text in ['transition', 'editer']:
            for etat in list(self.Q):
                if etat.contient_point(x, y):
                    self.click1 = etat#pour editer et transition
                    #print(etat.get_dictionnaire())
                    if text == 'transition':
                        self.forme_mouse_motion = self.toile.create_line(x, y, x, y, fill="blue", width=2, arrow=LAST)
                    
        elif text == 'supprimer':
            for etat in list(self.Q):
                if etat.contient_point(x, y):
                    self.re_de_faires.insert(self.index, ['ajout_etat', etat.get_dictionnaire()])
                    etat.supprimer()
                    self.dessiner()
                    return
            for tr in list(self.Transitions):#si je parcouris 'self.Trasitions' type='Set' donc une Exception 'RunTime' sera levé !!. 
                if tr.contient_point(x, y):
                    #print(tr.get_dictionnaire())
                    self.re_de_faires.insert(self.index, ['ajout_trans', tr.get_dictionnaire()])
                    tr.supprimer()
                    self.dessiner()
                    
        elif text == 'undo':
            print("============automate======")
            print("A:", self.A)
            print("Q:", self.Q)
            print("I:", self.I)
            print("F:", self.F)
            print("Trans:", self.Transitions)
            print("Auto:", self.Auto)
        elif text == 'redo':
            print("redissiner")
            self.dessiner()
            #print(self.get_dictionnaire_simplifie())
            #--------------
            
                        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def mouse_motion_toile(self, event):
        """
        géstionnaire d'événement du 'mouvement du souris avec click du Boutton gauche sur la toile' 
        """
        x, y = event.x, event.y
        text = self.choix_dessin
        if text == 'transition':
            if type(self.click1) is EtatGraphe and self.forme_mouse_motion is not None:
                self.toile.coords(self.forme_mouse_motion, \
                                  self.click1.centre[0], self.click1.centre[1], x, y)
        if text == 'editer':
            if type(self.click1) is EtatGraphe:
                if x<EtatGraphe.rayon:
                    x=EtatGraphe.rayon
                if x>self.largeur-EtatGraphe.rayon:
                    x=self.largeur-EtatGraphe.rayon
                if y<EtatGraphe.rayon:
                    y=EtatGraphe.rayon
                if y>self.hauteur-EtatGraphe.rayon:
                    y=self.hauteur-EtatGraphe.rayon
                self.click1.centre = (x, y)
                self.click1.dessiner()
                
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def btn1_lacher(self, event):
        """
        géstionnaire d'événement ' lacher le boutton gauche du souris sur la toile '
        """
        x, y = event.x, event.y
        text = self.choix_dessin
        if text == 'transition':
            if  type(self.click1) is EtatGraphe and self.forme_mouse_motion is not None:
                for etat in list(self.Q):
                    if etat.contient_point(x, y):
                        self.click2 = etat
                        break
                if type(self.click2) is EtatGraphe:
                    #verifier si cette transition est déjà existe
                    #car on fait une et une seule transition etre deux états (ou bien un état :transitio reflexive)
                    for tr in list(self.Transitions):
                        if tr.etatDepart is self.click1 and tr.etatFin is self.click2:
                            t = tr
                            break#si on sort grace à cette instruction donc on passe pas par else.
                    else:
                        t = TransitionGraphe(self, self.click1, self.click2)
                        t.dessiner()
                        self.re_de_faires.insert(self.index, ['supp_trans', t])
                    t.entrer_lettres()
                    
                
                if self.forme_mouse_motion is not None:
                    self.toile.delete(self.forme_mouse_motion)
                self.click1 = self.click2 = self.forme_mouse_motion = None
        if text == 'editer':
            self.click1 = None
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def click_btn_droite_toile(self, event):
        """
        géstionnaire d'événement d'un click de boutton droit de la souris.
        """
        x, y = event.x, event.y
        if self.update_etat is not None:
            self.toile.delete(self.update_etat)
            self.update_etat = None
        for etat in list(self.Q):
            if etat.contient_point(x, y):
                fen = UpdateEtat(self.toile, etat)
                self.update_etat = self.toile.create_window(x + fen.largeur // 2, y + fen.hauteur // 2, window=fen)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def dessiner(self):
        """
        méthode qui permette de dissiner un automate
        """
        self.toile.delete(ALL)
        for etat in list(self.Q):
            etat.dessiner()

       
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def get_dictionnaire_simplifie(self):
        """
        méthode qui permette de retourne un dictionnaire simplifié qui defini
        l'automate.
        """
        d = {"etats":[], "transitions":[], "nb_etats":self._nb_etats, \
        "largeur":self.largeur, "hauteur":self.hauteur}
        for etat in list(self.Q):
            d['etats'].append(etat.get_dictionnaire())
        for tr in list(self.Transitions):
            d['transitions'].append(tr.get_dictionnaire())
        return d
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def dict_to_automate(cls, fenetre, dic, activer_exception=False):
        """
        méthode de classe qui permette de construire un automate à partir de 
        son dictionnaire simplifié.
        """
        largeur, hauteur = 700, 600
        try:
            if "largeur" in dic.keys():
                largeur = int(dic['largeur'])
            if "hauteur" in dic.keys():
                hauteur = int(dic['hauteur'])
            auto = AutoGraphe(fenetre, largeur, hauteur)
            if len(set(['etats', 'transitions', 'nb_etats'])-set(dic.keys())) == 0:
                for etat in dic["etats"]:
                    nve = EtatGraphe(auto, centre=tuple(etat['centre']), \
                                     etiquette=etat['etiquette'], initial=etat['initial'], final=etat['final'])
                    nve.ens_etats = list(etat['ens_etats'])
                for tr in dic["transitions"]:
                    TransitionGraphe(auto, etatDepart=auto.get_etat(tr['etq_d']), \
                                     etatFin=auto.get_etat(tr['etq_f']), lettres=set(tr['lettres'].copy()))
                auto._nb_etats = dic['nb_etats']
            elif activer_exception:
                raise KeyError
                return None
        except:
            return None
        return auto
        

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    dict_to_automate = classmethod(dict_to_automate)
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def copie(self, fenetre):
        """
        une méthode qui permette de retourner une copie de l'automate.
        """
        dic = self.get_dictionnaire_simplifie()
        auto = AutoGraphe.dict_to_automate(fenetre, dic, activer_exception=False)
        auto.dessiner()
        #auto.pack()
        return auto
 
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def vider(self):
        """
        une méthode qui permette de vider l'automate.
        """
        self.toile.delete(ALL)
        self.A = set()
        self.Q = set()
        self.I = set()
        self.F = set()
        self.Auto = {}
        self.Transitions = set()
        self.nb_etats = -1
        self.re_de_faires=list()
        self.index=0
 
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def fermeture_transitive(cls, automate):
        """
        une méthode de classe qui permette de retourner un automate 
        représente la fermeture transitive d'un autre automate.
        l'automate obtenu s'affiché dans une nouvelle fenetre.
        """
        if type(automate) is not AutoGraphe:
            showwarning("erreur", "on peut pas faire la fermutre transitive que pour un automate.")
            return
        if len(automate.I) < 1 or len(automate.F) < 1:
            showwarning("automte non défini", "l'automate a besion d'au moins un état initial et final.", parent=automate)
            return
        if len(automate.I) == len(automate.F) == 1 and list(automate.I)[0] is list(automate.F)[0]:
            showwarning("automte transitive", "cet automate est une fermeture transitive.", parent=automate)
            return
        auto = automate.copie(automate.master)
        xi, yi = 30 + list(auto.I)[0].rayon, auto.hauteur // 2
        etat_if = EtatGraphe(auto, (xi, yi))
        #transitions instantanées partant de nv état à chaque état initial.
        for etat in list(auto.I):
            TransitionGraphe(auto, etat_if, etat).dessiner()
            etat.initial = False
        etat_if.initial = True#nv etat devenu le seul état initial.
        #transitions instantanées partant de chaque état final au nouveau état.
        for etat in list(auto.F):
            TransitionGraphe(auto, etat, etat_if).dessiner()
            etat.final = False
        etat_if.final = True#nv etat devenu le seul état final.
        etat_if.dessiner()
        auto.master.nouveau_automate(auto, "férmeture transitive de [" + automate.master.nom + "]")#lancer la nv fenetre.
    #definir une méthode de classe
    fermeture_transitive = classmethod(fermeture_transitive)
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def concatener(cls, automate1, automate2, title=None):
        """
        une méthode de classe qui permette de retourner un automate 
        représente la concaténation du deux automates passés en paramères.
        l'automate obtenu s'affiché dans une nouvelle fenetre.
        """
        if type(automate1) is not AutoGraphe or type(automate2) is not AutoGraphe:
            showwarning("erreur", "on ne peut concatener que deux automates.", parent=automate1)
            return
        if len(automate1.I) < 1 or len(automate1.F) < 1 or len(automate2.I) < 1 or len(automate2.F) < 1:
            showwarning("automtes non définis", "les automates ont besion d'au moins un état initial et final.", parent=automate1)
            return
        auto1 = automate1.copie(automate1.master)
        auto2 = automate2.copie(automate2.master)
        etats_i2 = []#liste pour stocker les états initiaux d'automate 2 dans le nv automate.
        etats_f1 = list(auto1.F).copy()#liste des états final d'automate 1.
        #ajouter tous les étas d'automate 2 au copie d'automate 1.
        for etat in list(auto2.Q):
            e = EtatGraphe(auto1, tuple(etat.centre), etat.etiquette + "'", False, etat.final)
            if etat.initial:
                etats_i2.append(e)
        #ajouter tous les transitions d'automate 2 au copie d'automate 1.
        for tr in list(auto2.Transitions):
            TransitionGraphe(auto1, auto1.get_etat(tr.etatDepart.etiquette + "'"), \
                             auto1.get_etat(tr.etatFin.etiquette + "'"), tr.lettres.copy())
        for etati in etats_i2:
            etati.initial = False
            for etatf in etats_f1:
                etatf.final = False
                TransitionGraphe(auto1, etatf, etati)
        #lancer une nouvelle fenetre avec l'automate réunion.
        auto1.master.nouveau_automate(auto1, title)
    #definir une méthode de classe
    concatener = classmethod(concatener)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def reunion(cls, automate1, automate2, title=None):
        """
        une méthode de classe qui permette de retourner un automate 
        représente la réunion du deux automates passés en paramères.
        l'automate obtenu s'affiché dans une nouvelle fenetre.
        """
        if type(automate1) is not AutoGraphe or type(automate2) is not AutoGraphe:
            showwarning("erreur", "on ne peut faire la réunion que à deux automates.", parent=automate1)
            return
        if len(automate1.I) < 1 or len(automate1.F) < 1 or len(automate2.I) < 1 or len(automate2.F) < 1:
            showwarning("automtes non définis", "les automates ont besion d'au moins un état initial et final.", parent=automate1)
            return
        auto1 = automate1.copie(automate1.master)
        auto2 = automate2.copie(automate2.master)
        etats_i = list(auto1.I)#liste pour stocker les états initaiux de deux automates.
        n = len(etats_i)
        #ajout des états d'automate é
        for etat in list(auto2.Q):
            e = EtatGraphe(auto1, tuple(etat.centre), etat.etiquette + "'", False, etat.final)
            if etat.initial:
                etats_i.append(e)
        #ajouter tous les transitions d'automate 2 au copie d'automate 1.
        for tr in list(auto2.Transitions):
            TransitionGraphe(auto1, auto1.get_etat(tr.etatDepart.etiquette + "'"), \
                             auto1.get_etat(tr.etatFin.etiquette + "'"), tr.lettres.copy())
        #les initiaux devient des états normaux,et ajout nv état initial avec leur transitions instantanées.
        xi = (etats_i[0].centre[0] + etats_i[n].centre[0]) // 2
        yi = (etats_i[0].centre[1] + etats_i[n].centre[1]) // 2
        etat_initial = EtatGraphe(auto1, (xi, yi), "qi''", True)
        for ei in etats_i:
            ei.initial = False
            TransitionGraphe(auto1, etat_initial, ei)
        #lancer une nouvelle fenetre avec l'automate réunion.
        auto1.master.nouveau_automate(auto1, title)
    #definir une méthode de classe
    reunion = classmethod(reunion)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def ajouter_etat_par_dict(self, dic):
        """
        ajouter un état par son dictionnaire.
        j'atoute cette méthode spécifiquement pour les traitements
        des boutons 'Défaire' et 'Refaire'.
        """
        if len(set(['etiquette', 'initial', 'final', 'centre', 'ens_etats'])-set(dic.keys())) == 0:
            if self.get_etat(dic['etiquette']) is None:
                e = EtatGraphe(self, \
                               centre=dic['centre'], \
                               etiquette=dic['etiquette'], \
                               initial=dic['initial'], \
                               final=dic['final'])
                e.dessiner()
            return e
        return None
            
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def ajouter_transition_par_dict(self, dic):
        """
        ajouter une transition par son dictionnaire.
        j'atoute cette méthode spécifiquement pour les traitements
        des boutons 'Défaire' et 'Refaire'.
        """
        if len(set(['etq_d', 'etq_f', 'lettres'])-set(dic.keys())) == 0:
            etatd, etatf = self.get_etat(dic['etq_d']), self.get_etat(dic['etq_f'])
            if etatd is not None and etatf is not None:
                t = TransitionGraphe(self, etatDepart=etatd, etatFin=etatf, lettres=dic['lettres'])
                t.dessiner()
                return t
        return None
    
#===============================================================================
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
class UpdateEtat(Frame):
    """
    class (widget) qui permette de modifier un etat
    """

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def __init__(self, master, etat):
        """
        initialisateur de la classe
        """
        super().__init__(master)
        self.config(relief='ridge', bd=3, bg='light green', width=100, height=120)
        self.largeur, self.hauteur = 100, 120
        self.etat = etat#l'état qui sera modifiée
        self.initText, self.finText = BooleanVar(etat.automate), BooleanVar(etat.automate)#pour les bouttons radios
        self.initText.set(etat.initial)#crocher ou decrocher le btn radio suivant l'état initial
        self.finText.set(etat.final)#crocher ou decrocher le btn radio ()
        Checkbutton(self, text="initial", variable=self.initText, command=self.act_initial, anchor=W).grid(row=0, sticky=N + E + S + W, padx=1, pady=2)
        Checkbutton(self, text="final", variable=self.finText, command=self.act_final, anchor=W).grid(row=1, sticky=N + E + S + W, padx=1, pady=2)
        Button(self, text='changer nom', command=self.act_changer_nom, anchor=W).grid(row=2, sticky=N + E + S + W, padx=1, pady=2)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def act_initial(self):
        """
        modifier l'initialité d'état.
        """
        self.etat.initial = self.initText.get()

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def act_final(self):
        """
        modificaion du finalité d'état.
        """
        self.etat.final = self.finText.get()

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def act_changer_nom(self):
        """
        modifier le nom (etiquette) d'état
        """
        if self.etat.automate.update_etat is not None:
            self.etat.automate.toile.delete(self.etat.automate.update_etat)
            self.etat.automate.update_etat = None
        b = askstring("modification d'état", "entrer la nouvelle libelé pour cet état.", parent=self)
        if b is not None and b != self.etat.etiquette:
            etqs = [etat.etiquette for etat in self.etat.automate.Q]
            if b in etqs:
                showwarning("nom non accepté", "ce nom est réservé pour un autre état,\
                \nvous étes pas le droit de nommmer deux états avec même nom\
                \nbien que ça n'a aucune importance théorique.")
                return
            self.etat.etiquette = b
    
