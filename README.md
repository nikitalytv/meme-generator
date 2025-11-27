<img src="static/logo.png" width="50">

# Meme Generator

To je spletna aplikacija za ustvarjanje memov, narejena v Pythonu s pomočjo ogrodja Flask in knjižnice Pillow. Uporabnik lahko naloži sliko, doda zgornje in spodnje besedilo ter ustvari končno sliko.

## ✨ Funkcionalnosti
- nalaganje slike preko obrazca
- vnos zgornjega in spodnjega teksta
- dinamična sprememba velikosti pisave
- generiranje končnega mema
- prikaz rezultata v brskalniku

---

## 🐳 Zagon preko Dockerja

Najprej zgradimo sliko:

```bash
docker build -t meme-generator .
```

Nato zaženemo vsebnik:
```bash
docker run -p 8080:5000 meme-generator
```

Aplikacija bo dostopna na naslovu:
http://localhost:8080

## 📁 Struktura projekta
.
├── app.py
├── Dockerfile
├── static/
│   ├── style.css
│   ├── main.js
│   └── logo.png
└── templates/
    └── index.html

## 📦 Uporabljene tehnologije
Python 3.12
Flask
Pillow
Docker
