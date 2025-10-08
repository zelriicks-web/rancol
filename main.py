import random
import requests
from flask import Flask, request

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
def random_pick():
    user = request.args.get("user", "Maycol")
    champ = random.choice(champions)
    frases = [
        f"{user} pickea {champ}, ahora sí que saldrán cosas coreanas 🇰🇷",
        f"{champ} fue elegido por {user}... GG o troleo, tú decides 😏",
        f"{user} con {champ}, prepárense para la pentakill 😎",
        f"{champ} pickeado por {user}, ¡que empiece el show!",
        f"{champ} es la elección de {user}, meta asegurada 🔥"
    ]
    return random.choice(frases)

@app.route("/")
def home():
    return "API Rancol Activa!"

# Ejecutar Flask localmente si se usa python main.py
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
