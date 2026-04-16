import logging
import requests
from fastapi import FastAPI, UploadFile, File

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

async def callPlantNet(file):
    try:
        contents = await file.read()
        response = requests.post(
            "http://plantnet-api:8081/identify",
            files={"file": (file.filename, contents, file.content_type)},
        )
        if response.status_code == 200:
            dados = response.json()
            best_match = dados.get("bestMatch")
            logger.info(f"bestMatch: {best_match}")
            return best_match
        else:
            logger.error(f"Erro ao chamar PlantNet: [{response.status_code}] {response.text}")
            raise Exception(f"Erro [{response.status_code}] {response.text}")
    except Exception as e:
        logger.exception(f"Erro de comunicação: {e}")
        raise e

async def callDB(scientific_name):
    try:
        scientific_name = scientific_name.split()[0]
        response = requests.get(f"http://db-api:8083/flowers/{scientific_name}")
        if response.status_code == 200:
            dados = response.json()
            name = dados.get("name")
            logger.info(f"name: {name}")
            return {"name": name, "poisonToCats": dados.get("poison_to_cats"), "poisonToDogs": dados.get("poison_to_dogs")}
        else:
            logger.error(f"Erro ao chamar o banco de dados: [{response.status_code}] {response.text}")
            raise Exception(f"Erro [{response.status_code}] {response.text}")
    except Exception as e:
        logger.exception(f"Erro de comunicação: {e}")
        raise e

@app.get("/hello-world")
def hello_world():
    return "Hello from BFF!"


@app.post("/identify")
async def identify_image(file: UploadFile = File(...)):
    scientific_name = ""
    try:
        scientific_name = await callPlantNet(file)
    except Exception as e:
        return {"erro": str(e)}
    try:
        return await callDB(scientific_name)
    except Exception as e:
        return {"erro": str(e)}
