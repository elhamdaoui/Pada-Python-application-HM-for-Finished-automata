# -*-coding:Latin-1 -*

__author__ = "abdelmajid"
__date__ = "$30 juin 2015 23:05:18$"

from tkinter import END

dictionnaire1 = {
"0quoi":"""   PADA est une application s'interesse aux automates finis d�terministes,\n   elle est d�velopp� par l'�tudiant ELHAMDAOUI ABDELMAJID comme\n   sujet de son projet de fin d'�tude pour d�rocher sa licence en \n   science math�matiques et informatique au facult� polydisciplinaire de safi Maroc,\n   et encadr� par ses professeurs Mr.Maarouf et Mr.Kchikech.\n\n    Cette application est tr�s simple � utiliser, donc voici le guide de sa utilisation:\n\n
""",
"0titre":"  Dessin d'un automate\n",
"10":"""
   donc on peut dessiner un automate � l'aide des bouttons qui sont plac�es\n    � cot� gauche de l'interface qui nous aide de faire:\n
""",
"1100soustitre":"   1er boutton: ",
"1101":"quand on clique sur ce boutton, donc on peut d�placer \n   les �tats, modifier l'�tat comme un �tat initial ou final\n   avec le bouton droite du souris.\n",
"1102soustitre":"   2�me boutton: ",
"1103":"permet de dessiner un �tat.\n",
"1104soustitre":"   3�me boutton: ",
"1105":"permet de dessiner une transition, on clique sur un �tat\n   et on fait glisser le cursor vers un autre �tat, puis un champ de text qui nous permet\n   d'entrer les lettres portant par cette transition.\n",
"1110soustitre":"   4�me boutton: ",
"1111":"   permet de supprimer un �tat ou bien une transition,\n   on clique sur l'�lement � supprimer.\n",
"1112soustitre":"   5�me boutton: ",
"1113":"c'est le boutton d�faire.\n",
"1114soustitre":"   6�me boutton: ",
"1115":"c'est le boutton refaire.\n",
"1116soustitre":"   7�me boutton: ",
"1117":"permet de supprimer netoyer le paneau de dessin.\n\n",

"200titre":"  le menu Options\n",
"201soustitre":"   sous menu <Nouveau>: ",
"202":"permet d'ouvrir une nouvelle fen�tre, pour un nouveau automate.\n",
"203soustitre":"   sous menu <Ouvrir>: ",
"204":"permet d'ouvrir un automate d�j� enregister dans \n   un fichier d'extention pap.\n",
"205soustitre":"   sous menu <Enregistrer sous>: ",
"206":"permet d'enregister un automate dans un fichier.\n",
"207soustitre":"   sous menu <plein ecarn>: ",
"208":"permet de mettre l'application au mode plein �cran.\n",
"220soustitre":"   sous menu <fermer>: ",
"221":"permet de fermer la fenetre.\n\n",

"300titre":"  le menu Conversion\n",
"301soustitre":"   sous menu <Convert en AFD>: ",
"302":"permet de convertir un automate fini non d�terministe \n   en un automate fini d�terministe.\n",
"303soustitre":"   sous menu <Completer automate>: ",
"304":"permet de completer un automate s'il est incomplet.\n",
"305soustitre":"   sous menu <Minimiser automate>: ",
"306":"permet de minimiser un automate fini d�terminste ou non.\n",
"307soustitre":"   sous menu <Convert en RE>: ",
"308":"permet de convertir un automate en une expression r�guli�re.\n",
"320soustitre":"   sous menu <Convert RE en automate>: ",
"321":"permet d'obtenir l'automate qui reconnu le langage rationnel\n   d�crit par une expression r�guli�re.\n\n",

"400titre":"  le menu Op�rations\n",
"401soustitre":"   sous menu <fermeture transitive>: ",
"402":"permet de obtenir un automate repr�sentant la fermeture de KLEENE\n   d'un automate.\n",
"403soustitre":"   sous menu <Concat�nation>: ",
"404":"permet de faire la concat�nation de deux automates, � condition\n   d'ouvrir deux fen�tres chaqune repr�sente un automate.\n",
"405soustitre":"   sous menu <R�union>: ",
"406":"permet de faire la r�union de deux automates, m�me condition \n  que la concat�nation.\n\n",

"500titre":"  le menu Test\n",
"501soustitre":"   sous menu <D�terminisation>: ",
"502":"permet de tester si un automate est d�terministe ou non.\n",
"503soustitre":"   sous menu <Concat�nation>: ",
"504":"permet de faire la concat�nation de deux automates, � condition\n   d'ouvrir deux fen�tres chaqune repr�sente un automate.\n\n",

"600titre":"  le menu Aides\n",
"601soustitre":"   sous menu <cours automates finis>: ",
"602":"permet d'ouvrir une nouvelle fen�tre contient une documentation\n   sur les automates fini.\n",
"603soustitre":"   sous menu <aide>: ",
"604":"permet d'ouvrir l'aide de l'application PADA. vous �tes ici ;) .\n",
"605soustitre":"   sous menu <� propos>: ",
"606":"� propos de l'application PADA ;) .\n\n"

}


def compiler_texte(textWidget):
    """
    
    """
    keys=sorted(dictionnaire1.keys())
    for k in keys:
        v=dictionnaire1[k]
        if "quoi" in k:
            textWidget.insert(END,v,'quoi')
        elif "soustitre" in k:
            textWidget.insert(END,v,'soustitre')
        elif "titre" in k:
            textWidget.insert(END,v,'titre')
        else:
            textWidget.insert(END,v,'textnormal')
            
