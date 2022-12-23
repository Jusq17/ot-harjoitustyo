# Arkkitehtuurikuvaus

## Sovelluksen rakenne

Sovelluksessa on 4 pakkausta/kansiota, jotka hoitavat sovelluksen eri toiminnalisuuksia.
<br/>
_logic_ vastaa sovelluslogiikasta, _UI_ käyttöliittymästä, _game_ syötteistä ja pelin pyörittämisestä ja _file_management_ tiedostojen talletuksesta ja hallinnasta.

## Sovelluslogiikka

Sovelluslogiikasta vastaa pääasiassa gamelogic moduuli.

Tämä moduuli hoitaa pelimatriisiin liittyvän toiminnallisuuden. Koko 2048-peli perustuu tähän pelimatriisiin ja sen muokkaukseen.

## Käyttöliittymä

Käyttöliittymästä vastaa UI moduuli.

Tämä moduuli vastaa käyttöliittymän ja kaiken muun grafiikan piirtämisestä näytölle.

## Syötteet ja pelin pyöritys

Tämä moduuli hoitaa pygame-eventeistä ja mahdollistaa, että pelaaja voi oikeasti pelata peliä syötteiden avulla. Se myös yhdistää kaikki muut moduulit toimivaksi rakenteeksi. Sen run() funktiota kutsutaan, kun index.py käynnistetään.

## Tiedostojen hallinta

Tiedostojen hallinnasta vastaa file_manager moduuli.

Se on pieni moduuli, joka sisältää tiedostojen hallinta funktioita. Se tekee koodin lukemisesta muissa moduuleissa mielekkäämpää ja mahdollistaa parempaa jatkokehitystä.
<br/>
<br/>
Koska sovellus on vielä aika yksinkertainen, jokainen moduuli sisältää vain yhden luokan. Jatkokehityksessä voi olla hyödyllistä luoda lisää luokkia.

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
</br>
Ne piirretään näytölle UI-luokan draw_menu_UI() ja draw_main_UI() avulla.
UI-luokka vastaa siis kaikesta käyttöliittymään liittyvästä. Käyttöliittymä on eristetty sovelluslogiikasta kokonaan.
