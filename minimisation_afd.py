# -*-coding:Latin-1 -*

#===============================================================================
__author__ = "abdelmajid"
__date__ = "$19 avr. 2015 01:14:26$"
__doc__ = """
c'est un module qui contient tout ce que concerne la technique de minimisation 
d'un automate finis déterministe.
"""
#===============================================================================
from random import randrange
from tkinter import *
from transformation_auto import *

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class MinimiserAfd:
    """
    c'est la classe qui permette de minimiser un automate AFD.
    """
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def __init__(self, automate):
        """
        l'initialisteur qui prend en paramétres l'automate à minimiser.
        """
        self.automateNM = automate#attention au référence. (fais une copie)
        self.automateM = automate.copie(automate.master)#attention au référence. (c'est une copie) 
        

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def mini_automate(self):
        """
        --méthode sera appellé après l'initialisateur
        c'est une méthode qui contient tout le travaille de minimisation,
        on peut faire ça dans l'initialisateur '__init__'. mais 
        pour afficher tous les étapes je fais ça.
        --convertir en AFD
        --completer
        --minimisation.
        donc j'attache l'automate au fenetre et puis je fais l'appelle à
        cette méthode.
        sinon on tout ces étapes seront faites avant le remplacement du cadre.
        donc rien, sauf la forme finale d'automate.
        """
        if len(self.automateM.est_complet()) > 0:
            self.automateM.completer(False)
            showinfo("information", "cet automate est incomplet,\n\
            on le complete.")
        print("###################################################")
        print("###################minimisation####################")
        print("###################################################")
        self.algorithme_de_moore()
        print("###################################################")
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def algorithme_de_moore(self):
        """
        une méthode qui decrit la minimisation utilisant l'algorithme de Moore.
        Principe général : l'algorithme calcule lettre par lettre les mots
        séparant des états (il calcule donc les classes d'équivalences des
        relations =n). Après examen de chaque longueur de mot possible,
        un bilan est fait : il consiste à attribuer un numéro (en chiffre)
        à chaque classe de =n.
        l'équivalence ici est celle là de Nérode. 
        """
        print("moore")
        #commençant l'algorithme de Moore.
        alphabet=[a for a in list(self.automateM.A)]
        etats=[etat.etiquette for etat in list(self.automateM.Q)]
        etats_f=[etat.etiquette for etat in list(self.automateM.F)]
        etats_i=[etat.etiquette for etat in list(self.automateM.I)]
        bilan={}
        for etq in etats:
            if etq in etats_f:
                bilan[etq]=1
            else:
                bilan[etq]=0
        repeter=True
        while repeter:
            table={}
            #------------remplir la table------------
            for a in alphabet:
                table[a]={}
                for etq in etats:
                    #puisque l'automate est déterministe complet donc la transition
                    #partant de 'etq' et portant la lettre 'a' est existe, et a arrivé
                    #au une seul état 'etq2'.
                    etq2=self.automateM.Auto[etq][a][0]
                    table[a][etq]=bilan[etq2]
            #----------------------------------------
            bilan2={}#détéerminer le nouveau bilan.
            classes=0#entier qui permet de donner un chifre au nouvelle classe.
            cols={}
            #--------------remplir le nv bilan-------
            for etq in etats:
                colonne=[bilan[etq]]
                for a in alphabet:
                    colonne.append(table[a][etq])
                colonne=[str(i) for i in colonne]
                colonne=",".join(colonne)#l'ensemble des classe pour une colonne.
                if colonne not in cols:
                    cols[colonne]=classes
                    classes+=1
                bilan2[etq]=cols[colonne]#la nouvelle classe d'etat au nv bilan.
            #-----teste si le bilan ne change pas-----
            for etq in etats:
                if bilan[etq]!=bilan2[etq]:
                    bilan=bilan2.copy()
                    break
            else:
                repeter=False#fin du boucle.
        self.automateM.vider()
        nv_classes=list(set(bilan.values()))#les chifres corresponds au classes.
        classes={}#dictionnaire qui va contenir comme clé le chifre de classe et comme valeur l'état correspond.
        #-----------les nouveau états d'automate minimal------
        etat_rebut=None
        for c in nv_classes:
            classe=[]
            for cle,val in bilan.items():
                if val==c:
                    classe.append(cle)
            initial=final=False
            if len(set(classe)&set(etats_f))>0:
                final=True
            if len(set(classe)&set(etats_i))>0:
                initial=True
            e=EtatGraphe(self.automateM,None,None,initial,final)
            e.ens_etats=classe.copy()
            #e.dessiner()
            classes[c]=e
            if len(classe)==1 and classe[0]=='rebut':
                etat_rebut=e#pour supprimer cette état à la fin d'algorithme
        #-----------les nouvelles transitions d'automate minimal------
        for etq in etats:
            c1=bilan[etq]
            etat1=classes[c1]
            for a in alphabet:
                c2=table[a][etq]
                etat2=classes[c2]
                for tr in list(self.automateM.Transitions):
                    if tr.etatDepart is etat1 and tr.etatFin is etat2:
                        tr.lettres=set(list(tr.lettres)+[a])
                        #tr.dessiner()
                        break
                else:
                    TransitionGraphe(self.automateM,etat1,etat2,set([a]))#.dessiner()
        #supprimer l'état rebut 
        if etat_rebut is not None:
            etat_rebut.supprimer()
        self.automateM.dessiner()
                        
        

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def mini_automate_2(self):
        """
        --méthode sera appellé après l'initialisateur
        c'est une méthode qui contient tout le travaille de minimisation,
        on peut faire ça dans l'initialisateur '__init__'. mais 
        pour afficher tous les étapes je fais ça.
        --convertir en AFD
        --completer
        --minimisation.
        donc j'attache l'automate au fenetre et puis je fais l'appelle à
        cette méthode.
        sinon on tout ces étapes seront faites avant le remplacement du cadre.
        donc rien, sauf la forme finale d'automate.
        """
        print("------mininn")
        if not self.automateM.est_deterministe():
            showinfo("information", "cet automate est non détérministe,\n\
            on le convert en AFD.")
            self.automateM = TransformAuto(self.automateM).automateD#cette ligne permette d'éviter
        #le problème de référence car il construit nouveau auromate (automateD). 
        if len(self.automateM.est_complet()) > 0:
            showinfo("information", "cet automate est incomplet,\n\
            on le complete.")
            self.automateM.completer(False)
            self.automateM.dessiner()
        self.etats = [etat.etiquette for etat in list(self.automateM.Q)]
        self.etat_i = [etat.etiquette for etat in list(self.automateM.I)]
        self.etats_f = [etat.etiquette for etat in list(self.automateM.F)]
        #triée les liste. c'est pas inportants.mais justement pour l'affichage.
        self.etats.sort()
        self.etat_i.sort()
        self.etats_f.sort()
        #--------
        """
        print(self.automateM.A)
        print(self.etats)
        print(self.etats_f)
        print(self.etat_i)"""
        #construction du rectangle utilisé par l'algorithme de minimisation.
        self.triangle = {}
        self.construction_triangle()
        #liste qui contient les couple existe dans le rectengle,(ligne,colonne)
        #c'est pas intéréssante mais elle est utilisée par la méthode est_marquée.
        #pour gagnée le temps. (compléxité).
        self.couples = []
        for i, l in self.triangle.items():
            for j in l:
                self.couples.append((i, j))
        print(self.couples)
        #-------
        print(self.triangle)
        #-------
        
        print("############################################")
        print("####### algorithme de minimisation #########")
        print("############################################")
        self.algorithme_de_moore()
        #self.algo_minimiser()
        #print(self.triangle)
        #ensnv=[etat.ens_etats for etat in list(self.automateM.Q)]
        #print("ens_nv_etats :",ensnv)
        print("############################################")
                            
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def construction_triangle(self):
        """
        c'est la méthode qui permette de construire le triangle q'on va 
        utiliser pour l'algorithme du minimisation.
        """
        lignes = self.etats[1:]
        colonnes = self.etats[:-1]
        self.triangle = {}
        for l in lignes:
            self.triangle[l] = {}
        for c in colonnes:
            for l in lignes:
                if (l in self.etats_f) ^ (c in self.etats_f):#si l et c sont distinguables.
                    self.triangle[l][c] = True#marqué case.
                else:
                    self.triangle[l][c] = False 
            lignes = lignes[1:]
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def est_marquee(self, etq1, etq2):
        """
        la méthode qui permette de vérifier si un couple(etq1,etq2)
        est marqué.
        """
        if (etq1, etq2) not in self.couples and (etq2, etq1) not in self.couples:
            return False
        couple = (etq1, etq2) if (etq1, etq2) in self.couples else (etq2, etq1)
        return self.triangle[couple[0]][couple[1]]

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def marquee_couple(self, etq1, etq2):
        """
        une méthode qui permette de marquée un couple d'états.
        """
        if (etq1, etq2) not in self.couples and (etq2, etq1) not in self.couples:
            return False
        couple = (etq1, etq2) if (etq1, etq2) in self.couples else (etq2, etq1)
        self.triangle[couple[0]][couple[1]] = True
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def algo_minimiser(self):
        """
        la méthode qui permette d'appliquer l'algorithme de minimisation. 
        """
        cpls = self.couples.copy()
        cpls = [cp for cp in cpls if not self.est_marquee(cp[0], cp[1])]#les couple non marquées.
        cpls_temp = cpls.copy()
        #marquées les couples distinguables non encore marqués.
        while True:
            for cp in cpls:
                etat1 = self.automateM.get_etat(cp[0])
                etat2 = self.automateM.get_etat(cp[1])
                for a in list(self.automateM.A):
                    lis_e = etat1.lit_lettre(a)[0] + etat2.lit_lettre(a)[0]
                    print("{0}--{1}-->({2})".format(cp, a, lis_e))
                    if len(lis_e) == 2:
                        if self.est_marquee(lis_e[0], lis_e[1]):
                            self.marquee_couple(cp[0], cp[1])
                            cpls_temp.remove(cp)
                            break#sortir du boucle marquée
            if len(cpls) == len(cpls_temp):
                break#fin d'algorithme, tout est fait.
            cpls = cpls_temp.copy()
        #recupérer les couples non marqués.
        nv_couples = []
        for i, l in self.triangle.items():
            for j in l.keys():
                if not self.est_marquee(i, j):
                    nv_couples.append((i, j))
        #construction les nouveaux états et transitions.
        nn_t=len(self.etats)#le nbr d'états d'automate.
        #(nn_t*(nn_t-1))/2 c'est le nombre de couples possibles.
        if len(nv_couples) > 0 and len(nv_couples)!=(nn_t*(nn_t-1))/2:
            auto = AutoGraphe(self.automateNM.master, self.automateNM.largeur, self.automateNM.hauteur)
            etats_auto = []
            #l'ajout des nouveaux états (couples).
            for cp in nv_couples:
                etats_auto.append(cp[0])
                etats_auto.append(cp[1])
                initial = False
                final = False
                if cp[0] in self.etats_f or cp[1] in self.etats_f:
                    final = True
                if cp[0] in self.etat_i or cp[1] in self.etat_i:
                    initial = True
                e = EtatGraphe(auto, None, None, initial, final)
                e.ens_etats = list(cp)
            #=============================================
            #état initial s'il n'est pas existe. 
            if self.etat_i[0] not in etats_auto:
                etats_auto.append(self.etat_i[0]) 
                final = False
                if self.etat_i[0] in self.etats_f:
                    final = True
                e = EtatGraphe(auto, None, None, True, final)
                e.ens_etats = list(self.etat_i)#automate détérministe donc un seul état initial.
                
            etats_single = list(set(etats_auto))
            #print("siiin_aven",etats_single)
            etats_single = list(set(self.etats)-set(etats_single))#les états non trouvées.
            print("siiin_apres",etats_single)
            
            #ajouter les états singletons  (EtatGraphe) à l'automate.
            for e in etats_single:
                etats_auto.append(e)
                initial = False
                final = False
                if e in self.etats_f:
                    final = True
                if e in self.etat_i:
                    initial = True
                ets = EtatGraphe(auto, None, None, initial, final)
                lis_e = list()
                lis_e.append(e)
                ets.ens_etats = lis_e
                
            
            #------------------------------------
            #=====ajouter les transition au auto minimisé
            for etat_m1 in list(auto.Q):
                etqs = list(etat_m1.ens_etats)
                for a in list(self.automateM.A):
                    lis = []
                    for etq in etqs:
                        etat_nm = self.automateM.get_etat(etq)
                        lis += etat_nm.lit_lettre(a)[0]
                    lis = list(set(lis))
                    for etat_m2 in list(auto.Q):
                        if len(set(lis) & set(etat_m2.ens_etats)) > 0:
                            lis_etqs = list()
                            lis_etqs.append(a)
                            nv = True
                            for tr in list(auto.Transitions):
                                if tr.etatDepart is etat_m1 and tr.etatFin is etat_m2:
                                    tr.lettres = set(list(tr.lettres) + lis_etqs)
                                    nv = False
                                    break
                            if nv:
                                TransitionGraphe(auto, etat_m1, etat_m2, set(lis_etqs))
            """
            print("etats-singles", etats_single)
            print("couples", nv_couples)
            print("etats", auto.Q)
            print("---ens")
            for eta in list(auto.Q):
                print(eta.etiquette, "-->", eta.ens_etats)
            print("-----")"""
            #d'où notre automate minimal.
            auto.dessiner()
            self.automateM = auto
        else:
            showinfo("information", "cet automate est détérministe minimal.")
                                

                

        
                
                
            
