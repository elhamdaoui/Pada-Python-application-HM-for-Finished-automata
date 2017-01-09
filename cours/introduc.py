# -*-coding:Latin-1 -*
__author__ = "abdelmajid"
__date__ = "$13 juin 2015 13:55:56$"

dictionnaire1 = {
"contenu":{
"0":"""
Dans les ann�es 50 est apparu le besoin de langages de plus haut niveau que l'assembleur, de fa�on � abstraire certaines particularit�s propres � la machine (registres en nombre finis, instructions de branchement basiques, etc.) pour mieux se concentrer sur les aspects algorithmiques et pouvoir passer � l'�chelle sur des projets plus complexes. Un des objectif �tait �galement de pouvoir �crire un seul programme pour des architectures diff�rentes. Pour pouvoir utiliser ces langages, il faut alors soit disposer d�un interpr�teur, c'est-�-dire un ex�cutable qui va lire le programme et �valuer son contenu ; soit traduire le programme en code machine ex�cutable : on parle alors de compilation.
""",
"1":"""
Ces langages se sont heurt�s au scepticisme des programmeurs de l'�poque qui avaient l'habitude de produire des codes assembleurs tr�s efficaces et qui pensaient qu'il ne serait pas possible de produire automatiquement des ex�cutables aussi efficaces � partir de langages de haut niveau . Un bon compilateur  ne peut donc se contenter de traduire na�vement le langage de haut niveau, il doit l'optimiser. Ces optimisations, associ�es au gain d'�chelle offert par l'abstraction, a permis la g�n�ralisation de l'utilisation de langages de haut niveau.
""",
"2":"""
Un compilateur ne traduit pas forc�ment un langages en code machine, il peut produire du code dans un langage interm�diaire qui sera ensuite lui-m�me compil� (par exemple, le langage interm�diaire peut �tre du C) ou interpr�t� (par exemple, du bytecode).
""",
"3":"""
La production d'un compilateur comprend une succession d'�tapes importantes, impl�ment�e par diff�rents modules :
""",
"31bold1":"""
-<pr�processeur> :""",
"4":"""est un programme qui proc�de � des transformations sur un code source, avant l'�tape de traduction ou bien la compilation.
""",
"41bold2":"-<analyseur lexical> :",
"5":"""grouper les lettres pour former des mots (lex�mes). L'analyseur est un automate fini dont les �tats terminaux sont associ�s � des actions (traduction, �mission d�un code caract�risant le lex�me).
""",
"51bold3":"-<analyseur syntaxique> :",
"6":"""Les langages r�guliers sont insuffisants pour sp�cifier la structure d'un programme. Il est n�cessaire de reconna�tre des constructions imbriqu�es, comme les blocs, les boucles, les expressions arithm�tiques, parenth�s�es... Pour ces constructions il est n�cessaire d'avoir une pile, donc on parle aux langages alg�briques qui sont reconnus par des automates � pile.
""",
"61bold4":"-<analyse s�mantique, typage >:",
"7":"""Pour d�finir un langage de programmation, il ne suffit pas de d�crire sa syntaxe, c'est-�-dire l'ensemble des expressions valides dans ce langage. Il faut �galement d�crire sa s�mantique, c'est-�-dire comment ces expressions seront interpr�t�es.
""",
"71bold5":"-<g�n�rateur de code interm�diaire> :",
"8":"""c'est le coeur du compilateur, apr�s avoir v�rifier les port�es et les types, doit traduire l'arbre de Syntaxe abstraite en Code Interm�diaire. Ensuite le Back-End du compilateur traduit le Code Interm�diaire en Assembleur.
""",
"81bold6":"-<optimisation de code> :",
"9":"""L'optimalit� du code est ind�cidable, puisque le probl�me de savoir si deux programmes ont le m�me comportement (terminent ou non) sur toutes les entr�es est ind�cidable.
""",
"91bold7":"-<g�n�rateur de code assembleur>"
}
}


dictionnaire2={
"contenu":{
"0":"""
Un automate fini (on dit parfois, par une traduction litt�rale maladroite de
l'anglais, machine � �tats finis, au lieu de machine avec un nombre fini d'�tats),
state automaton ou finite state machine (FSA, FSM), est une machine abstraite
qui est un outil fondamental en math�matiques discr�tes et en informatique. On les
retrouve dans la mod�lisation de processus, le contr�le, les protocoles de communication, la v�rification de programmes, la th�orie de la calculabilit�, dans l��tude
des langages formels et en compilation. Ils sont utilis�s dans la recherche des motifs
dans un texte.
""",
"1":"""
Les automates finis reconnaissent exactement des langages rationnels. Ce sont
les machines les plus simples dans la hi�rarchie de Chomsky, et par cons�quent ils
sont moins puissants que les automates � pile 5 et, bien entendu, que les machines
de Turing.
""",
"2":"""
Un automate est constitu� d'�tats et de transitions. Son comportement est dirig� par un mot fourni en entr�e : l'automate passe d'�tat en �tat, suivant les transitions, � la lecture de chaque lettre de l'entr�e
""",
"3":"""
L'automate est dit � fini � car il poss�de un nombre fini d'�tats : il ne dispose donc que d'une m�moire born�e. On peut tr�s bien consid�rer des automates sans limitation sur le nombre d'�tats : la th�orie qui en r�sulte est tr�s analogue � la th�orie habituelle.Un automate fini peut �tre vu comme un graphe orient� �tiquet� :les �tats sont les sommets et les transitions sont les ar�tes �tiquet�es. L'�tat initial est marqu� par une fl�che entrante ; un �tat final est, selon les auteurs, soit doublement cercl�, soit marqu� d'une fl�che sortante.
""",
"4":"""
Une autre fa�on commode de repr�senter un automate fini est sa table de transition. Elle donne, pour chaque �tat et chaque lettre, l'�tat d'arriv�e de la transition.
"""
}
}