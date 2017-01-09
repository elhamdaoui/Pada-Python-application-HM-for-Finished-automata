# -*-coding:Latin-1 -*

__author__ = "abdelmajid"
__date__ = "$30 juin 2015 23:05:18$"

from tkinter import END

dictionnaire1 = {
"0quoi":"""   PADA est une application s'interesse aux automates finis déterministes,\n   elle est développé par l'étudiant ELHAMDAOUI ABDELMAJID comme\n   sujet de son projet de fin d'étude pour dérocher sa licence en \n   science mathématiques et informatique au faculté polydisciplinaire de safi Maroc,\n   et encadré par ses professeurs Mr.Maarouf et Mr.Kchikech.\n\n    Cette application est très simple à utiliser, donc voici le guide de sa utilisation:\n\n
""",
"0titre":"  Dessin d'un automate\n",
"10":"""
   donc on peut dessiner un automate à l'aide des bouttons qui sont placées\n    à coté gauche de l'interface qui nous aide de faire:\n
""",
"1100soustitre":"   1er boutton: ",
"1101":"quand on clique sur ce boutton, donc on peut déplacer \n   les états, modifier l'état comme un état initial ou final\n   avec le bouton droite du souris.\n",
"1102soustitre":"   2ème boutton: ",
"1103":"permet de dessiner un état.\n",
"1104soustitre":"   3ème boutton: ",
"1105":"permet de dessiner une transition, on clique sur un état\n   et on fait glisser le cursor vers un autre état, puis un champ de text qui nous permet\n   d'entrer les lettres portant par cette transition.\n",
"1110soustitre":"   4ème boutton: ",
"1111":"   permet de supprimer un état ou bien une transition,\n   on clique sur l'élement à supprimer.\n",
"1112soustitre":"   5ème boutton: ",
"1113":"c'est le boutton défaire.\n",
"1114soustitre":"   6ème boutton: ",
"1115":"c'est le boutton refaire.\n",
"1116soustitre":"   7ème boutton: ",
"1117":"permet de supprimer netoyer le paneau de dessin.\n\n",

"200titre":"  le menu Options\n",
"201soustitre":"   sous menu <Nouveau>: ",
"202":"permet d'ouvrir une nouvelle fenêtre, pour un nouveau automate.\n",
"203soustitre":"   sous menu <Ouvrir>: ",
"204":"permet d'ouvrir un automate déjà enregister dans \n   un fichier d'extention pap.\n",
"205soustitre":"   sous menu <Enregistrer sous>: ",
"206":"permet d'enregister un automate dans un fichier.\n",
"207soustitre":"   sous menu <plein ecarn>: ",
"208":"permet de mettre l'application au mode plein écran.\n",
"220soustitre":"   sous menu <fermer>: ",
"221":"permet de fermer la fenetre.\n\n",

"300titre":"  le menu Conversion\n",
"301soustitre":"   sous menu <Convert en AFD>: ",
"302":"permet de convertir un automate fini non déterministe \n   en un automate fini déterministe.\n",
"303soustitre":"   sous menu <Completer automate>: ",
"304":"permet de completer un automate s'il est incomplet.\n",
"305soustitre":"   sous menu <Minimiser automate>: ",
"306":"permet de minimiser un automate fini déterminste ou non.\n",
"307soustitre":"   sous menu <Convert en RE>: ",
"308":"permet de convertir un automate en une expression régulière.\n",
"320soustitre":"   sous menu <Convert RE en automate>: ",
"321":"permet d'obtenir l'automate qui reconnu le langage rationnel\n   décrit par une expression régulière.\n\n",

"400titre":"  le menu Opérations\n",
"401soustitre":"   sous menu <fermeture transitive>: ",
"402":"permet de obtenir un automate représentant la fermeture de KLEENE\n   d'un automate.\n",
"403soustitre":"   sous menu <Concaténation>: ",
"404":"permet de faire la concaténation de deux automates, à condition\n   d'ouvrir deux fenêtres chaqune représente un automate.\n",
"405soustitre":"   sous menu <Réunion>: ",
"406":"permet de faire la réunion de deux automates, même condition \n  que la concaténation.\n\n",

"500titre":"  le menu Test\n",
"501soustitre":"   sous menu <Déterminisation>: ",
"502":"permet de tester si un automate est déterministe ou non.\n",
"503soustitre":"   sous menu <Concaténation>: ",
"504":"permet de faire la concaténation de deux automates, à condition\n   d'ouvrir deux fenêtres chaqune représente un automate.\n\n",

"600titre":"  le menu Aides\n",
"601soustitre":"   sous menu <cours automates finis>: ",
"602":"permet d'ouvrir une nouvelle fenêtre contient une documentation\n   sur les automates fini.\n",
"603soustitre":"   sous menu <aide>: ",
"604":"permet d'ouvrir l'aide de l'application PADA. vous étes ici ;) .\n",
"605soustitre":"   sous menu <à propos>: ",
"606":"à propos de l'application PADA ;) .\n\n"

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
            
