# Käyttöohje

Lataa viimeisimmän releasen lähdekoodi assests-osiosta.

## Asennus ja ohjelman käynnistys

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Muuta ei tarvitse tehdä. Ohjelman voi käynnistää komennolla:

```bash
poetry run invoke start
```

## Ohjelman käyttö

Käynnistyksen jälkeen avautuu start-menu näkymä joka näyttää seuraavalta:
<br/>
<br/>
![](./kuvat/kayttoohje-startmenu.JPG)

Paina Enter-näppäintä siirtyäksesi pelinäkymään.
<br/>
Pelinäkymä:
<br/>
<br/>
![](./kuvat/kayttoohje-game.JPG)

Käytä nuolinäppäimiä pelataksesi peliä. Kun saavut tilanteeseen, jossa et voi enää siirtää numeroita, voit painaa "r"-näppäintä aloittaaksesi uudelleen. Highscoresi tallennetaan aina, kun saat suuremman scoren kuin edellinen parhaasi. Voit siis sulkea sovelluksen yläkulmasta ja highscoresi on tallessa.

## Konfiguraatio

Pelilaudan laatikoiden värit muuttuvat niiden numeroiden perusteella. Näiden laatikkojen värejä voi muokata data kansioissa olevan colors.ini tiedoston kautta. Voidaan esimerkiksi vaihtaa numeroa 32 vastaavan laatikon väriä muokkaamalla kohtaa color_32 arvoa.

