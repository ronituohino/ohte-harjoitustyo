Sudoku -sovelluksen luokkakaavio

```mermaid
classDiagram
index "1" -- "1" Canvas
Canvas "1" -- "*" View
View "1" -- "*" Form
Form "1" -- "*" TextBox
Form "1" -- "*" Button
View <|-- SudokuView
View <|-- MenuView
View <|-- LoginView
View <|-- RegisterView
SudokuView "1" -- "1" Sudoku
MenuView "1" -- "1" Menu
LoginView "1" -- "1" Login
RegisterView "1" -- "1" Register

class index { }
class Canvas { }
class Button { }
class TextBox { }
class Form { }
class View { }

class SudokuView { }
class MenuView { }
class LoginView { }
class RegisterView { }

class Sudoku { }
class Menu { }
class Login { }
class Register { }
```

> Written with [StackEdit](https://stackedit.io/).
