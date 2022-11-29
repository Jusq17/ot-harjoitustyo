
```mermaid

  classDiagram
  
  2048 Game --> Logic
  2048 Game --> UI
  
  class 2048 Game{
  
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
