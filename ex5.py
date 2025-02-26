class Personnage:
    def attaquer(self):
        print("Le personnage attaque")

class Guerrier:
    def attaquer(self):
        print("Le guerrier attaque avec sa grande hache")

class Magicien:
    def attaquer(self):
        print("Le magicien lance un sort afaiblissant")

class Archer:
    def attaquer(self):
        print("L'archer tire une fleche")


class CreationPersonnage:
    def creer_guerrier():
        return Guerrier()

    def creer_magicien():
        return Magicien()

    def creer_archer():
        return Archer()

if __name__ == "__main__":
    perso = CreationPersonnage.creer_guerrier()
    perso.attaquer()

    perso = CreationPersonnage.creer_magicien()
    perso.attaquer()

    perso = CreationPersonnage.creer_archer()
    perso.attaquer()
