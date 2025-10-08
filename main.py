import random
import requests
from flask import Flask

app = Flask(__name__)

# Descargar lista de campeones desde Riot
versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()
latest_version = versions[0]

champions_data = requests.get(
    f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/en_US/champion.json"
).json()

champions = list(champions_data["data"].keys())

# Asegurar que Yunara esté incluida
if "Yunara" not in champions:
    champions.append("Yunara")

@app.route("/rancol")
def random_champ():
    champ = random.choice(champions)
    frases = [
        f"Maycol pickea {champ}, ahora sí que saldrán cosas coreanas 🇰🇷",
        f"{champ} fue elegido por Maycol... GG o troleo, tú decides 😏",
        f"Maycol con {champ}, prepárense para la pentakill 😎",
        f"{champ} pickeado por Maycol, ¡que empiece el show!",
        f"{champ} es la elección de Maycol, meta asegurada 🔥"
    ]
    return random.choice(frases)

@app.route("/")
def home():
    return "API Rancol Activa!"
