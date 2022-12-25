### Ohjelmistotekniikka 2022 projekti
# 2048 Python peli

Tämä sovellus on siis työpyötä versio tutusta 2048 pelistä. Se on toteutettu käyttäen Python3 ohjelmointikieltä ja vaatii vähintään version 3.8, jotta sen voi suorittaa. Se käyttää myös pygame ja numpy kirjastoja.

## Dokumentaatio

[Käyttöohje](https://github.com/Jusq17/ot-harjoitustyo/blob/master/Dokumentaatio/Kayttoohje.md)
<br/>
[Vaatimusmäärittely](https://github.com/Jusq17/ot-harjoitustyo/blob/master/Dokumentaatio/vaatimusmaarittely.md)
<br/>
[Arkkitehtuuri](https://github.com/Jusq17/ot-harjoitustyo/blob/master/Dokumentaatio/arkkitehtuuri.md)
<br/>
[Testausdokumentti](https://github.com/Jusq17/ot-harjoitustyo/blob/master/Dokumentaatio/testausdokumentti.md)
<br/>
[Tuntikirjanpito](https://github.com/Jusq17/ot-harjoitustyo/blob/master/Dokumentaatio/tuntikirjanpito.md)
<br/>
[changelog](https://github.com/Jusq17/ot-harjoitustyo/blob/master/Dokumentaatio/changelog.md)

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
poetry run invoke coverage-report
```

Pylint tarkastuksien suorittaminen:

```bash
poetry run invoke lint
```
