from view import UserView
from controller import UserController
from model import UserModel
def main():
    uv = UserView()
    um = UserModel()
    uc = UserController(uv,um)
    uv.setController(uc)
    uv.run()

if __name__ == "__main__": main()