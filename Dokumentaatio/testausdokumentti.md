# Testausdokumentti

Sovelluksen sovelluslogiikkaa ja pygame-eventtien toimintaa testataan automatisoitujen yksikkötestien avulla. Testataan siis luokkien _Logic_ ja _Game_ toimintaa.

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
<br/>
Näin voidaan olla varmoja, että molempien luokkien toiminta onnistuu silloinkin, kun ne tekevät yhteistyötä.

## Haarautumakattavuus ja coverage-report

![](https://github.com/Jusq17/ot-harjoitustyo/blob/master/Dokumentaatio/kuvat/coverage.JPG)

## Järjestelmätestaus manuaalisesti

Pelaaja ei voi saada virhetilannetta aikaan peliä pelatessa. Ainoat syötteet, jotka pelaaja voi pelissä tehdä ovat: näppäimistön nuolinäppäimet, ENTER-näppäin ja R-näppäin. Peliä on testattu manuaalisesti antamalla erilaisia syötteitä start-menu näkymässä ja peli-näkymässä.
<br/>
<br/>
Testien avulla voidaan olla myös varma, että syötteet tekevät, mitä niiden pitäisi.
<br/>
<br/>

## Sovelluksen laatuongelmat

Jos colors.ini tiedostoa muunnetaan väärästi ja sinne laitetaan esim. kirjaimia numeroiden sijaan, ohjelma ei osaa ratkaista ongelmaa itse.
Jostain syystä pelin startmenu-näkymässä ENTER-näppäintä pitää painaa kaksi kertaa.
