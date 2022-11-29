
## Luokkakaavio

```mermaid

  classDiagram
  
  Game --> Logic
  Game --> UI
  
  class Game{
  
  }
  
  class Logic{
    game matrix
    move_left()
    move_right()
    move_down()
    move_up()
  }
  
  class UI{
    block_size
    draw_matrix()
    draw_UI()
  }

```
