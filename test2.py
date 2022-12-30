import  tkinter as tk
from PIL import Image,ImageTk


window = tk.Tk()
window.title('小工具合集')
window.minsize(400,300)
window.maxsize(1920,1080)
geo_size = '%dx%d+%d+%d'%(400,300,(window.winfo_screenwidth()-400)/2,(window.winfo_screenheight()-300)/2)
window.geometry(geo_size)#居中
# img = ImageTk.PhotoImage(Image.open(r'bg.jpg'))
# tk.Label(window, imag=img,
# state = 'disabled',
# compound = 'center'
#          ).pack()
tk.Label(window,bg="#7CCD7C"
                ).pack()

window.mainloop()