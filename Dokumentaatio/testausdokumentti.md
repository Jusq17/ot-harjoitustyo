# Testausdokumentti

Testeissä testataan sovelluslogiikkaa ja pygame-eventtien toimintaa. Testataan siis luokkien Logic ja Game toimintaa.

## Luokka Logic

Logic-luokka vastaa pelimatriisin muokkaamisesta. Testeissä testataan, että luokan metodit toimivat oikein.
<br/>
Käydään siis läpi, että kaikki matriisin siirto metodit (esim. move_left()) toimivat oikein.
<br/>
Testataan myös, että create_start_pos() metodi tekee matriisin alustuksen oikein.

## Luokka Game

Testaamme, että Game-luokan pygame-eventeistä tapahtuu odotettu tilanne. Luokkia Game ja Logic testataan yhdessä näissä testeissä.
<br/>
Testataan, että kun kutsutaan Game-luokan game_handler(event) metodia tietynlaisella pygame-eventillä, niin saadaan haluttu muutos matriisissa.
<br/>
Näin voidaan olla varmoja, että molempien luokkien toiminta onnistuu silloinkin, kun ne tekevät yhteistyötä.
