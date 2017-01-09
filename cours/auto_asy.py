# -*-coding:Latin-1 -*

__author__ = "abdelmajid"
__date__ = "$14 juin 2015 03:22:51$"

dictionnaire1 = {
"contenu":{
"0":"""
Un automate asynchrone est un automate fini autorisé à posséder des transitions
étiquetées par le mot vide, appelées des £-transitions.
L'élimination des £-transitions se fait par un algorithme de fermeture transitive
comme suit :
- Pour chaque chemin d'un état <s> à un état <t> formé de £-transitions, et pour
chaque transition de <t> à un état <u> portant une lettre <a>, ajouter une transition
de <s> à <u> d'étiquette <a>.
- Pour chaque chemin d'un état <s> à un état <t> terminal formé de £-transitions,
ajouter <s> à lensemble des états terminaux.
- Supprimer les £-transitions.
"""
}
}
