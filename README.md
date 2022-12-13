# Ohjelmistotekniikka 2022 projekti
## 2048 Python peli

Tämä sovellus on siis työpyötä versio tutusta 2048 pelistä. Se on toteutettu käyttäen Python3 ohjelmointikieltä ja vaatii vähintään version 3.8, jotta sen voi suorittaa. Se käyttää myös pygame ja numpy kirjastoja.

## Dokumentaatio

[Arkkitehtuuri](https://github.com/Jusq17/ot-harjoitustyo/blob/master/Dokumentaatio/arkkitehtuuri.md)
<br/>
[Vaatimusmäärittely](https://github.com/Jusq17/ot-harjoitustyo/blob/master/Dokumentaatio/vaatimusmaarittely.md)
[Tuntikirjanpito](https://github.com/Jusq17/ot-harjoitustyo/blob/master/Dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Muuta ei tarvitse tehdä. Ohjelman voi käynnistää komennolla:

```bash
poetry run invoke start
```

## Kaikki komentoriviltä suoritettavat komennot

Ohjelman käynnistys:

```bash
poetry run invoke start
```
Testien suorittaminen:

```bash
poetry run invoke test
```
Testi coverage reportin luominen:

```bash
poetry run invoke coverage
```


