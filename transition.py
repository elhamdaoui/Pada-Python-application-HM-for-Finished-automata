# -*-coding:Latin-1 -*

__author__ = "abdelmajid"
__date__ = "$7 avr. 2015 19:18:20$"

#===============================================================================
__doc__ = """
c'est le module qui contient tout ce qui concere d'une transition 
d'un état à l'autre avec une lettre .
[[ l'automate trouvant dans l'état 'qi' lire l'alphabet 'a' et transit 
vers l'état 'qj' ]].
les classes:
++Transition++ :classe qui représente une transition d'un état au autre avec
la liste des alphabets que l'automate peut les lisé.
++TransitionGraphe++ :c'est l'objet graphique qui représente une transition 
'Forme gémétrique'.
"""
#===============================================================================
from etat import *
from math import cos
from math import pi
from math import sin
from math import sqrt

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
class Transition:
    """
    c'est une classe qui permette de definir une transition 
    entre deux états d'un automate avec une ou plusieurs lettres.
    """
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def __init__(self, automate, etatDepart=None, etatFin=None, lettres=set()):
        """initialisateur du classe"""
        self.automate = automate
        self.etatDepart = etatDepart#l'état où cette transition se commence.(:EtatGraphe)
        self.etatFin = etatFin#l'état d'arrivée de cette transition.(:EtatGraphe)
        self._lettres = lettres#les lettre qui peut l'automate lire pour faire cette transition.(:set)
        if self not in self.automate.Transitions:
            self.automate.Transitions.add(self)
            self._set_lettres(lettres)
 
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def _get_lettres(self):
        """la methode qui sera appllé lorsqu'on récupére l'ensemble des lettres de cette trans."""
        return self._lettres
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def _set_lettres(self, letr):
        """la méthode qui permette d'ajouter d'autre lettres au l'ensemble des lettres."""
        letr = set(letr)
        if len(list(letr)) == 0:
            letr.add(self.automate.epsilon)
        dif = list(self._lettres-letr)#les lettres supprimer 
        #self._lettres = self._lettres | letr#réunion de deux ensemble
        self._lettres = letr
        self.automate.A = self.automate.A | self._lettres
        #--------------------------
        #supprimer les transitions qui sont lit les lettre supprimées pour transiter.
        for a in dif:
            lsup = self.automate.Auto[self.etatDepart.etiquette][a]
            if self.etatFin.etiquette in lsup:
                self.automate.Auto[self.etatDepart.etiquette][a].remove(self.etatFin.etiquette)
            if len(self.automate.Auto[self.etatDepart.etiquette][a]) < 1:
                del self.automate.Auto[self.etatDepart.etiquette][a]
        #ajouter les nouvelles transitions avec les nv lettres.
        for a in list(letr):
            if a not in self.automate.Auto[self.etatDepart.etiquette]:
                self.automate.Auto[self.etatDepart.etiquette][a] = list()
            self.automate.Auto[self.etatDepart.etiquette][a].append(self.etatFin.etiquette)
            #supprimer les doublons
            self.automate.Auto[self.etatDepart.etiquette][a] = \
                list(set(self.automate.Auto[self.etatDepart.etiquette][a]))
        #actualiser l'ensemble d'alphabet de l'automate
        alph = set()
        for ligne in self.automate.Auto.values():
            alph = alph | set(ligne.keys())#ajouter les alphabets d'un état
        self.automate.A = alph#maintenant les alphabets d'automate est seul qui ont éxistés dans Auto.
    lettres = property(_get_lettres, _set_lettres)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
#===============================================================================
class TransitionGraphe(Transition):
    """
    une classe qui représent une trasition(graphiquement et thériquemet) 
    entre deux états d'un automate. 
    """
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def __init__(self, automate, etatDepart=None, etatFin=None, lettres=set()):
        """
        initialisateur d'une transition , avec un état de départ et état de fin
        et les lettres sui peut lire l'automate transitant. 
        """
        super().__init__(automate, etatDepart, etatFin, lettres)
        self.curve = QuadCurveBezier2D(self.automate, self.etatDepart, self.etatFin)
        self.sens = None#le num du courbe de bezier dans le canvas
        self.text = None#le num d'etiquette (lettres) dans le canvas
        #
        self.etatDepart.transDepart.append(self)
        self.etatFin.transFin.append(self)
        #
        self.text_entry = Entry(self.automate.toile, relief='ridge', highlightthickness=2, bg='#2C9E87', fg='yellow', font='arial 12 bold')
        self.num_text_entry = None#le numero du champ d'entré dans la toile (canvas).
        self.text_entry.bind("<Return>", self.click_key_return_entry)
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def supprimer(self):
        """
        méthode qui permette de supprimer la transition du canvas et l'automate
        """
        print("supprimer:", self.etatDepart.etiquette, '->', self.etatFin.etiquette)
        if self.sens is not None:
            self.automate.toile.delete(self.sens)
        if self.text is not None:
            self.automate.toile.delete(self.text)
        if len(list(self.lettres)) > 0:
            for a in list(self.lettres):
                try:
                    self.automate.Auto[self.etatDepart.etiquette][a].remove(self.etatFin.etiquette)
                except:
                    print("etiquette non existe")#c'est seulement , pq je veux pas voir les erreurs rouges.

        if self in self.etatDepart.transDepart:
            self.etatDepart.transDepart.remove(self)
            self.etatDepart.dessiner()
        if self in self.etatFin.transFin:
            self.etatFin.transFin.remove(self)
            self.etatFin.dessiner()
        if self in self.automate.Transitions:
            self.automate.Transitions.remove(self)
        
        self.automate.actualiser()

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     
    def dessiner(self):
        """
        méthode qui permette de dessiner une trasition etre deux étas d'automate
        """
        if self.sens is not None:
            self.automate.toile.delete(self.sens)
        if self.text is not None:
            self.automate.toile.delete(self.text)
        self.sens = self.curve.dessiner()
        self.text = self.automate.toile.create_text(self.curve.points[len(self.curve.points) // 2], \
                                                    text=','.join(self.lettres), font='arial 12 bold', anchor=CENTER, fill='#2C9E87')
                                                    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def entrer_lettres(self):
        """
        une méthode qui permette d'afficher un champ d'entrée, pour saisir 
        les lettres qui peut l'automate lit avant sa transition
        vers l'état fin de cette Transition.
        """
        ltr = "".join(self.lettres)
        str = StringVar(self.automate)
        str.set(ltr)
        self.text_entry['textvariable'] = str
        self.text_entry['state'] = 'normal'
        self.text_entry.focus()
        self.text_entry.icursor(END)
        #on prend le point milieu du courbe de bézier
        x, y = self.curve.points[len(self.curve.points) // 2]
        self.num_text_entry = self.automate.toile.create_window(x, y, window=self.text_entry)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def click_key_return_entry(self, event):
        """
        le géstionnaire d'événement 'click boutton entré du clavier' quand le champ
        d'entrée a le focus.
        """
        if self.num_text_entry is not None:
            self.automate.toile.delete(self.num_text_entry)
        let = self.text_entry.get()
        let = set(let)
        self.lettres = let
        if self.text is not None:
            self.automate.toile.itemconfig(self.text, text=",".join(self.lettres))
        else:
            self.text = self.automate.toile.create_text(self.curve.points[len(self.curve.points) // 2], \
                                                        text=','.join(self.lettres), font='arial 12 bold', fill='#2C9E87')
        self.text_entry['state'] = 'disabled'
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def contient_point(self, x, y):
        """
        méthode qui permette de vérifier si un point est dans la courbe.
        """
        j = 0
        for i in range(1, len(self.curve.points), 5):
            x1 = min(self.curve.points[j][0], self.curve.points[i][0])
            x2 = max(self.curve.points[j][0], self.curve.points[i][0])
            y1 = min(self.curve.points[j][1], self.curve.points[i][1])
            y2 = max(self.curve.points[j][1], self.curve.points[i][1])
            if x1-3 <= x <= x2 + 3 and y1-3 <= y <= y2 + 3:
                return True
            j = i
        return False
    
    def __repr__(self):
        """"""
        return "!" + repr(self.etatDepart) + "--" + "~".join(self.lettres) + "-->" + repr(self.etatFin) + "!"

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def get_dictionnaire(self):
        """
        la méthode qui permette de retourner un dictionnaire contientt tous
        les info sur cette transition.
        """
        return {
    "etq_d":self.etatDepart.etiquette,
    "etq_f":self.etatFin.etiquette,
    "lettres":list(self.lettres)
    }
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
#----classe courbe de bezier quadratique
class QuadCurveBezier2D:
    """"""
    def __init__(self, automate, etatdepart, etatFin):
        self.automate = automate
        self.etatDepart = etatdepart
        self.etatFin = etatFin
        self.ctrlx, self.ctrly = 0, 0
        self.set_point_controle()
        self.points = []
       
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def diviser(self):
        """
        méthode qui permette de determier les points du courbe polynomiale (de Bézier).
        """
        self.points.clear()
        t = 0.00
        for i in range(0, 400):#c'est très long .pour mon processeur.
            t += 0.0025# utiliser 0.01 comme un pas.et boucler 100 fois.
            t = '%.4f' % t
            t = float(t)
            x = self.etatDepart.centre[0] * ((1-t) ** 3) + 3 * self.ctrlx * t * ((1-t) ** 2)\
            + 3 * self.ctrlx2 * (t ** 2) * (1-t) + self.etatFin.centre[0] * (t ** 3)
            y = self.etatDepart.centre[1] * ((1-t) ** 3) + 3 * self.ctrly * t * ((1-t) ** 2)\
            + 3 * self.ctrly2 * (t ** 2) * (1-t) + self.etatFin.centre[1] * (t ** 3)
            df = sqrt((x-self.etatFin.centre[0]) ** 2 + (y-self.etatFin.centre[1]) ** 2)
            dd = sqrt((x-self.etatDepart.centre[0]) ** 2 + (y-self.etatDepart.centre[1]) ** 2)
            if df > EtatGraphe.rayon and dd > EtatGraphe.rayon:#pour ne sorte pas dans le cercle d'etat d'automate.
                self.points.append((x, y))

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>         
    def dessiner(self):
        """méthode qui permette de dessier une courbe de bézier (transition)"""
        #self.points.clear()
        self.set_point_controle()
        self.diviser()
        try:
            return self.automate.toile.create_line(self.points, width=2, joinstyle='round', \
                                                   capstyle='round', arrow=LAST, fill="orange")
        except:
            print("Exception")
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def set_point_debut(self, x, y):
        self.etatDepart.centre = [x, y]
  
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def set_point_controle(self):
        x = (self.etatFin.centre[0] + self.etatDepart.centre[0]) / 2
        y = (self.etatFin.centre[1] + self.etatDepart.centre[1]) / 2
        d = sqrt((self.etatFin.centre[0]-self.etatDepart.centre[0]) ** 2 + (self.etatFin.centre[1]-self.etatDepart.centre[1]) ** 2)
        if self.etatDepart is self.etatFin:
            self.ctrlx, self.ctrly = self.etatDepart.centre[0], self.etatDepart.centre[1]-4 * EtatGraphe.rayon
            self.ctrlx2, self.ctrly2 = self.etatDepart.centre[0]-4 * EtatGraphe.rayon, self.etatDepart.centre[1]
        elif d <= EtatGraphe.rayon * 2:
            self.ctrlx, self.ctrly = self.etatDepart.centre[0], self.etatDepart.centre[1] + 4 * EtatGraphe.rayon
            self.ctrlx2, self.ctrly2 = self.etatFin.centre[0], self.etatFin.centre[1] + 4 * EtatGraphe.rayon
    
        else:
            self.ctrlx = self.ctrlx2 = self.etatDepart.centre[0] + cos(pi / 20) * (x-self.etatDepart.centre[0])-sin(pi / 20) * (self.etatDepart.centre[1]-y)
            self.ctrly = self.ctrly2 = self.etatDepart.centre[1] + cos(pi / 20) * (y-self.etatDepart.centre[1]) + sin(pi / 20) * (self.etatDepart.centre[0]-x)
 
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    def set_point_fin(self, x, y):
        self.etatFin.centre = [x, y]
        
   