# -*-coding:Latin-1 -*

__author__ = "abdelmajid"
__date__ = "$14 juin 2015 03:22:51$"

dictionnaire1 = {
"contenu":{
"0":"""
Un automate asynchrone est un automate fini autoris� � poss�der des transitions
�tiquet�es par le mot vide, appel�es des �-transitions.
L'�limination des �-transitions se fait par un algorithme de fermeture transitive
comme suit :
- Pour chaque chemin d'un �tat <s> � un �tat <t> form� de �-transitions, et pour
chaque transition de <t> � un �tat <u> portant une lettre <a>, ajouter une transition
de <s> � <u> d'�tiquette <a>.
- Pour chaque chemin d'un �tat <s> � un �tat <t> terminal form� de �-transitions,
ajouter <s> � lensemble des �tats terminaux.
- Supprimer les �-transitions.
"""
}
}
