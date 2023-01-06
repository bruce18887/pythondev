import ttkbootstrap as ttk
from ttkbootstrap import utility
from ttkbootstrap.constants import *
import re
########################
_softwareversion = 'V1.1'
########################
class PatternCreateTool(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        # form variables
        self.I2C_strWFT = ttk.StringVar(value="TS1")
        self.I2C_strSignal = ttk.StringVar(value="SCL,SDA")
        self.I2C_strFileName = ttk.StringVar(value="*.csv")
        self.I2C_ModeSelect = ttk.IntVar(value=0)
        NoteBookPage = ttk.Notebook(
            master=master
        )
        NoteBookPage.pack(fill=X)
        NoteBookPage.add(child=self.I2C_GUI_Create(NoteBookPage), text="I2C")
        NoteBookPage.add(child=self.SPI_GUI_Create(NoteBookPage), text="SPI")
        NoteBookPage.add(child=self.UART_GUI_Create(NoteBookPage), text="UART")

    def OnTreeViewSelect(self,A):
        print("Begin")
        for var in self.I2C_RegListBox.selection():
            print(self.I2C_RegListBox.set(var))
        print("End")
    def I2C_GUI_Create(self,NotebookMaster):
        I2C_GUI_Frame = ttk.Frame(master=NotebookMaster)
        I2C_GUI_Frame.pack()
        ########################################
        I2C_Setting = ttk.Labelframe(master=I2C_GUI_Frame, text="I2C_Setting")
        I2C_Setting.pack(fill=X,expand=True)
        ttk.Label(master=I2C_Setting, text="SlaveID").grid(row=0, column=0)
        ttk.Label(master=I2C_Setting, text="Address").grid(row=1, column=0)
        ttk.Label(master=I2C_Setting, text="Data").grid(row=2, column=0)
        ttk.Label(master=I2C_Setting, text="WFT").grid(row=0, column=2)
        ttk.Label(master=I2C_Setting, text="Signal").grid(row=1, column=2)
        ttk.Label(master=I2C_Setting, text="FileName").grid(row=2, column=2)
        ttk.Label(master=I2C_Setting, text="CreateMode").grid(row=3, column=0)
        I2C_SlaveID = ttk.Entry(master=I2C_Setting)
        I2C_Address = ttk.Entry(master=I2C_Setting)
        I2C_Data = ttk.Entry(master=I2C_Setting)
        I2C_WFT = ttk.Entry(master=I2C_Setting, textvariable=self.I2C_strWFT)
        I2C_Signal = ttk.Entry(master=I2C_Setting, textvariable=self.I2C_strSignal)
        I2C_FileName = ttk.Entry(master=I2C_Setting, textvariable=self.I2C_strFileName)
        I2C_SlaveID.grid(row=0, column=1)
        I2C_Address.grid(row=1, column=1)
        I2C_Data.grid(row=2, column=1)
        I2C_WFT.grid(row=0, column=3)
        I2C_Signal.grid(row=1, column=3)
        I2C_FileName.grid(row=2, column=3)
        #for PatternCreateMode
        ttk.Radiobutton(I2C_Setting,text="Driver",variable=self.I2C_ModeSelect,value=0).grid(row=3,column=1)
        ttk.Radiobutton(I2C_Setting,text="Compare",variable=self.I2C_ModeSelect,value=1).grid(row=3,column=2)
        ########################################
        I2C_RegMessage = ttk.Labelframe(master=I2C_GUI_Frame,text="I2C_RegMessage")
        I2C_RegMessage.pack(fill=X, expand=True)
        ttk.Label(master=I2C_RegMessage, text="Trans_SlaveID").grid(row=0, column=0)
        ttk.Label(master=I2C_RegMessage, text="Trans_RegList").grid(row=1, column=0)
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
        # I2C_RegListBox.heading(0,text="序号")
        I2C_RegListBox.heading(column="seq", text="指令",anchor=W)
        I2C_RegListBox.column(0,width=200)
        I2C_RegListBox.grid(row=0,column=1)
        # I2C_RegListBox.column(0, anchor=W,width=utility.scale_size(I2C_RegMessage, 125),stretch=False)
        # I2C_RegListBox.column(1, anchor=W, width=utility.scale_size(I2C_RegMessage, 125), stretch=False)
        # for var in range(0,len(LIST)):
        #     I2C_RegListBox.insert(parent='',index=var, values=(var,LIST[var]))

        I2C_RegListBox.bind("<<TreeviewSelect>>",self.OnTreeViewSelect)


        return I2C_GUI_Frame

    def SPI_GUI_Create(self, NotebookMaster):
        ########################################
        SPI_Setting = ttk.Labelframe(master=NotebookMaster, text="SPI_Setting")
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
        return SPI_Setting
    def UART_GUI_Create(self, NotebookMaster):
        ########################################
        UART_Setting = ttk.Labelframe(master=NotebookMaster, text="I2C_Setting")
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
        return UART_Setting

    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)
if __name__ == "__main__":

    app = ttk.Window(
        title="PatternCreateTool " + _softwareversion,
        size=(800,600),
        themename="solar",
        # All suport theme
        # flatly  litera  minty  lumen sandstone yeti pulse
        # united morph journal darkly superhero solar  cyborg vapor simplex  cerculean
        resizable=(False, False)
    )

    # for var in ttk.Style().theme_names():
    #     print(var)
    PatternCreateTool(app)
    app.mainloop()