class ControlerActions:
    def sauter(self):
        pass

    def attaquer(self):
        pass

    def interagir(self):
        pass

# On partira du principe qu'on a la librairie pour utiliser une manette Xbox/PS5/etc.

class ManetteXbox:
    def button_a(self):
        pass

    def button_b(self):
        pass

    def button_x(self):
        pass

class XboxControlerActionsAdapter (ControlerActions):
    def __init__(self, manette: ManetteXbox):
        self.manette = manette

    def sauter(self):
        print("Bouton A")

    def attaquer(self):
        print("Bouton B")

    def interagir(self):
        print("Bouton X")


class ManettePS5:
    def button_x(self):
        print("Bouton X")

    def button_o(self):
        print("Bouton O")

    def button_tri(self):
        print("Bouton Triangle")

class PS5ControlerActionsAdapter (ControlerActions):
    def __init__(self, manette: ManettePS5):
        self.manette = manette

    def sauter(self):
        self.manette.button_x()

    def attaquer(self):
        self.manette.button_o()

    def interagir(self):
        self.manette.button_tri()

# PROGRAMME PRINCIPAL
if __name__ == "__main__":
    xbox = ManetteXbox()
    play = ManettePS5()

    xbox_action = XboxControlerActionsAdapter(xbox)
    play_action = PS5ControlerActionsAdapter(play)

    xbox_action.sauter()
    xbox_action.attaquer()
    xbox_action.interagir()

    play_action.sauter()
    play_action.attaquer()
    play_action.interagir()
