# -*-coding:Latin-1 -*
__author__ = "abdelmajid"
__date__ = "$7 avr. 2015 19:18:01$"

#===============================================================================
__doc__ = """
c'est le module qui contient tous ce qui concerne un etat
d'un automate tel que construction, dessin ...
les classes:
++Etat++ : c'est l'etat standard d'un automate (etiquette)
++EtatGraphe++ : c'est l'objet graphique qui repr�sente un �tat 'Forme
g�m�trique'.
"""
#===============================================================================
from tkinter import *
from random import randrange

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
class Etat:
    """
    c'est la classe qui repr�sente un �tat d'un automate.
    """
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def __init__(self, automate, etiquette=None, initial=False, final=False):
        self.automate = automate
        if etiquette is None:
            etiquette = 'q' + str(self.automate.nb_etats)
        self._etiquette = etiquette
        self._initial = initial
        self._final = final
        #-----------------------
        #c'est un attribut qui contient les �tiquettes des �tats d'un AFND, 
        #lorsqu'il est transform� en AFD.
        self.ens_etats = []
        #-----------------------
        self._set_etiquette(etiquette)
        self._set_initial(initial)
        self._set_final(final)
        if self not in self.automate.Q:
            self.automate.Q.add(self)#ajouter aux �tas de l'automate
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def _get_etiquette(self):
        """"""
        return str(self._etiquette)
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def _set_etiquette(self, etq):
        """
        m�thode qui permette de modifier l'etiquette d'�tat et donc
        modifier les esembles d'automate
        """
        
        if self._etiquette in self.automate.Auto:
            ligne = self.automate.Auto[self._etiquette]
            del self.automate.Auto[self._etiquette]
            self.automate.Auto[str(etq)] = ligne
        else:
            self.automate.Auto[str(etq)] = {}
        
        updates = []
        for etat, ligne in self.automate.Auto.items():
            for alphabet, listetat in ligne.items():
                for i in range(len(listetat)):
                    if listetat[i] == self._etiquette:
                        updates.append((etat, alphabet, i))
        for i, j, k in updates:
            self.automate.Auto[i][j][k] = str(etq)
            
        self._etiquette = str(etq)
        #dessin
        if type(self) is EtatGraphe:
            if self.text is not None:
                self.automate.toile.itemconfig(self.text, text=etq)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def _get_final(self):
        """"""
        return self._final

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def _set_final(self, state):
        """m�thode qui permette de modifier l'�tat (final) et l'automate aussi"""
        if state and self not in self.automate.F:
            self.automate.F.add(self)#ajouter l'�tat au les �tats finaux d'automate
        elif not state:
            st = set()
            st.add(self)
            st = self.automate.F-st#supprimer l'�tat de les �tats finaux d'automate
            self.automate.F = set(st)
        self._final = state
        #et on modifie quelque chose dans la repr�sentation graphique (dessin)
        if type(self) is EtatGraphe:
            if state:
                if self.cerclef is not None:
                    self.automate.toile.delete(self.cerclef)
                self.cerclef = self.automate.toile.create_oval(self.centre[0]-(self.rayon * 3 // 4), self.centre[1]-(self.rayon * 3 // 4), \
                                                               self.centre[0] + (self.rayon * 3 // 4), self.centre[1] + (self.rayon * 3 // 4), width=2, outline="#001111")
            else:
                if self.cerclef is not None:
                    self.automate.toile.delete(self.cerclef)
                    self.cerclef = None
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def _get_initial(self):
        """"""
        return self._initial

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def _set_initial(self, state):
        """m�thode qui permette de modifier l'�tat (initial) et l'automate aussi"""
        if state and self not in self.automate.I:
            self.automate.I.add(self)#ajouter l'�tat au les �tats initiaux d'automate
        elif not state:
            st = set()
            st.add(self)
            st = self.automate.I-st#supprimer l'�tat de les �tats initiaux d'automate
            self.automate.I = set(st)
        self._initial = state
        #et on modifie quelque chose dans la repr�sentation graphique (dessin)
        if type(self) is EtatGraphe:
            if state:
                if self.start is not None:
                    self.automate.toile.delete(self.start)
                self.start = self.automate.toile.create_line(self.centre[0]-self.rayon-20, self.centre[1], \
                                                             self.centre[0]-self.rayon, self.centre[1], width=3, arrow=LAST, fill='red')
            else:
                if self.start is not None:
                    self.automate.toile.delete(self.start)
                    self.start = None
                    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    #les propri�t�s des instances
    initial = property(_get_initial, _set_initial)
    final = property(_get_final, _set_final)
    etiquette = property(_get_etiquette, _set_etiquette)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def cloture(self):
        """
        la m�thode qui permette de retourner le epsilon-cl�ture du l'�tat courant.
        sous forme de deux liste l'une contient les �tiquettes et l'autre les �tats (Etat).
        """
        clot = list()
        clot.append(list());clot.append(list())
        clot[0].append(self.etiquette)#ajouter �tq d'etat
        #s'il existe une transtion instantan� (lit le vide (epsilon)) de cette �tat vers d'autres �tats 
        if self.automate.epsilon in self.automate.Auto[self.etiquette].keys():
            lis = self.automate.Auto[self.etiquette][self.automate.epsilon].copy()
            clot[0] += list(set(lis))#on ajoute ces �tats
            #on parcourir cette liste des �tats .pour ajouter les autres transition instantan�es.
            while(len(lis) > 0):
                lis2 = []
                for etat in lis:
                    if self.automate.epsilon in self.automate.Auto[etat].keys():
                        lisclot = self.automate.Auto[etat][self.automate.epsilon]
                        lis2 += lisclot
                #donc lis2 contient l'ensemble des �tats o� il ya des transition instantan�es.
                #on det�rmines l'ensembles �tats (epsilon-cl�ture) non encore trait�s
                lis = list(set(lis2)-set(clot[0]))
                #on ajoute les nouveaux �tats.
                clot[0] = list(set(clot[0] + lis2))
        lis = list()
        for e in clot[0]:
            lis.append(self.automate.get_etat(e))
        clot[1] = lis
        return clot

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def lit_lettre(self, lettre):
        """
        une m�thode qui permette de retourner les �tats d'arriv�s possibles
        lorsque l'automate lit la lettre .
        pi------lettre---->p'={ei,...}
        """
        lis, lise = [], []
        if lettre in self.automate.Auto[self.etiquette].keys():
            lis = self.automate.Auto[self.etiquette][lettre].copy()
            lis = list(set(lis))
            for e in lis:
                lise.append(self.automate.get_etat(e))
        return [lis, lise]
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 

#===============================================================================
class EtatGraphe(Etat):
    """
    c'est la classe qu'on va utiliser dans notre application
    elle repr�sente un �tat d'automate 
    """
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    rayon = 25#attribut de classe 

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def __init__(self, automate, centre=None, etiquette=None, initial=False, final=False):
        """
        l'initialisateur du classe.
        """
        self.centre = tuple([0,0])#liste de deux �l�ments qui contient les cordo�es.
        self.cercle = None#le numero du cercle d'etat dans le canvas
        self.cerclef = None#le numero du cercle 'final' d'etat dans le canvas
        self.start = None#le numero du fleche de start d'etat dans le canvas
        self.text = None#le numero du texte 'etiquette etat' d'etat dans le canvas
        self.rect_ens_etats = None#le numero du rectangle qui contient le texte (ens_etats)
        self.text_ens_etats = None#le numero du  le texte (ens_etats)
        self.transDepart = []#les transitions qui ont cet �tat comme point de d�part
        self.transFin = []#les transitions qui ont cet �tat comme point final
        super().__init__(automate, etiquette, initial, final)
        if centre is None:
            self.set_centre()
        else:
            self.centre = tuple(centre)
        #!!! attetion le constructeur du classe M�re est obligatoirement declar�
        #apres les nouveau attribut il a besoins a (self.start et self.text et 
        #self.cerclef) par exemple.
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def actualiser(self):
        """
        une m�thode qui permette d'actualiser un �tat
        """
        self.transDepart = list(set(self.transDepart) & self.automate.Transitions)
        self.transFin = list(set(self.transFin) & self.automate.Transitions)
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>         
    def dessiner(self):
        """
        une m�thode qui permmette de dessiner l'�tat
        """
        self.actualiser()
        if self.cercle is not None:
            self.automate.toile.delete(self.cercle)
        if self.cerclef is not None:
            self.automate.toile.delete(self.cerclef)
        if self.start is not None:
            self.automate.toile.delete(self.start)
        if self.text is not None:
            self.automate.toile.delete(self.text)
        if self.text_ens_etats is not None:
            self.automate.toile.delete(self.text_ens_etats)
        if self.rect_ens_etats is not None:
            self.automate.toile.delete(self.rect_ens_etats)
        #notez que les transition doivent etre dissiner d'abord
        self.cercle = self.automate.toile.create_oval(self.centre[0]-self.rayon, self.centre[1]-self.rayon, \
                                                      self.centre[0] + self.rayon, self.centre[1] + self.rayon, width=2, fill='#95F7B7', outline="#001111")
        if self.final:
            self.cerclef = self.automate.toile.create_oval(self.centre[0]-(self.rayon * 3 // 4), self.centre[1]-(self.rayon * 3 // 4), \
                                                           self.centre[0] + (self.rayon * 3 // 4), self.centre[1] + (self.rayon * 3 // 4), width=2, outline="#001111")
        if self.initial:
            self.start = self.automate.toile.create_line(self.centre[0]-self.rayon-20, self.centre[1], \
                                                         self.centre[0]-self.rayon, self.centre[1], width=3, arrow=LAST, fill='red')
        if len(self.ens_etats) > 0:
            texte_ens = ",".join(self.ens_etats)
            x1, y1 = self.centre[0]-10, self.centre[1] + self.rayon
            x2, y2 = self.centre[0]+10, self.centre[1] + self.rayon + 20
            length = (len(",".join(texte_ens))-4) // 2
            x1, x2 = x1-length * 3, x2 + length * 3
            self.rect_ens_etats = self.automate.toile.create_rectangle(x1, y1, x2, y2, outline='blue', fill='light green')
            self.text_ens_etats = self.automate.toile.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=texte_ens, fill='brown')
        self.text = self.automate.toile.create_text(self.centre[0], self.centre[1], text=self.etiquette, anchor=CENTER)
        for trans in self.transDepart:
            trans.dessiner()
        for trans in self.transFin:
            trans.dessiner()
      
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def supprimer(self):
        """
        m�thode qui permette de supprimer l'�tat du canvas est d'automate
        """
        """
        if self.cercle is not None:
            self.automate.toile.delete(self.cercle)
            print("supp_cercle",self.cercle)
        if self.cerclef is not None:
            self.automate.toile.delete(self.cerclef)
            print("supp_cerclef")
        if self.start is not None:
            self.automate.toile.delete(self.start)
            print("supp_start")
        if self.text is not None:
            self.automate.toile.delete(self.text)
            print("supp_text",self.text)
        if self.rect_ens_etats is not None:
            self.automate.toile.delete(self.rect_ens_etats)
            print("supp_rect_ens_etats")
        if self.text_ens_etats is not None:
            self.automate.toile.delete(self.text_ens_etats)
            print("supp_text_ens_etats")
        """
        trse=set(self.transFin + self.transDepart)
        self.automate.Transitions = self.automate.Transitions-trse
        for tr in list(trse):
            tr.supprimer()
        
        try:
            self.automate.Q.remove(self)
            if self.initial:
                self.automate.I.remove(self) 
            if self.final:
                self.automate.F.remove(self)
            del self.automate.Auto[self.etiquette]
        except:
            print("Erreur: suppression erron�e ,�tat non existe")
        #supprimer l'etat du table de transition d'automate
        for etat, ligne in self.automate.Auto.items():
            for alphabet, listetat in ligne.items():
                st = set(listetat)
                st = st-set(self.etiquette)
                self.automate.Auto[etat][alphabet] = list(st)
        self.automate.actualiser()

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def set_centre(self, x=None, y=None):
        """
        m�thode qui permette d'ajouter le centre d'etat s'il est sp�cifi�,
        sinon on ajoute un centre al�atoire qui respecte les conditions.
        """
        if x is None:
            x = randrange(EtatGraphe.rayon + 20, \
                          self.automate.largeur * 7 // 8-EtatGraphe.rayon)
        if y is None:
            y = randrange(EtatGraphe.rayon, \
                          self.automate.hauteur-EtatGraphe.rayon)
        self.centre=(x,y)
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def contient_point(self, x, y):
        """
        m�thode qui permette de verifier si u point est � l'int�rieur d'�tat
        """
        if self.centre[0]-self.rayon <= x <= self.centre[0] + self.rayon and self.centre[1]-self.rayon <= y <= self.centre[1] + self.rayon:
            return True
        return False
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def __repr__(self):
        """"""
        return self.etiquette + "/" + str(self.centre)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def get_dictionnaire(self):
        """
        m�thode qui permette de retourner un dictionnaire qui contient les attributs. 
        """
        return {
        "etiquette":self.etiquette,
        "initial":self.initial,
        "final":self.final,
        "centre":tuple(self.centre),
        "ens_etats":self.ens_etats.copy()
        }
    