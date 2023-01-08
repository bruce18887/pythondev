import time
import tkinter
import ReadInIFile as RINI
import ttkbootstrap as ttk
from ttkbootstrap import utility
from ttkbootstrap.constants import *
import re
########################
_softwareversion = 'V1.2'
########################
I2C_RINI_OBJ =  RINI.I2C('test.ini')
def GUIConsole_Print(arg):
    GUIConsoleSCR.insert('end',
        time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime())+'  ' +arg + '\n')#末尾插入
    GUIConsoleSCR.see(END)
def OnTreeViewSelect(event):
    # print("Begin")
    for var in I2C_RegListBox.selection():
        GUIConsole_Print(I2C_RegListBox.set(var)['seq']+' ')
        # GUIConsoleStr.set(I2C_RegListBox.set(var)['seq'])
        # GUIConsoleStr.set(I2C_RegListBox.item(var,option="values")[0])
    # print("End")
def OnTreeViewHeaderPressed():
    GUIConsole_Print("指令框内的为待转化的寄存器指令:),点击CreatePattern会转换里面所有的指令")
def AddRegSequence():
    GUIConsole_Print("你点击了AddRegSequence")
def DeleteSelectSequence():
    GUIConsole_Print("Now excute DeleteSelectSequence()")
    for SelectIID in I2C_RegListBox.selection():#selection 返回选择的所有IID，用循环逐个删除
        GUIConsole_Print(I2C_RegListBox.set(SelectIID)['seq'] + ' 已经删除')
        I2C_RegListBox.delete(SelectIID)

def ReadFromInIFile():
    # GUIConsole_Print("你点击了ReadFromInIFile")
    GUIConsole_Print(I2C_RINI_OBJ.ReadSlaveID())
    GUIConsole_Print(I2C_RINI_OBJ.ReadWFTName())
    GUIConsole_Print(I2C_RINI_OBJ.ReadSignals())
    for Data in I2C_RINI_OBJ.ReadDataAfterCheck():
        GUIConsole_Print(Data)
def CreatePattern():
    GUIConsole_Print("你点击了CreatePattern")
# def
class GUIMessageGet:
    def __init__(self):
        print("Create GUIMessageGet Obj")
        pass
########################
master = ttk.Window(
        title="PatternCreateTool " + _softwareversion,
        size=(800,700),
        themename="solar",
        # All suport theme
        # flatly  litera  minty  lumen sandstone yeti pulse
        # united morph journal darkly superhero solar  cyborg vapor simplex  cerculean
        resizable=(False, False)
    )

# masterstyle = master.style()
# form variables
GUIConsoleStr = ttk.StringVar(value="Wait ... ...")
I2C_strWFT = ttk.StringVar(value="TS1")
I2C_strSignal = ttk.StringVar(value="SCL,SDA")
I2C_strFileName = ttk.StringVar(value="*.csv")
I2C_ModeSelect = ttk.IntVar(value=0)

NoteBookPage = ttk.Notebook(
    master=master
)
I2C_GUI_Frame = ttk.Frame(master=NoteBookPage)
I2C_GUI_Frame.pack()
########################################
I2C_Setting = ttk.Labelframe(master=I2C_GUI_Frame, text="I2C_Setting")
I2C_Setting.pack(fill=X, expand=True,pady=6)
ttk.Label(master=I2C_Setting, text="SlaveID").grid(row=0, column=0,padx=4,pady=4)
ttk.Label(master=I2C_Setting, text="Address").grid(row=1, column=0)
ttk.Label(master=I2C_Setting, text="Data").grid(row=2, column=0,padx=4,pady=4)
ttk.Label(master=I2C_Setting, text="WFT").grid(row=0, column=2,padx=4,pady=4)
ttk.Label(master=I2C_Setting, text="Signal").grid(row=1, column=2,padx=4,pady=4)
ttk.Label(master=I2C_Setting, text="FileName").grid(row=2, column=2,padx=4,pady=4)
ttk.Label(master=I2C_Setting, text="CreateMode").grid(row=3, column=0,padx=4,pady=8)
I2C_SlaveID = ttk.Entry(master=I2C_Setting)
I2C_Address = ttk.Entry(master=I2C_Setting)
I2C_Data = ttk.Entry(master=I2C_Setting)
I2C_WFT = ttk.Entry(master=I2C_Setting, textvariable=I2C_strWFT)
I2C_Signal = ttk.Entry(master=I2C_Setting, textvariable=I2C_strSignal)
I2C_FileName = ttk.Entry(master=I2C_Setting, textvariable=I2C_strFileName)
I2C_SlaveID.grid(row=0, column=1,padx=4,pady=4)
I2C_Address.grid(row=1, column=1,padx=4,pady=4)
I2C_Data.grid(row=2, column=1,padx=4,pady=4)
I2C_WFT.grid(row=0, column=3,padx=4,pady=4)
I2C_Signal.grid(row=1, column=3,padx=4,pady=4)
I2C_FileName.grid(row=2, column=3,padx=4,pady=4)
# for PatternCreateMode
I2C_DriverMode =  ttk.Radiobutton(I2C_Setting, text="Driver", variable=I2C_ModeSelect, value=0)
I2C_DriverMode.bind("<ButtonRelease-1>",lambda event:GUIConsole_Print("Set CreateMode to Driver"))
I2C_DriverMode.grid(row=3, column=1)
I2C_CompareMode = ttk.Radiobutton(I2C_Setting, text="Compare", variable=I2C_ModeSelect, value=1)
I2C_CompareMode.bind("<ButtonRelease-1>",lambda event:GUIConsole_Print("Set CreateMode to Compare"))
I2C_CompareMode.grid(row=3, column=2)
########################################
I2C_RegMessage = ttk.Labelframe(master=I2C_GUI_Frame, text="I2C_RegMessage")
I2C_RegMessage.pack(side=LEFT, fill=BOTH,expand=True,pady=8,padx=5)
ttk.Label(master=I2C_RegMessage, text="Trans_SlaveID").grid(row=0, column=0,pady=6,padx=4)
ttk.Label(master=I2C_RegMessage, text="6A").grid(row=0, column=1,pady=6,padx=4)
ttk.Label(master=I2C_RegMessage, text="Trans_RegList").grid(row=1, column=0,pady=6,padx=4)
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
I2C_RegListBox = ttk.Treeview(I2C_RegMessage, columns="seq", show=HEADINGS)
for row in LIST:
    I2C_RegListBox.insert('', END, values=row)
I2C_RegListBox.heading(column="seq", text="指令",anchor='center',command=OnTreeViewHeaderPressed)
I2C_RegListBox.grid(row=1, column=1,pady=6,padx=4)
# I2C_RegListBox.column(0, width=200)
I2C_RegListBox.column(0, anchor=W,width=utility.scale_size(I2C_RegMessage, 125),stretch=False)
I2C_RegListBox.bind("<ButtonRelease-1>", OnTreeViewSelect)
########################################
I2C_CreateControl = ttk.Labelframe(master=I2C_GUI_Frame, text="I2C_CreateControl")
I2C_CreateControl.pack(side=RIGHT,fill=BOTH, expand=True,pady=8,padx=5)
ttk.Button(master=I2C_CreateControl,text="AddRegSequence",width=20,command=AddRegSequence)\
    .grid(row=0,column=0,ipady=5,padx=10,pady=10)
ttk.Button(master=I2C_CreateControl,text="DeleteSelectSequence",width=20,command=DeleteSelectSequence)\
    .grid(row=0,column=1,ipady=5,padx=10,pady=10)
ttk.Button(master=I2C_CreateControl,text="ReadFromInIFile",width=20,command=ReadFromInIFile)\
    .grid(row=1,column=0,ipady=5,padx=10,pady=10)
ttk.Button(master=I2C_CreateControl,text="CreatePattern",width=20,command=CreatePattern)\
    .grid(row=1,column=1,ipady=5,padx=10,pady=10)
########################################
GUIConsole = ttk.Labelframe(master=master, text="GUIConsole")
GUIConsole.pack(side=BOTTOM, fill=BOTH,expand=True,pady=8,padx=5)
# ttk.Label(GUIConsole,text="This will print some app log:)").grid(row=0,column=0,padx=10,pady=10)
# ttk.Label(GUIConsole,textvariable=GUIConsoleStr,font=("Consolas",10),anchor=W).grid(row=0,column=0)
GUIConsoleSCR =  ttk.ScrolledText(master=GUIConsole,height=4)
GUIConsoleSCR.grid(row=0,column=0)
for line in LIST:
        # GUIConsoleSCR.insert('end',
        # time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime())+'  ' +line + '\n')#末尾插入
        GUIConsole_Print(line)
GUIMouseRightMenu = ttk.Menu(master=master)
GUIMouseRightMenu.add_command(label="指令提示"
                    ,command=lambda:GUIConsole_Print("指令框内的为待转化的寄存器指令:),点击CreatePattern会转换里面所有的指令"))
GUIMouseRightMenu.add_separator()
GUIMouseRightMenu.add_command(label="生成提示"
                    ,command=lambda:GUIConsole_Print("Pattern生成仅根据Trans_SlaveID和Trans_Reg来使用预设模板生成"))
GUIMouseRightMenu.add_separator()
GUIMouseRightMenu.add_command(label="读取配置文件提示"
                    ,command=lambda:GUIConsole_Print("选择ini文件将自动导入所有信息"))
master.bind("<Button-3>", lambda event:GUIMouseRightMenu.post(event.x_root, event.y_root))
GUIEdgeTopMenu = ttk.Menu(master=master)
GUIEdgeTopMenu.add_command(label="文件")
GUIEdgeTopMenu.add_command(label="查看")

########################################
SPI_Setting = ttk.Labelframe(master=NoteBookPage, text="SPI_Setting")
SPI_Setting.pack()
ttk.Label(master=SPI_Setting, text="SlaveID").grid(row=0, column=0)
ttk.Label(master=SPI_Setting, text="Address").grid(row=1, column=0)
ttk.Label(master=SPI_Setting, text="Data").grid(row=2, column=0)
ttk.Label(master=SPI_Setting, text="WFT").grid(row=0, column=2)
ttk.Label(master=SPI_Setting, text="Signal").grid(row=1, column=2)
ttk.Label(master=SPI_Setting, text="FileName").grid(row=2, column=2)
SPI_SlaveID = ttk.Entry(master=SPI_Setting)
SPI_Address = ttk.Entry(master=SPI_Setting)
SPI_Data = ttk.Entry(master=SPI_Setting)
SPI_WFT = ttk.Entry(master=SPI_Setting)
SPI_Signal = ttk.Entry(master=SPI_Setting)
SPI_FileName = ttk.Entry(master=SPI_Setting)
SPI_SlaveID.grid(row=0, column=1)
SPI_Address.grid(row=1, column=1)
SPI_Data.grid(row=2, column=1)
SPI_WFT.grid(row=0, column=3)
SPI_Signal.grid(row=1, column=3)
SPI_FileName.grid(row=2, column=3)
########################################

########################################
UART_Setting = ttk.Labelframe(master=NoteBookPage, text="I2C_Setting")
UART_Setting.pack()
ttk.Label(master=UART_Setting, text="SlaveID").grid(row=0, column=0)
ttk.Label(master=UART_Setting, text="Address").grid(row=1, column=0)
ttk.Label(master=UART_Setting, text="Data").grid(row=2, column=0)
ttk.Label(master=UART_Setting, text="WFT").grid(row=0, column=2)
ttk.Label(master=UART_Setting, text="Signal").grid(row=1, column=2)
ttk.Label(master=UART_Setting, text="FileName").grid(row=2, column=2)
UART_SlaveID = ttk.Entry(master=UART_Setting)
UART_Address = ttk.Entry(master=UART_Setting)
UART_Data = ttk.Entry(master=UART_Setting)
UART_WFT = ttk.Entry(master=UART_Setting)
UART_Signal = ttk.Entry(master=UART_Setting)
UART_FileName = ttk.Entry(master=UART_Setting)
UART_SlaveID.grid(row=0, column=1)
UART_Address.grid(row=1, column=1)
UART_Data.grid(row=2, column=1)
UART_WFT.grid(row=0, column=3)
UART_Signal.grid(row=1, column=3)
UART_FileName.grid(row=2, column=3)
########################################
NoteBookPage.pack(fill=X)
NoteBookPage.add(child=I2C_GUI_Frame, text="I2C")
NoteBookPage.add(child=SPI_Setting, text="SPI")
NoteBookPage.add(child=UART_Setting, text="UART")
master.config(menu=GUIEdgeTopMenu)
master.position_center()
master.mainloop()