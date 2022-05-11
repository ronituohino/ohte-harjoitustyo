class Form:
    """Lomake -luokka, joka ylläpitää syötekenttiä

    Attributes:
        textboxes: Syötekentät
        validation_func: Funktio, joka validoi syötekenttien syötteet
    """

    def __init__(self, validation_func):
        """Luokan konstruktori

        Args:
            validation_func: Funktio, joka validoi syötekenttien syötteet
        """

        self.textboxes = []
        self.validation_func = validation_func

    def attach_textbox(self, textbox):
        """Kiinnittää uuden syötekentän lomakkeeseen

        Args:
            textbox: Syötekenttä
        """

        self.textboxes.append(textbox)

    def validate(self):
        """Päivittää lomakkeen syötekenttien virheviestit validointifunktion avulla"""

        errors = self.validation_func()
        for textbox in self.textboxes:
            if textbox.name in errors:
                textbox.set_errors(errors[textbox.name])
            else:
                textbox.set_errors(None)
