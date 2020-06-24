import tkinter as tk
from tkinter import ttk #css for tkinter

import matplotlib
matplotlib.use("TkAgg") #backend of matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

LARGE_FONT=("Verdana",12)

class SeaofBTCapp(tk.Tk): #This class will inherit the attributes and methods of the class tk
                          #So Frame, grid_rowconfigure... is a method within tk.Tk
    def __init__(self,*args,**kwargs):
        
        super().__init__(*args,**kwargs) #throw the inputs into SeaofBTCapp to be processed by tk.Tk
        
        #icon=tk.Image("photo",file="test_icon.png") Cannot add icon in linux/mac
        #super().call('wm','iconphoto',_w,icon)
        
        super().wm_title("sea of BTC client")#If you go to the source code, the Tk class is a subclass of the
                                             #Wm and misc class, so you can access the methods (i.e. wm_title() ) inside those
                                             #classes using Tk!
        
        container = tk.Frame(self) #container is the window, Frame defines the edge of the window

        #To include stuff into the Frame, you can use pack or grid. Here we use pack
        
        container.pack(side="top", fill="both", expand=True)
        #side: what side you want to pack the stuff to
        #Fill will fill in the space you alloted the pack to
        #Expand=true will allow the window to be resized normally (try putting expand=false and see the effect)
        
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        self.frames={} #The frames will be inside a dictionary
        
        for F in (StartPage,PageOne,PageTwo,PageThree): #This initializes each frame; frame = page
            self.frames[F]=F(container,self) #StartPage ... are classes defined below
            self.frames[F].grid(row=0,column=0, sticky="nsew")
            
        self.show_frame(StartPage)

    def show_frame(self,cont):
         frame=self.frames[cont] 
         frame.tkraise()
        
class StartPage(tk.Frame): #Each page inherits from the Frame class of tk package. It is called in the for loop
                           #in the SeaofBTC class above.
    
    def __init__(self,parent,button): 
        super().__init__(parent) #The parent argument here is container, which is processed by super()
        
        #This initializes the startpage window
        label = ttk.Label(self,text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        #This initializes the button in this window
        button1=ttk.Button(self,text="visit page 1",
                          command=lambda: button.show_frame(PageOne))
        #lambda is used so that the function is not run on the first iteration
                                                    #of the loop
        button1.pack()
        
        #This initializes the button in this window
        button2=ttk.Button(self,text="visit page 2",
                          command=lambda: button.show_frame(PageTwo))
        #lambda is used so that the function is not run on the first iteration
                                                    #of the loop
        button2.pack()
        
        #This initializes the button in this window
        button3=ttk.Button(self,text="visit graph page",
                          command=lambda: button.show_frame(PageThree))
        #lambda is used so that the function is not run on the first iteration
                                                    #of the loop
        button3.pack()


class PageOne(tk.Frame):
    def __init__(self,parent,button):
        super().__init__(parent)
        
        #This initializes the startpage window
        label = ttk.Label(self,text="Page 1", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        #This initializes the button in this window
        button1=ttk.Button(self,text="Back to start",
                          command=lambda: button.show_frame(StartPage))
        #lambda is used so that the function is not run on the first iteration
                                                    #of the loop
        button1.pack()
        
        button2=ttk.Button(self,text="Go to page 2",
                          command=lambda: button.show_frame(PageTwo))
        #lambda is used so that the function is not run on the first iteration
                                                    #of the loop
        button2.pack()

class PageTwo(tk.Frame):
    def __init__(self,parent,button):
        super().__init__(parent)
        
        #This initializes the startpage window
        label = ttk.Label(self,text="Page 2", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        #This initializes the button in this window
        button1=ttk.Button(self,text="Back to start",
                          command=lambda: button.show_frame(StartPage))
        #lambda is used so that the function is not run on the first iteration
                                                    #of the loop
        button1.pack()
        
        #This initializes the button in this window
        button2=ttk.Button(self,text="Back to page 1",
                          command=lambda: button.show_frame(PageOne))
        #lambda is used so that the function is not run on the first iteration
                                                    #of the loop
        button2.pack()

class PageThree(tk.Frame):
    def __init__(self,parent,button):
        super().__init__(parent)
        
        #This initializes the startpage window
        label = ttk.Label(self,text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        #This initializes the button in this window
        button1=ttk.Button(self,text="Back to start",
                          command=lambda: button.show_frame(StartPage))
        #lambda is used so that the function is not run on the first iteration
                                                    #of the loop
        button1.pack()
        
        #This initializes the button in this window
        button2=ttk.Button(self,text="Back to page 1",
                          command=lambda: button.show_frame(PageOne))
        #lambda is used so that the function is not run on the first iteration
                                                    #of the loop
        button2.pack()
        
app=SeaofBTCapp()
app.mainloop()
