import logging
import requests
from fastapi import FastAPI, UploadFile, File

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/hello-world")
def hello_world():
    return "Hello from plantnet!"


@app.post("/identify")
async def identify_image(file: UploadFile = File(...)):
    bytes = await file.read()

    project = "k-brazil"
    api_key = "2b10p4QPtOtMthltVMaQPiwp"
    url = (
        f"https://my-api.plantnet.org/v2/identify/{project}"
        f"?include-related-images=true&no-reject=false&nb-results=5"
        f"&lang=pt&type=kt&detailed=false&api-key={api_key}"
    )

    try:
        logger.info(f"Enviando imagem '{file.filename}' para PlantNet ({url})")
        response = requests.post(
            url,
            headers={"accept": "application/json"},
            files=[("images", (file.filename, bytes, file.content_type))],
            data={"organs": "auto"},
        )
        logger.info(f"Resposta PlantNet: status={response.status_code}")
        if response.status_code == 200:
            dados = response.json()
            best_match = dados.get("bestMatch")
            logger.info(f"bestMatch: {best_match}")
            return {"bestMatch": best_match}
        else:
            logger.error(f"Erro PlantNet: [{response.status_code}] {response.text}")
            return {"erro": f"[{response.status_code}] {response.text}"}
    except Exception as e:
        logger.exception(f"Erro de comunicação: {e}")
        return {"erro": str(e)}
