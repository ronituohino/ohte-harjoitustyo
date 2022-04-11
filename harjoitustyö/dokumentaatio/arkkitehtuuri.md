Sudoku -sovelluksen luokkakaavio

```mermaid
classDiagram
index "1" -- "1" Game
Game "1" -- "1" Sudoku
Game "1" -- "1" Menu
Game "1" -- "1" Canvas
Canvas "1" -- "*" View
View "1" -- "*" Button
View <|-- SudokuView
SudokuView "1" -- "1" Sudoku
MenuView "1" -- "1" Menu
View <|-- MenuView

class index { }
class Game { }
class Canvas { }
class Button { }
class View { }

class SudokuView { }
class MenuView { }
class Sudoku { }
class Menu { }
```

> Written with [StackEdit](https://stackedit.io/).
