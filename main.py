from kivy.app import App

class RechnerApp(App):
    pass

    def berechne(self,button, gui, app):
        print("berechne wird ausgeführt")
        for x in [self, button, gui, app]:
            print(x)
        button.text = "fertig berechnet!"
        print("fertig")

    def button_pressed(self, button):
        print(button.text)
        if self.root.ids.Feld.text == "Hallo":
            self.root.ids.Feld.text = button.text
        else:
            self.root.ids.Feld.text += button.text
        print(self.root.ids)

meineAnwendung = RechnerApp()
print(meineAnwendung)
meineAnwendung.run()
