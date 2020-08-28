import npyscreen

class MainForm(npyscreen.ActionForm):
    def create(self):
        self.fname = self.add(
            npyscreen.TitleText,
            name= 'First Name: '
        )
    
    def afterEditing(self):
        self.parentApp.setNextForm(None)

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm(
            'MAIN',
            MainForm,
            name='NPS App !'
        )

if __name__ == "__main__":
    app = App().run()