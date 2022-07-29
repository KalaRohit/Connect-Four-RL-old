from tkinter import *



class ConnectFourMenu(Menu):
    def __init__(self, master=None):
        super().__init__(master)
        master.config(menu=self)
        self.fileMenu = Menu(self)
        self.canvasOptionsAdded = False
        self.canvasOptionsDisabled = True
        self.showMenuOptions()
        self.canvasOptions = []
        

        
        
    
    def showMenuOptions(self):
        if self.canvasOptionsAdded == False:

            self.fileMenu.add_command(label='Save Board', command = self.master.saveCurrentBoard)
            self.fileMenu.add_command(label='Load Board', command= self.master.loadBoard)
            self.fileMenu.add_command(label='Return to Main Menu', command=self.master.createMainMenu)
            
            self.fileMenu.add_command(label='Exit', command=self.master.destroy)
            self.add_cascade(label="ConnectFour",menu=self.fileMenu,underline=0)
            self.canvasOptionsAdded = True
        
            
    
    def enableMenuOptions(self):
        if self.canvasOptionsDisabled == True:
            self.fileMenu.entryconfigure('Save Board', state=NORMAL)
            self.canvasOptionsDisabled = True
        
    def disableMenuOptions(self):
        try:
            self.fileMenu.entryconfigure('Save Board', state=DISABLED)
            self.canvasOptionsDisabled = True
        except:
            pass
