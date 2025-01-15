import tkinter as tk
from tkinter import *

class UserView:
    def __init__(self, master=None):
        self.m = tk.Tk()
        self.m.title("Rejseplanen")
        self.m.geometry("{0}x{1}+0+0".format(self.m.winfo_screenwidth(), self.m.winfo_screenheight()))
        
    def createscreen(self):
        departure = self.controller.getDeparture()
        Label(self.m, text="CPH Lufthavn - København",font='Helvetica 18 bold').grid(row=2, column=1, padx=5, pady=2)
        Label(self.m, text="Name", width=10,anchor="w",font='Helvetica 12 bold').grid(row=3, column=0, padx=5, pady=2)
        Label(self.m, text="Direction", width=20,anchor="w",font='Helvetica 12 bold').grid(row=3, column=1, padx=5, pady=2)
        Label(self.m, text="Scheduled", width=10,anchor="w",font='Helvetica 12 bold').grid(row=3, column=2, padx=5, pady=2)
        Label(self.m, text="Actual", width=10,anchor="w",font='Helvetica 12 bold').grid(row=3, column=3, padx=5, pady=2)
        Label(self.m, text="Within", width=10,anchor="w",font='Helvetica 12 bold').grid(row=3, column=4, padx=5, pady=2)
        j=4
        for i in departure:
            print(i.get("name"))
            Label(self.m, text=i.get("name"), width=10,anchor="w",font='Helvetica 12').grid(row=j, column=0, padx=5, pady=2)
            Label(self.m, text=i.get("direction"), width=20,anchor="w",font='Helvetica 12').grid(row=j, column=1, padx=5, pady=2)
            Label(self.m, text=i.get("time"), width=10,anchor="w",font='Helvetica 12').grid(row=j, column=2, padx=5, pady=2)
            Label(self.m, text=i.get("rtTime"), width=10,anchor="w",font='Helvetica 12').grid(row=j, column=3, padx=5, pady=2)
            Label(self.m, text=i.get("timeDelta"), width=10,anchor="w",font='Helvetica 12').grid(row=j, column=4, padx=5, pady=2)
            j+=1
            self.refresh_button = Button(self.m, text="Refresh", command=self.refresh).grid(row=4, column=10, padx=10, pady=15)          

    def refresh(self):
        self.run()
        

    def setController(self, controller):
        self.controller = controller
        
    
    def run(self):
        self.createscreen()
        self.m.mainloop()
