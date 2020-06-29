#follows tutorial from sentdex on tkinter tutorial
#hahaha
import tkinter as tk
from tkinter import ttk #css for tkinter

import matplotlib
matplotlib.use("TkAgg") #backend of matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from matplotlib import pyplot as plt

import matplotlib.animation as animation
from matplotlib import style
style.use("ggplot")#For background of graph. Options are dark_background, ggplot and grayscale
import matplotlib.dates as mdates
import matplotlib.ticker as mticker

import warnings
warnings.filterwarnings("ignore")

import urllib
import json

import pandas as pd
import numpy as np
LARGE_FONT=("Verdana",12)
NORM_FONT=("Verdana",10)
SMALL_FONT=("Verdana",8)

resampleSize="15Min"
dataPace="tick"
candleWidth=0.008
paneCount=1
chartLoad=1
def changeTimeFrame(tf):
    global DataPace
    global DatCounter
    
    if tf=='7d' and resampleSize=="1Min":
        popupmsg("Too much data chosen, choose a smaller time frame or higher OHLC interval")
    else:
        DataPace=tf
        DatCounter=9000
        
        
def changeSampleSize(size,width):
    global resampleSize
    global DatCounter
    global candleWidth
    if tf=='7d' and resampleSize=="1Min":
        popupmsg("Too much data chosen, choose a smaller time frame or higher OHLC interval")
    elif DataPace=="tick":
        popupmsg("youre currently viewing tick data, not OHLC")
    else:
        resampleSize=size
        DatCounter=9000
        candleWidth=width
        
f = Figure(figsize=(10,6),dpi=100) #instantiate a Figure class
a=f.add_subplot(111) #specify no of plots

def popupmsg(msg):
    popup=tk.Tk()
        
    popup.wm_title("!")
    label=tk.Label(popup,text=msg,font=NORM_FONT)
    label.pack(side="top",fill="x",pady=10)
    B1=ttk.Button(popup,text="Okay",command=popup.destroy())
    B1.pack()
    popup.mainloop()
    
def animate(i):
    global refreshrate
    global DatCounter
    
    #a=plt.subplot2grid((6,4),(0,0),rowspan=5,colspan=4)
    #a2=plt.subplot2grid((6,4),(0,0),rowspan=1,colspan=4,sharex=a)
    
    dataLink="https://bitbay.net/API/Public/BTCEUR/trades.json"
    data=urllib.request.urlopen(dataLink)
    data=data.read()
    data=json.loads(data)
    data=pd.DataFrame(data) #pandas DataFrame will convert
                            #the keys into heading of a table and
                            #the values of each key as the rows
    
    data["date"]=np.array(data['date']).astype("datetime64[s]") 
    allDates=(data['date']).tolist() #create a list of the dates

    buys=data[data['type']=="buy"] #filter data table to only include rows with 'buy' type
    buys['date']=np.array(buys['date']).astype("datetime64[s]") #convert dates in data table to normal format
    buyDates=(buys['date']).tolist() #create a list of the dates
    
    sells=data[data['type']=="sell"]
    sells['date']=np.array(sells['date']).astype("datetime64[s]")
    sellDates=(sells['date']).tolist()
    a.clear()
    
    a.plot_date(buyDates,buys["price"], "#00A3E0",label="buys")
    a.plot_date(sellDates,sells["price"],"#183A54",label="sells") #We use hex color in #
    
    title="BTC-e BTCUSD Prices\nLast Price: {}".format(str(data['price'][len(data.columns)]))
    a.set_title(title)
    
    a.legend(bbox_to_anchor=(0,1.02,1,.102),loc=3,
             ncol=2,borderaxespad=0)
                    
    
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
        
        menubar=tk.Menu(container) #create a dropdown like "file", "edit", ...
        #now define the options inside the dropdown
        filemenu=tk.Menu(menubar,tearoff=0) #tearoff will create a new window for each option
        filemenu.add_command(label="save settings", command=lambda:popupmsg("Not supported just yet!"))
        filemenu.add_separator() #bar between options on the dropdown
        filemenu.add_command(label="Exit",command=quit)
        #create the "file" menubar
        menubar.add_cascade(label="File",menu=filemenu) 
        
        currencyChoice=tk.Menu(menubar,tearoff=0)
        currencyChoice.add_command(label="EUR",command=lambda:changeCurrency("EUR"))
        currencyChoice.add_command(label="USD",command=lambda:changeCurrency("USD"))
        currencyChoice.add_command(label="GBP",command=lambda:changeCurrency("GBP"))
        menubar.add_cascade(label="currency",menu=currencyChoice)
        
        dataTF = tk.Menu(menubar,tearoff=0)
        dataTF.add_command(label="Now",command=lambda:changeTimeFrame('tick'))
        dataTF.add_command(label="1 Day",command=lambda:changeTimeFrame('1day'))
        dataTF.add_command(label="3 Days",command=lambda:changeTimeFrame('3days'))
        dataTF.add_command(label="1 Week",command=lambda:changeTimeFrame('1week'))
        menubar.add_cascade(label="Data Time Frame",menu=dataTF)
        
        OHLCI=tk.Menu(menubar,tearoff=0)#open high low close interval
        OHLCI.add_command(label="tick",command=lambda:changeTimeFrame('tick'))
        OHLCI.add_command(label="1 minute",command=lambda:changeTimeFrame('1min',0.0005))
        OHLCI.add_command(label="5 minute",command=lambda:changeTimeFrame('5min',0.003))
        OHLCI.add_command(label="15 minute",command=lambda:changeTimeFrame('15min',0.008))
        OHLCI.add_command(label="30 minute",command=lambda:changeTimeFrame('30min',0.016))
        OHLCI.add_command(label="1 hour",command=lambda:changeTimeFrame('1H',0.032))
        OHLCI.add_command(label="3 hour",command=lambda:changeTimeFrame('3H',0.096))
        menubar.add_cascade(label="OHLCI",menu=OHLCI)


        
        
        tk.Tk.config(self,menu=menubar)
        
        self.frames={} #The frames will be inside a dictionary
        
        for F in (StartPage,BTCE_page): #This initializes each frame; frame = page
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
        label = tk.Label(self,text="""ALPHA Bitcoin trading application
                                      Use at your own risk!
                                      No warranty promise!""",bg="red",fg="white",font=LARGE_FONT)
        #passing self here since the label function takes in a frame object 
        label.pack(fill=tk.X,pady=5) #tk.X fmakes 
        
        
        #This initializes the button in this window
        button1=ttk.Button(self,text="Agree",
                          command=lambda: button.show_frame(BTCE_page))
        #lambda is used so that the function is not run on the first iteration
                                                    #of the loop
        button1.pack()
        
        #This initializes the button in this window
        button2=ttk.Button(self,text="Disagree",
                          command=lambda: button.show_frame(StartPage))
        #lambda is used so that the function is not run on the first iteration
                                                    #of the loop
        button2.pack()
        

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


class BTCE_page(tk.Frame):
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
#app.geometry("800x600") #("1280x720")
ani=animation.FuncAnimation(f,animate,interval=5000)#send the frame, the animate function and the interval
app.mainloop()

