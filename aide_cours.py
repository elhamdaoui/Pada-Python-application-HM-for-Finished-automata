# -*-coding:Latin-1 -*

#===============================================================================
__author__ = "abdelmajid"
__date__ = "$8 juin 2015 01:54:48$"
__doc__ = """
c'est un module qui contient une aide comme une classe Text.
"""
#===============================================================================
from tkinter import *
import cours.introduc,cours.def_form,\
cours.auto_finis,cours.auto_asy,cours.lang_rat,\
    cours.re_lang_r,cours.mini_afd

#===============================================================================

class CoursAuto(Toplevel):
    """
    c'est l'initialisateur du classe
    """
    
    def __init__(self,master):
        """
        
        """
        Toplevel.__init__(self,master)
        self.title("cours sur les automates finis déterministes")
        pane= PanedWindow(self, opaqueresize=1, sashcursor='', \
                                     showhandle=1, handlesize=0, handlepad=1, \
                                     sashrelief='sunken', sashpad=1, sashwidth=1, \
                                     orient=HORIZONTAL, relief='ridge', bd=2)
        self.menu = PanedWindow(pane, opaqueresize=1, sashcursor='', \
                                     showhandle=1, handlesize=0, handlepad=1, \
                                     sashrelief='sunken', sashpad=1, sashwidth=1, \
                                     orient=VERTICAL, relief='ridge', bd=2, bg='#5FBCA3')
        self.ajt_bnts_menu()
        pane.add(self.menu)#.pack(side=LEFT,fill=Y)

        self.text2 = Text(pane, height=20,tabs=('2c', '4.5c', 'right', '9c', 'center', '13c', 'numeric'))
        print(self.text2.config(takefocus=1))
        scroll = Scrollbar(self, command=self.text2.yview,width=5)
        self.text2.configure(yscrollcommand=scroll.set)
        self.text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        #mes styles
        self.text2.tag_configure('section', font=('Verdana', 18, 'bold'),foreground='#ef6042')
        self.text2.tag_configure('subsection', font=('Andalus', 15, 'bold'),foreground='green')
        self.text2.tag_configure('textbold', font=('Andalus', 12, 'bold'))
        self.text2.tag_configure('textnormal', font=('Tw Cen MT', 12, 'normal'), foreground='#3730aa')
        pane.add(self.text2)
        scroll.pack(side=RIGHT,expand =NO,fill=Y)
        pane.pack(fill=BOTH,expand=YES,padx=1)
        
    def ajt_bnts_menu(self):
        """
        
        """
        btns=[0]*7
        btns[0]=Button(self.menu,text="Introduction",bg='teal',command=self.introduction)
        btns[1]=Button(self.menu,text="definitions formelle",bg='teal',command=self.def_form)
        btns[2]=Button(self.menu,text="Automate finis déterministe",bg='teal',command=self.auto_finis)
        btns[3]=Button(self.menu,text="Automates asynchrones",bg='teal',command=self.auto_asy)
        btns[4]=Button(self.menu,text="Langages rationnels et reconnaissables",bg='teal',command=self.lang_rat)
        btns[5]=Button(self.menu,text="ER et langages rationnels",bg='teal',command=self.re_lang_r)
        btns[6]=Button(self.menu,text="minimisation d'un AFD",bg='teal',command=self.mini_afd)
        for i in range(len(btns)):
            self.menu.add(btns[i])
    
    def introduction(self):
        """
        """
        self.text2.configure(state='normal')
        self.text2.delete('1.0',END)
        self.text2.insert(END,'\nCompilation\n','section')
        self.compiler_dict(cours.introduc.dictionnaire1)
        self.text2.insert(END,'\n\nLes automates finis\n','section')
        self.compiler_dict(cours.introduc.dictionnaire2)
        self.text2.configure(state='disabled')
                
    def def_form(self):
        """
        """
        self.text2.configure(state='normal')
        self.text2.delete('1.0',END)
        self.text2.insert(END,'\nDéfinitions formelles\n','section')
        self.compiler_dict(cours.def_form.dictionnaire1)
        self.text2.configure(state='disabled')
        
    def auto_finis(self):
     """
     """
     self.text2.configure(state='normal')
     self.text2.delete('1.0',END)
     self.text2.insert(END,'\nAutomate finis déterministe\n','section')
     self.compiler_dict(cours.auto_finis.dictionnaire1)
     self.text2.configure(state='disabled')
        
    def auto_asy(self):
        """
        """
        self.text2.configure(state='normal')
        self.text2.delete('1.0',END)
        self.text2.insert(END,'\nAutomates asynchrones\n','section')
        self.compiler_dict(cours.auto_asy.dictionnaire1)
        self.text2.configure(state='disabled')
    
    def lang_rat(self):
        """
        """
        self.text2.configure(state='normal')
        self.text2.delete('1.0',END)
        self.text2.insert(END,'\nLangages rationnels et langages reconnaissables :\n le théorème de Kleene\n','section')
        self.compiler_dict(cours.lang_rat.dictionnaire1)
        self.text2.configure(state='disabled')
    
    def re_lang_r(self):
        """
        """
        self.text2.configure(state='normal')
        self.text2.delete('1.0',END)
        self.text2.insert(END,'\nExpressions rationnelles et langages rationnels\n','section')
        self.compiler_dict(cours.re_lang_r.dictionnaire1)
        self.text2.configure(state='disabled')
   
    def mini_afd(self):
        """
        """
        self.text2.configure(state='normal')
        self.text2.delete('1.0',END)
        self.text2.insert(END,"\nMinimisation d'un automate finis déterministe\n",'section')
        self.compiler_dict(cours.mini_afd.dictionnaire1)
        self.text2.configure(state='disabled')

        
    def compiler_dict(self,diction):
        """
        une méthode qui permette de bien présenter un texte d'un dictionnaire.
        """
        if type(diction) is dict:
            keys=sorted(diction.keys())
            for k in keys:
                v=diction[k]
                if "subsection" in k:
                    self.text2.insert(END,v['titre']+"\n",'subsection')
                    self.compiler_contenu(v['contenu'])
                if "contenu" in k:
                    self.compiler_contenu(v)
    
    def compiler_contenu(self,diction):
        """
        méthode qui permette de compiler le contenu d'un dict
        """
        if type(diction)is dict:
            keys=sorted(diction.keys())
            for k in keys:
                v=diction[k]
                if "bold" in k:
                    self.text2.insert(END,v,"textbold")
                elif "image" in k:
                    photo=PhotoImage(file=v)
                    win=Button(self.text2,bg='cyan',text='./imgs/ex1_moore_c.gif',image=photo)
                    win.image=photo
                    self.text2.insert(END,'\n')
                    self.text2.window_create(END, window=win)
                elif "widget" in k:
                    pass
                else:
                    self.text2.insert(END,v,"textnormal")