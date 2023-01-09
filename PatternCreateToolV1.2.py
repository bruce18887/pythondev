import time
# import tkinter
from tkinter import filedialog
import ReadInIFile as RINI
import ttkbootstrap as ttk
from ttkbootstrap import utility
from ttkbootstrap.constants import *
import re
########################
_softwareversion = 'V1.2'
########################
# I2C_RINI_OBJ =  RINI.I2C
GUIThemes = ("flatly","litera",  "minty",  "lumen", "sandstone", "yeti", "pulse",
            "united", "morph", "journal", "darkly" ,"superhero", "solar",
            "cyborg", "vapor", "simplex",  "cerculean")
def PatternTemplate():
    PatternTemplateFrame = ttk.Toplevel(master=master,title="Pattern模板",size=(1000,800))
    PatternTemplateFrame.position_center()
    PatternTemplateTreeView = ttk.Treeview(master=PatternTemplateFrame,
                                           columns=['label','wftname','sequence','signal1','signal2'],
                                           show=HEADINGS,
                                           height=40
                                           )
    PatternTemplateTreeView.heading(column="label", text="Label", anchor='center')
    PatternTemplateTreeView.heading(column="wftname", text="WFT", anchor='center')
    PatternTemplateTreeView.heading(column="sequence", text="sequence", anchor='center')
    PatternTemplateTreeView.heading(column="signal1", text="SCL", anchor='center')
    PatternTemplateTreeView.heading(column="signal2", text="SDA", anchor='center')
    PatternTemplateTreeView.grid(row=0,column=0,)
    ttk.Style().map('Treeview', background=[('selected', 'green')], foreground=[('selected', 'yellow')])
    PatternTemplateTreeView.column(column="label", anchor=CENTER,minwidth=75
                                   , width=utility.scale_size(PatternTemplateTreeView, 100), stretch=False)
    PatternTemplateTreeView.column(column="wftname", anchor=CENTER,minwidth=75
                                   , width=utility.scale_size(PatternTemplateTreeView, 100), stretch=False)
    PatternTemplateTreeView.column(column="sequence", anchor=CENTER,minwidth=75
                                   , width=utility.scale_size(PatternTemplateTreeView, 100), stretch=False)
    PatternTemplateTreeView.column(column="signal1", anchor=CENTER,minwidth=75
                                   , width=utility.scale_size(PatternTemplateTreeView, 100), stretch=False)
    PatternTemplateTreeView.column(column="signal2", anchor=CENTER,minwidth=75
                                   , width=utility.scale_size(PatternTemplateTreeView, 100), stretch=False)
    for intvar in range(0,10):
        PatternTemplateTreeView.insert('',END,values=['0','TS1','nop','0','0'])
    for intvar in range(0,10):
        PatternTemplateTreeView.insert('',END,values=['0','TS1','nop','1','0'])
    for intvar in range(0,10):
        PatternTemplateTreeView.insert('',END,values=['0','TS1','nop','H','H'])
    # defalut set for test now ,LIST has been deleted
    # for row in LIST:
    #     # I2C_RegListBox.insert('', END, values=row)
    #     TreeViewInsertValues(InputTreeViewControl=I2C_RegListBox,InputValues=row)

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
def EntryInputFormatCheck():
    pass
def TreeViewInsertValues(InputTreeViewControl,InputValues):
    #目前只有一列，插入一个string就行
    InputTreeViewControl.insert('', END, values=InputValues)
def AddRegSequence():
    # GUIConsole_Print("你点击了AddRegSequence")
    RegListBoxSetLabel = False #判断是否对I2CRegListBox 进行插入value
    TempI2C_SlaveID = I2C_SlaveID.get()
    TempI2C_SlaveID = re.sub(pattern=r'0[xX]',repl='',string=TempI2C_SlaveID,count=0)#先把0x去掉
    # print(re.match(r'(([a-f0-9]?)([a-f0-9])?)',Temp,re.I).span())

    if re.match(r'(([a-f0-9]?)([a-f0-9])?)',TempI2C_SlaveID,re.I).span() == (0,2):
        GUIConsole_Print('SlaveID = '+TempI2C_SlaveID)
        I2C_Trans_SlaveID.config(text=TempI2C_SlaveID)
        RegListBoxSetLabel = True
    else:
        GUIConsole_Print('I2C_SlaveID Wrong Format,Commant stoped')
        return
    TempI2C_Address = I2C_Address.get()
    TempI2C_Address = re.sub(pattern=r'0[xX]', repl='', string=TempI2C_Address, count=0)  # 先把0x去掉
    if re.match(r'([a-f0-9]?[a-f0-9]?[a-f0-9]?[a-f0-9]?)',TempI2C_Address,re.I).span() == (0,4):
        GUIConsole_Print('Address = '+ TempI2C_Address)
        RegListBoxSetLabel = True
    else:
        GUIConsole_Print('I2C_Address Wrong Format,Command stoped')
        return
    TempI2C_Data = I2C_Data.get()
    TempI2C_Data = re.sub(pattern=r'0[xX]',repl='',string=TempI2C_Data,count=0)#先把0x去掉
    if re.match(r'([a-f0-9]?[a-f0-9]?)',TempI2C_Data,re.I).span() == (0,2):
        GUIConsole_Print('Data = '+TempI2C_Data)
        RegListBoxSetLabel = True
    else:
        GUIConsole_Print('I2C_Data Wrong Format,Command stoped')
        return
    TempI2C_Signal = I2C_Signal.get()
    # print(re.match(r'((.*),(.*))',TempI2C_Signal,re.I))
    if re.match(r'((.*),(.*))',TempI2C_Signal,re.I):#检查信号名中间的分割逗号
        GUIConsole_Print('I2C_Signal = '+ TempI2C_Signal)
        RegListBoxSetLabel = True
    else:
        GUIConsole_Print('I2C_Signal Wrong Format,Command stoped')
        return
    TempI2C_strFileName = I2C_strFileName.get()
    if  re.match(r'[*].csv',TempI2C_strFileName) is not None:
        if re.match(r'[*].csv',TempI2C_strFileName).span()==(0,5):#如果没填，则用地址+数据补充
            I2C_strFileName.set(TempI2C_Address+'_'+TempI2C_Data+'.csv')
            GUIConsole_Print('PatternName Set '+I2C_strFileName.get())
            # Temp = I2C_strFileName.get()
            RegListBoxSetLabel = True
    elif re.match(r'(.*)_(.*).csv',TempI2C_strFileName) is not None:
        I2C_strFileName.set(TempI2C_Address + '_' + TempI2C_Data + '.csv')
        GUIConsole_Print('PatternName Set '+I2C_strFileName.get())
        RegListBoxSetLabel = True
    else:
        GUIConsole_Print('I2C_strFileName Wrong Format,Command stoped')
        return
    if RegListBoxSetLabel:
        TreeViewInsertValues(InputTreeViewControl = I2C_RegListBox
                             ,InputValues =(('D,'if I2C_ModeSelect.get()==0 else 'C,')
                             +'0x'+TempI2C_Address + ',0x' + TempI2C_Data+','))
        # GUIConsole_Print('PatternCreateModeSet to '+ ('Driver'if I2C_ModeSelect.get()==0 else 'Compare'))
def DeleteSelectSequence():
    GUIConsole_Print("Now excute DeleteSelectSequence()")
    for SelectIID in I2C_RegListBox.selection():#selection 返回选择的所有IID，用循环逐个删除
        GUIConsole_Print(I2C_RegListBox.set(SelectIID)['seq'] + ' 已经删除')
        I2C_RegListBox.delete(SelectIID)
def ReadFromInIFile():
    # GUIConsole_Print("你点击了ReadFromInIFile")
    filename = filedialog.askopenfilename(filetypes=[('ini','INI')])
    if filename != '':
         GUIConsole_Print(filename)
         I2C_RINI_OBJ = RINI.I2C(filename)
         I2C_Trans_SlaveID.config(text=I2C_RINI_OBJ.ReadSlaveID())
         # GUIConsole_Print(I2C_RINI_OBJ.ReadSlaveID())
         I2C_strWFT.set(I2C_RINI_OBJ.ReadWFTName())
         # GUIConsole_Print(I2C_RINI_OBJ.ReadWFTName())
         I2C_strSignal.set(I2C_RINI_OBJ.ReadSignals())
         # GUIConsole_Print(I2C_RINI_OBJ.ReadSignals())
         for Data in I2C_RINI_OBJ.ReadDataAfterCheck():
             TreeViewInsertValues(InputTreeViewControl=I2C_RegListBox,InputValues=Data)
             # GUIConsole_Print(Data)
    else:
         GUIConsole_Print('您没有选择任何文件')
def CreatePattern():
    GUIConsole_Print("你点击了CreatePattern")
# def
class GUIInfoGet:
    def __init__(self):
        print("Create GUIMessageGet Obj")
        pass
    # def Entry

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
I2C_Trans_SlaveID =  ttk.Label(master=I2C_RegMessage, text="")
I2C_Trans_SlaveID.grid(row=0, column=1,pady=6,padx=4)
ttk.Label(master=I2C_RegMessage, text="Trans_RegList").grid(row=1, column=0,pady=6,padx=4)

I2C_RegListBox = ttk.Treeview(I2C_RegMessage, columns="seq", show=HEADINGS)
I2C_RegListBox.heading(column="seq", text="指令",anchor='center',command=OnTreeViewHeaderPressed)
# defalut set for test now ,LIST has been deleted
# for row in LIST:
#     # I2C_RegListBox.insert('', END, values=row)
#     TreeViewInsertValues(InputTreeViewControl=I2C_RegListBox,InputValues=row)
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
# for line in LIST:
#         GUIConsole_Print(line)
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
GUIEdgeTopMenu_ThemeMemu = ttk.Menu(master=GUIEdgeTopMenu)
# for ThemeName in GUIThemes:#不知道为啥 不起作用
#     print(ThemeName)
#     GUIEdgeTopMenu_ThemeMemu.add_command(label=ThemeName,command=lambda :AppThemeSet(ThemeName))
#     GUIEdgeTopMenu_ThemeMemu.add_separator()
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[0],command=lambda :ttk.Style().theme_use(GUIThemes[0]))
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[1],command=lambda :ttk.Style().theme_use(GUIThemes[1]))
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[2],command=lambda :ttk.Style().theme_use(GUIThemes[2]))
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[3],command=lambda :ttk.Style().theme_use(GUIThemes[3]))
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[4],command=lambda :ttk.Style().theme_use(GUIThemes[4]))
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[5],command=lambda :ttk.Style().theme_use(GUIThemes[5]))
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[6],command=lambda :ttk.Style().theme_use(GUIThemes[6]))
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[7],command=lambda :ttk.Style().theme_use(GUIThemes[7]))
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[8],command=lambda :ttk.Style().theme_use(GUIThemes[8]))
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[9],command=lambda :ttk.Style().theme_use(GUIThemes[9]))
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[10],command=lambda :ttk.Style().theme_use(GUIThemes[10]))
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[11],command=lambda :ttk.Style().theme_use(GUIThemes[11]))
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[12],command=lambda :ttk.Style().theme_use(GUIThemes[12]))
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[13],command=lambda :ttk.Style().theme_use(GUIThemes[13]))
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[14],command=lambda :ttk.Style().theme_use(GUIThemes[14]))
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[15],command=lambda :ttk.Style().theme_use(GUIThemes[15]))
GUIEdgeTopMenu_ThemeMemu.add_command(label=GUIThemes[16],command=lambda :ttk.Style().theme_use(GUIThemes[16]))
GUIEdgeTopMenu.add_cascade (label="主题设置",menu=GUIEdgeTopMenu_ThemeMemu)
GUIEdgeTopMenu.add_command(label="Pattern模板",command=PatternTemplate)
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