class Movies_List:
    def __init__(self,title,director,release,genre):
        self.title=title
        self.director=director
        self.release=release
        self.genre=genre
    def teee(self):
        print(f"Title:{self.title}")
        print(f"Director:{self.director}")
        print(f"Release{self.release}")
        print(f"Genre:{self.genre}\n\n")
    def teee2(self,title,director,release,genre):
        self.title=title
        self.director=director
        self.release=release
        self.genre=genre
print("*****************\nWelcome to the movie program\n*****************")
def asks():
    inp_tit=input("Enter the name of the movie:")
    inp_dir=input("Enter the name of film's author:")
    inp_rel=int(input("Enter the film's release:"))
    inp_genre=input("Enter the type of film:")
    return inp_tit,inp_dir,inp_rel,inp_genre

asks()

