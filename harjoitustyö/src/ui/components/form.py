class Form:
    def __init__(self, validation_func):
        self.textboxes = []
        self.validation_func = validation_func

    def attach_textbox(self, textbox):
        self.textboxes.append(textbox)

    def validate(self):
        errors = self.validation_func()
        for textbox in self.textboxes:
            if textbox.name in errors:
                textbox.set_errors(errors[textbox.name])
            else:
                textbox.set_errors(None)
