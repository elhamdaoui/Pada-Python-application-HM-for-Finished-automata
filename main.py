# -*-coding:Latin-1 -*

#===============================================================================
__author__ = "abdelmajid"
__date__ = "$7 avr. 2015 02:30:24$"
__doc__="""
c'est le module 'main' 
"""
#===============================================================================
print("c'est parti , je vais commencer mon application PFE")
#===============================================================================
from auto_app import *
def animation():
    alp=AutoApp.fen.attributes('-alpha')
    if alp>0.2:
        AutoApp.fen.attributes('-alpha',alp-0.003)
        AutoApp.fen.after(10,animation)
    else:
        AutoApp.fen.geometry("+4000+2000")
        AutoApp()
AutoApp.fen.after(1000,animation)
AutoApp.fen.mainloop()
#a=AutoApp()
#a.tk.call("::tk::unsupported::MacWindowStyle", "style", a._w, "help", "none")
#a.mainloop()
#from test import *
