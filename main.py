from fastapi import FastAPI
import random, requests

app = FastAPI()

def get_champions():
    try:
        version = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()[0]
        data = requests.get(f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json").json()
        return list(data["data"].keys())
    except:
        return ["Ahri", "Yasuo", "Lux", "LeeSin", "Garen", "Teemo"]

champions = get_champions()

@app.get("/")
def root():
    return {"message": "Rancol API lista. Usa /rancol para un pick aleatorio."}

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
    # Solo devolver el texto como hacía chebacor
    return {"result": random.choice(frases)}
