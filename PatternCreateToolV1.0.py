import tkinter as TK
import ctypes
from tkinter import MULTIPLE

softwareversion = 'V1.0'
mainwindow = TK.Tk()

#调用api设置成由应用程序缩放
ctypes.windll.shcore.SetProcessDpiAwareness(1)
#调用api获得当前的缩放因子
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
#设置缩放因子
mainwindow.tk.call('tk', 'scaling', ScaleFactor/75)
# mainwindow.rowconfigure(1,weight=1)
# mainwindow.columnconfigure(0,weight=1)
mainwindow.geometry('800x600')
mainwindow.title("PatternCreateTool" + softwareversion)
mainwindow.config(bg="#F0FFFF")
############################
def GetInfo():
    pass
############################
I2CGUI = TK.Frame(mainwindow,bg="#F0E68C",bd=10,height=400,width=200)
SPIGUI = TK.Frame(mainwindow,bg="#1E90FF",bd=10,height=200,width=200)
UARTGUI = TK.Frame(mainwindow,bg="#8FBC8F",bd=10,height=200,width=200)
TK.Label(I2CGUI,text="I2C",font=("Bahnschrift",14),bg="#F0E68C").grid(column=0,row=0,columnspan=4)
TK.Label(SPIGUI,text="SPI",font=("Bahnschrift",12)).grid(column=0,row=0)
TK.Label(UARTGUI,text="UART",font=("Bahnschrift",12)).grid(column=0,row=0)

I2CGUISTRING1 = TK.StringVar()
I2CGUISTRING2 = TK.StringVar()
I2CGUISTRING3 = TK.StringVar()
I2CGUISTRING1.set("TS1")
I2CGUISTRING2.set("*.csv")
I2CGUISTRING3.set("SCL,SDA")
TK.Label(I2CGUI,text="SlaveID",bg="#F0E68C",font=("Consolas",10)).grid(column=0,row=1)
TK.Label(I2CGUI,text="Address",bg="#F0E68C",font=("Consolas",10)).grid(column=0,row=2)
TK.Label(I2CGUI,text="Data",bg="#F0E68C",font=("Consolas",10)).grid(column=0,row=3)
TK.Label(I2CGUI,text="WFTName",bg="#F0E68C",font=("Consolas",10)).grid(column=2,row=1)
TK.Label(I2CGUI,text="PatternName",bg="#F0E68C",font=("Consolas",10)).grid(column=2,row=2)
TK.Label(I2CGUI,text="SignalNames",bg="#F0E68C",font=("Consolas",10)).grid(column=2,row=3)
TK.Label(I2CGUI,text="CreateMode",bg="#F0E68C",font=("Consolas",10)).grid(column=0,row=4)
I2CENTRY1 =  TK.Entry(I2CGUI)
I2CENTRY2 =  TK.Entry(I2CGUI)
I2CENTRY3 =  TK.Entry(I2CGUI)
I2CENTRY4 =  TK.Entry(I2CGUI,textvariable=I2CGUISTRING1)
I2CENTRY5 =  TK.Entry(I2CGUI,textvariable=I2CGUISTRING2)
I2CENTRY6 =  TK.Entry(I2CGUI,textvariable=I2CGUISTRING3)
I2CENTRY1.grid(column=1,row=1)
I2CENTRY2.grid(column=1,row=2)
I2CENTRY3.grid(column=1,row=3)
I2CENTRY4.grid(column=3,row=1)
I2CENTRY5.grid(column=3,row=2)
I2CENTRY6.grid(column=3,row=3)
I2CBUTTON1 = TK.Button(I2CGUI,text="输入生成Pattern",activeforeground="#2F4F4F",activebackground="#00BFFF"
                       ,bg="#87CEFA",bd=6
                       ,command=GetInfo)
I2CBUTTON1.grid(column=3,row=4)
I2CSELECTCONFIG = [("Driver",1),("Compare",2)]
I2CSELECT = TK.IntVar()
I2CSELECT.set(0) #默认选择Dirver
TK.Radiobutton(I2CGUI,text="Driver",bg="#008B8B",variable=I2CSELECT,value=0).grid(column=1,row=4)
TK.Radiobutton(I2CGUI,text="Compare",bg="#008B8B",variable=I2CSELECT,value=1).grid(column=2,row=4)

# I2CMSG1 = TK.Message(I2CGUI,text="若不指定生成的文件名，将生成Address_Data的组合文件名:)",bg="#808080",width=400)
# I2CMSG1.grid(column=0,row=8,columnspan=4)
TK.Label(I2CGUI,text="Multi_SlaveID",bg="#F0E68C",font=("Consolas",10)).grid(column=0,row=5)
TK.Label(I2CGUI,text="Multi_DataList",bg="#F0E68C",font=("Consolas",10)).grid(column=0,row=6)
I2CMSG2 = TK.Message(I2CGUI,text="6A",bg="#BDB76B",width=400)
I2CMSG2.grid(column=1,row=5)

I2CLISTBOX = TK.Listbox(I2CGUI,selectmode=MULTIPLE,height=8)
LIST = [
    "D,0x32aa,0x30,",
    "D,0x32ab,0x3f",
    "C,0x3000,0x00,",
    "C,0x3000,0x01,",
    "C,0x3000,0x02,",
    "C,0x3000,0x03,",
    "C,0x3000,0x04,",
    "C,0x3000,0x05,",
    "C,0x3000,0x06,",
    "C,0x3000,0x07,",
    "C,0x3000,0x08,",
        ]
for var in range(0,len(LIST)):
    I2CLISTBOX.insert(var,LIST[var])
I2CLISTBOX.grid(column=1,row=6,columnspan=2)
# I2CSCROLLBAR.config(command = I2CLISTBOX.yview)
I2CGUI.grid(column=0,row=0)
I2CBUTTON2 = TK.Button(I2CGUI,text="导入配置文件",activeforeground="#2F4F4F",activebackground="#00BFFF"
                       ,bg="#87CEFA",bd=6
                       ,command=GetInfo)
I2CBUTTON2.grid(column=0,row=7)
I2CBUTTON2 = TK.Button(I2CGUI,text="配置文件生成Pattern",activeforeground="#2F4F4F",activebackground="#00BFFF"
                       ,bg="#87CEFA",bd=6
                       ,command=GetInfo)
I2CBUTTON2.grid(column=1,row=7,columnspan=2)



SPIGUI.grid(column=1,row=1)
UARTGUI.grid(column=2,row=2)
mainwindow.mainloop()