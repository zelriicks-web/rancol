from fastapi import FastAPI
import random, requests

app = FastAPI()

# Obtener todos los campeones de LoL desde la API oficial de Riot
def get_champions():
    try:
        version = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()[0]
        data = requests.get(f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json").json()
        return list(data["data"].keys())
    except:
        # En caso de error, usar algunos por defecto
        return ["Ahri", "Yasuo", "Lux", "LeeSin", "Garen", "Teemo"]

champions = get_champions()

@app.get("/")
def home():
    return {"status": "Rancol API activa"}

@app.get("/rancol")
def rancol(user: str = "Maycol"):
    champ = random.choice(champions)
    frases = [
        f"{user} pickea {champ}, ahora sí que saldrán cosas coreanas 🇰🇷",
        f"{user} eligió {champ}, el draft se fue a la B 😭",
        f"{champ} fue pickeado por {user}, ya huele a pentakill 😎",
        f"{user} saca {champ}, GG EZ 🔥",
        f"{champ} es el elegido por {user}… o la víctima 😏",
    ]
    return {
        "result": random.choice(frases),
        "champion": champ
    }
