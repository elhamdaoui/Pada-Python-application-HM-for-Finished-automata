# -*-coding:Latin-1 -*

__author__ = "abdelmajid"
__date__ = "$14 juin 2015 03:44:12$"

dictionnaire1 = {
"contenu":{
"0":"""
   Les expressions rationnelles, ou expressions r�guli�res sont des expressions qui
d�crivent les langages rationnels. Le terme expression r�guli�re est ant�rieur, et
les langages d�crits par ces expressions sont naturellement aussi appel�s langages
r�guliers. Les expressions rationnelles, plus ou moins �tendues, servent notamment
� la recherche de motifs dans un texte.
"""
},
"subsection0":{
"titre":"Expressions rationnelles",
"contenu":{
"0":"""
Une expression rationnelle E sur un alphabet A est soit :
- Un symbole d�notant le mot vide : � ou 1.
- une lettre <a> de l'alphabet A.
- une r�union (ou somme, en notation alg�brique) de deux expressions rationnelles
M et N, not�e E = M|N ou E = M+N.
- une concat�nation (ou un produit, en notation alg�brique) de deux expressions
rationnelles M et N, not�e E = M.N ou simplement E = MN.
- une r�p�tition, ou �toile, ou it�ration, d'une expression rationnelle M not�e
E = M*.
"""
}
},
"subsection1":{
"titre":"Construction d-automates finis � partir des expressions rationnelles",
"contenu":{
"0":"""
   Il existe plusieurs m�thodes pour construire un automate fini � partir d�une
expression rationnelle :

""",
"0bold":"   la m�thode de Thompson",
"1":""" Elle a �t� utilis�e par Ken Thompson dans l'impl�mentation
de la commande grep du syst�me Unix. On construit r�cursivement
des automates pour les composants d'une expression. La forme particuli�re des
automates permet de les combiner avec une grande facilit�. L'automate obtenu est
non d�terministe asynchrone.

""",
"1bold":"   la m�thode de Glushkov",
"2":""" Cette m�thode, attribu�e � l'informaticien Glushkov,
permet de construire un automate non d�terministe de m�me taille (nombre d'�tats)
que la taille (nombre de symboles) de l'expression rationnelle. Il a �t�
observ� que l'automate de Glushkov est le m�me que l'automate obtenu en supprimant
les �-transitions de l'automate de Thompson.

""",
"2bold":"   la m�thode des quotients ou r�siduels ou d�riv�es, due � Brzozowski",
"3":""" On
forme les quotients (ou r�siduels) successifs de l'expression. Il n'y en a qu'un
nombre fini de diff�rents, apr�s application d'un certain nombre de r�gles de simplification
qui sont l'associativit�, la commutativit� et l'idempotente de l'op�ration +.


    Aucune de ces m�thodes ne donne directement l'automate minimal d'un langage.
On peut aussi employer des constructions simples d'automates pour la r�union, le
produit et l'�toile de langages, et op�rer r�cursivement.

    Soit A(M) (respectivement A(N)) l'automate fini reconnaissant le langage
d�not� par l'expression rationnelle M (respectivement N). Les constructions sont
les suivantes :

- Automate A(M|N) pour la r�union :
Il suffit de faire la r�union disjointe des automates A(M) et A(N).
- Automate A(M.N) pour le produit :
L'automate a pour �tats les �tats de A(M) et de A(N). Les �tats initiaux
sont ceux de A(M), les terminaux sont ceux de A(N). Les transitions sont
celles de A(M) et de A(N), et de plus des �-transitions des �tats terminaux
de A(M) vers les �tats initiaux de A(N).

Automate A(M*) pour l'�toile :
On part de l'automate A(M) que l'on augmente de deux �tats <i> et <t>. On
ajoute des �-transitions.
- de <i> � tout �tat initial de A(M)
- de tout �tat final de A(M) � <t>
- de <i> � <t> et de <t> � <i>.
L'�tat <i> (resp. <t>) est l'�tat initial (resp. final) de A(M*).
"""
}
},
"subsection2":{
"titre":"Convertion d'un automate en une expression r�guli�re",
"contenu":{
"0bold":"""
Th�or�me 3.8.1. """,
"1":"""Un langage est rationnel si, et seulement si, il est reconnaissable.

""",
"1bold":"""Algorithme d'�limination de Brzozowski-McCluskey
""",
"2":"""On d�crit ici un algorithme qui permet de d�terminer un expression r�guli�re
correspondant au langage reconnu par un automate standard.

- On standardise l'automate en ajoutant au besoin un �tat initial et final (voir
l'algorithme de Thompson pour un exemple).
- On consid�re chaque transition �tiquet�e avec une expression r�guli�re (et
donc pas seulement avec des caract�res ou �) puis on fusionne les transitions
entre deux m�mes �tats.

- On �limine chaque �tat autre que l'�tat initial et l'�tat final. Pour �liminer
un �tat <q1>, on consid�re tout couple (<q0> , <q2>) tel qu'il existe une transition
de <q0> vers <q1> (�tiquet�e avec l'expression <e>) et une transition de <q1> vers <q2>
(�tiquet�e avec l'expression <g>) ; notons <f> l'expression de l'�ventuelle transition
de <q1> vers <q1> et <h> l'expression de l'�ventuelle transition de <q0> vers <q2>.
On cr�e alors lors de l'�limination de <q1> (et des transitions associ�es) une
transition de <q0> vers <q2> �tiquet�e <ef*g+h>.

-L'expression r�guli�re �tiquetant la transition entre l'�tat initial et l'�tat
final s'interpr�te en le langage reconnu par l'automate initial..
"""
}
}
}
