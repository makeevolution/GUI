#follows tutorial from sentdex on tkinter tutorial

import tkinter as tk
from tkinter import ttk #css for tkinter

import matplotlib
matplotlib.use("TkAgg") #backend of matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import matplotlib.animation as animation
from matplotlib import style
style.use("ggplot")#For background of graph. Options are dark_background, ggplot and grayscale

import urllib
import json

import pandas as pd
import numpy as np
LARGE_FONT=("Verdana",12)

f = Figure(figsize=(5,5),dpi=100) #instantiate a Figure class
a=f.add_subplot(111) #specify no of plots

def animate(i):
    pullData = open("sampleData.txt","r").read()
    dataList=pullData.split("\n")
    xList=[]
    yList=[]
    for eachLine in dataList:
        if len(eachLine)>1: #To make sure we are processing not an empty line; sometimes the data has an empty line
            x,y=eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
    a.clear()
    a.plot(xList,yList)
    
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
        
        #This initializes the startpage texxt widget
        label = tk.Label(self,text="Start Page",bg="red",fg="white",font=LARGE_FONT)
        #passing self here since the label function takes in a frame object 
        label.pack(fill=tk.X,pady=5) #tk.X fmakes 
        
        #initialize another widget
        label = tk.Label(self,text="Welcome",bg="blue",fg="white",font=LARGE_FONT)
        #passing self here since the label function takes in a frame object 
        label.pack(ipady=10)
        
        #This initializes the button in this window
        button1=ttk.Button(self,text="visit page 1",
                          command=lambda: button.show_frame(PageOne))
        #lambda is used so that the function is not run on the first iteration
                                                    #of the loop
        button1.pack(side=tk.LEFT)
        
        #This initializes the button in this window
        button2=ttk.Button(self,text="visit page 2",
                          command=lambda: button.show_frame(PageTwo))
        #lambda is used so that the function is not run on the first iteration
                                                    #of the loop
        button2.pack(side=tk.LEFT,padx=100)
        
        #This initializes the button in this window
        button3=ttk.Button(self,text="visit graph page",
                          command=lambda: button.show_frame(PageThree))
        #lambda is used so that the function is not run on the first iteration
                                                    #of the loop
        button3.pack(side=tk.RIGHT)


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
        

        #a.plot([range(1,8),range(3,10)]) #plot sample data on the given subplot
        
        #we would usually do a.show(), but here it will not plot on our gui
        
        canvas=FigureCanvasTkAgg(f,self) #with self, we send in our gui page as
        canvas.draw() #draw figure on canvas
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True) #pack the canvas on tkinter
        
        toolbar=NavigationToolbar2Tk(canvas,self) #with self, we send the 
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
app=SeaofBTCapp()
ani=animation.FuncAnimation(f,animate,interval=1000)#send the frame, the animate function and the interval
app.mainloop()
