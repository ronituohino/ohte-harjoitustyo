class Form:
    def __init__(self):
        self.elements = []

    def attach_element(self, name, element: "Element", validation_func):
        self.elements.append((name, element, validation_func))

    def valid(self):
        for e in self.elements:
            name, element, validation_func = e
            if not validation_func(element.value):
                return False
        return True

    def get_values(self):
        values = {}
        for e in self.elements:
            name, element, validation_func = e
            values[name] = element.value
        return values
