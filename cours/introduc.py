# -*-coding:Latin-1 -*
__author__ = "abdelmajid"
__date__ = "$13 juin 2015 13:55:56$"

dictionnaire1 = {
"contenu":{
"0":"""
Dans les années 50 est apparu le besoin de langages de plus haut niveau que l'assembleur, de façon à abstraire certaines particularités propres à la machine (registres en nombre finis, instructions de branchement basiques, etc.) pour mieux se concentrer sur les aspects algorithmiques et pouvoir passer à l'échelle sur des projets plus complexes. Un des objectif était également de pouvoir écrire un seul programme pour des architectures différentes. Pour pouvoir utiliser ces langages, il faut alors soit disposer d’un interpréteur, c'est-à-dire un exécutable qui va lire le programme et évaluer son contenu ; soit traduire le programme en code machine exécutable : on parle alors de compilation.
""",
"1":"""
Ces langages se sont heurtés au scepticisme des programmeurs de l'époque qui avaient l'habitude de produire des codes assembleurs très efficaces et qui pensaient qu'il ne serait pas possible de produire automatiquement des exécutables aussi efficaces à partir de langages de haut niveau . Un bon compilateur  ne peut donc se contenter de traduire naïvement le langage de haut niveau, il doit l'optimiser. Ces optimisations, associées au gain d'échelle offert par l'abstraction, a permis la généralisation de l'utilisation de langages de haut niveau.
""",
"2":"""
Un compilateur ne traduit pas forcément un langages en code machine, il peut produire du code dans un langage intermédiaire qui sera ensuite lui-même compilé (par exemple, le langage intermédiaire peut être du C) ou interprété (par exemple, du bytecode).
""",
"3":"""
La production d'un compilateur comprend une succession d'étapes importantes, implémentée par différents modules :
""",
"31bold1":"""
-<préprocesseur> :""",
"4":"""est un programme qui procède à des transformations sur un code source, avant l'étape de traduction ou bien la compilation.
""",
"41bold2":"-<analyseur lexical> :",
"5":"""grouper les lettres pour former des mots (lexèmes). L'analyseur est un automate fini dont les états terminaux sont associés à des actions (traduction, émission d’un code caractérisant le lexème).
""",
"51bold3":"-<analyseur syntaxique> :",
"6":"""Les langages réguliers sont insuffisants pour spécifier la structure d'un programme. Il est nécessaire de reconnaître des constructions imbriquées, comme les blocs, les boucles, les expressions arithmétiques, parenthésées... Pour ces constructions il est nécessaire d'avoir une pile, donc on parle aux langages algébriques qui sont reconnus par des automates à pile.
""",
"61bold4":"-<analyse sémantique, typage >:",
"7":"""Pour définir un langage de programmation, il ne suffit pas de décrire sa syntaxe, c'est-à-dire l'ensemble des expressions valides dans ce langage. Il faut également décrire sa sémantique, c'est-à-dire comment ces expressions seront interprétées.
""",
"71bold5":"-<générateur de code intermédiaire> :",
"8":"""c'est le coeur du compilateur, après avoir vérifier les portées et les types, doit traduire l'arbre de Syntaxe abstraite en Code Intermédiaire. Ensuite le Back-End du compilateur traduit le Code Intermédiaire en Assembleur.
""",
"81bold6":"-<optimisation de code> :",
"9":"""L'optimalité du code est indécidable, puisque le problème de savoir si deux programmes ont le même comportement (terminent ou non) sur toutes les entrées est indécidable.
""",
"91bold7":"-<générateur de code assembleur>"
}
}


dictionnaire2={
"contenu":{
"0":"""
Un automate fini (on dit parfois, par une traduction littérale maladroite de
l'anglais, machine à états finis, au lieu de machine avec un nombre fini d'états),
state automaton ou finite state machine (FSA, FSM), est une machine abstraite
qui est un outil fondamental en mathématiques discrètes et en informatique. On les
retrouve dans la modélisation de processus, le contrôle, les protocoles de communication, la vérification de programmes, la théorie de la calculabilité, dans l’étude
des langages formels et en compilation. Ils sont utilisés dans la recherche des motifs
dans un texte.
""",
"1":"""
Les automates finis reconnaissent exactement des langages rationnels. Ce sont
les machines les plus simples dans la hiérarchie de Chomsky, et par conséquent ils
sont moins puissants que les automates à pile 5 et, bien entendu, que les machines
de Turing.
""",
"2":"""
Un automate est constitué d'états et de transitions. Son comportement est dirigé par un mot fourni en entrée : l'automate passe d'état en état, suivant les transitions, à la lecture de chaque lettre de l'entrée
""",
"3":"""
L'automate est dit « fini » car il possède un nombre fini d'états : il ne dispose donc que d'une mémoire bornée. On peut très bien considérer des automates sans limitation sur le nombre d'états : la théorie qui en résulte est très analogue à la théorie habituelle.Un automate fini peut être vu comme un graphe orienté étiqueté :les états sont les sommets et les transitions sont les arêtes étiquetées. L'état initial est marqué par une flèche entrante ; un état final est, selon les auteurs, soit doublement cerclé, soit marqué d'une flèche sortante.
""",
"4":"""
Une autre façon commode de représenter un automate fini est sa table de transition. Elle donne, pour chaque état et chaque lettre, l'état d'arrivée de la transition.
"""
}
}