class Kino:
    def __init__(self,skatitajs,filma):
        self.skatitajs = skatitajs
        self.filma = filma
        self.summa = 0

    def maksa(self):
        self.summa += 5

    def izdruka(self):
        print(f"{self.skatitajs} maksā {self.summa} par filmu {self.filma}")

    
skatitajs_1 = Kino("Stepans", "Šreks")

skatitajs_2 = Kino("Leonids", "Madagaskars")


skatitajs_1.maksa()
skatitajs_2.maksa()


skatitajs_1.izdruka()
skatitajs_2.izdruka()