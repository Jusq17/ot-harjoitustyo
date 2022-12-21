
## Luokkakaavio

```mermaid

  classDiagram
  
  Game --> Logic
  Game --> UI
  
  class Game{
     run()
  }
  
  class Logic{
    game_matrix: matrix1
    
    create_start_pos()
    move_left()
    move_right()
    move_down()
    move_up()
  }
  
  class UI{
    block_size
    draw_matrix()
    draw_main_UI()
    draw_menu_UI()
  }

```

## Käyttöliittymä

Pelissä on vain kaksi eri näkymää: start-menu ja varsinainen pelinäkymä. Koska näkymiä on niin vähän ja start-menu on todella yksinkertainen, molemmat näkymät ovat samassa luokassa.
</br>
Ne piirretään näytölle UI-luokan draw_menu_UI() ja draw_main_UI() avulla.
UI-luokka vastaa siis kaikesta käyttöliittymään liittyvästä. Käyttöliittymä on eristetty sovelluslogiikasta kokonaan.
