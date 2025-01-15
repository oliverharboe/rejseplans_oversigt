class UserController:
    def __init__(self,view,model):
        self.view = view
        self.model = model
    def getDeparture(self):
        return self.model.get_data()
    
