import tkinter as tk
from tkinter import *
from Model import UserModel

class UserView:
    def __init__(self, master=None):
        self.m = tk.Tk()
        self.m.title("Rejseplanen")
        self.m.geometry("{0}x{1}+0+0".format(self.m.winfo_screenwidth(), self.m.winfo_screenheight()))
        tk.Label(self.m, text="CPH Lufthavn - København",font='Helvetica 18 bold').grid(row=2, column=1, padx=5, pady=2)
        Label(self.m, text="Name", width=10,anchor="w",font='Helvetica 12 bold').grid(row=3, column=0, padx=5, pady=2)
        Label(self.m, text="Direction", width=20,anchor="w",font='Helvetica 12 bold').grid(row=3, column=1, padx=5, pady=2)
        Label(self.m, text="Scheduled", width=10,anchor="w",font='Helvetica 12 bold').grid(row=3, column=2, padx=5, pady=2)
        Label(self.m, text="Actual", width=10,anchor="w",font='Helvetica 12 bold').grid(row=3, column=3, padx=5, pady=2)
        Label(self.m, text="Within", width=10,anchor="w",font='Helvetica 12 bold').grid(row=3, column=4, padx=5, pady=2)
        j=4
        departure =  [{
                    "name": "5C",
                    "direction" : "Husum Torv",
                    "scheduled": "10:17",
                    "actual" : "10:26",
                    "within" : "3 min"
                    },
                    {
                    "name": "250S",
                    "direction" : "Gladsaxe",
                    "scheduled": "10:17",
                    "actual" : "10:26",
                    "within" : "5 min"
                    }]
        for i in departure:
            print(i.get("name"))
            Label(self.m, text=i.get("name"), width=10,anchor="w",font='Helvetica 12').grid(row=j, column=0, padx=5, pady=2)
            Label(self.m, text=i.get("direction"), width=20,anchor="w",font='Helvetica 12').grid(row=j, column=1, padx=5, pady=2)
            Label(self.m, text=i.get("scheduled"), width=10,anchor="w",font='Helvetica 12').grid(row=j, column=2, padx=5, pady=2)
            Label(self.m, text=i.get("actual"), width=10,anchor="w",font='Helvetica 12').grid(row=j, column=3, padx=5, pady=2)
            Label(self.m, text=i.get("within"), width=10,anchor="w",font='Helvetica 12').grid(row=j, column=4, padx=5, pady=2)
            j+=1
            self.refresh_button = Button(self.m, text="Refresh", command=self.refresh).grid(row=4, column=10, padx=10, pady=15)
            self.controller = master

    def refresh(self):
        self.m.destroy()
        self.__init__()
        

    def setController(self, controller):
        self.controller = controller
        departure = self.controller.getDeparture()  
        

    
    def run(self):
        self.m.mainloop()

p1 = UserView()
p1.run()