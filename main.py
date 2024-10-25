from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# Defina o JSON com os dados dos carros
carros = [
    {"id": 1, "marca": "Chrysler", "modelo": "Visionary", "ano": 2024, "tipoDeCombustivel": "Diesel", "consumoKmL": "8.63", "potenciaCv": 679, "zeroACemKmH": 8.62, "classificacaoDeSeguranca": "4 estrelas", "preco": 245331.14},
    {"id": 2, "marca": "Dodge", "modelo": "Falcon GT", "ano": 2024, "tipoDeCombustivel": "Diesel", "consumoKmL": None, "potenciaCv": 473, "zeroACemKmH": 9.87, "classificacaoDeSeguranca": "5 estrelas", "preco": 163832.92},
    {"id": 3, "marca": "Jeep", "modelo": "Explorer Trailhawk", "ano": 2024, "tipoDeCombustivel": "Híbrido", "consumoKmL": "5.76", "potenciaCv": 653, "zeroACemKmH": 7.29, "classificacaoDeSeguranca": "4 estrelas", "preco": 246336.85},
    {"id": 4, "marca": "RAM", "modelo": "3500 HD", "ano": 2024, "tipoDeCombustivel": "Híbrido", "consumoKmL": "10.35", "potenciaCv": 173, "zeroACemKmH": 8.06, "classificacaoDeSeguranca": "3 estrelas", "preco": 235831.5},
    {"id": 5, "marca": "Chrysler", "modelo": "Concorde LXI", "ano": 2024, "tipoDeCombustivel": "Diesel", "consumoKmL": "6.16", "potenciaCv": 685, "zeroACemKmH": 9.21, "classificacaoDeSeguranca": "4 estrelas", "preco": 136026.79},
    {"id": 6, "marca": "Dodge", "modelo": "Viper Dreamcatcher", "ano": 2024, "tipoDeCombustivel": "Elétrico", "consumoKmL": "-", "potenciaCv": 556, "zeroACemKmH": 12, "classificacaoDeSeguranca": "5 estrelas", "preco": 102163.59},
    {"id": 7, "marca": "Jeep", "modelo": "Compass Pioneer", "ano": 2024, "tipoDeCombustivel": "Gasolina", "consumoKmL": "11.13", "potenciaCv": 585, "zeroACemKmH": 6.04, "classificacaoDeSeguranca": "5 estrelas", "preco": 327965.66},
    {"id": 8, "marca": "RAM", "modelo": "Rebel TRX", "ano": 2024, "tipoDeCombustivel": "Diesel", "consumoKmL": "5.55", "potenciaCv": 163, "zeroACemKmH": 8.17, "classificacaoDeSeguranca": "4 estrelas", "preco": 214627.33},
    {"id": 9, "marca": "Chrysler", "modelo": "Aspen Eco", "ano": 2024, "tipoDeCombustivel": "Elétrico", "consumoKmL": "-", "potenciaCv": 653, "zeroACemKmH": 11.64, "classificacaoDeSeguranca": "4 estrelas", "preco": 247273.64},
    {"id": 10, "marca": "Dodge", "modelo": "Dart Phoenix", "ano": 2024, "tipoDeCombustivel": "Elétrico", "consumoKmL": "-", "potenciaCv": 252, "zeroACemKmH": 11.32, "classificacaoDeSeguranca": "5 estrelas", "preco": 161152.99},
    {"id": 11, "marca": "Jeep", "modelo": "Renegade Dust", "ano": 2024, "tipoDeCombustivel": "Diesel", "consumoKmL": "8.45", "potenciaCv": 320, "zeroACemKmH": 5.99, "classificacaoDeSeguranca": "3 estrelas", "preco": 162237.88},
    {"id": 12, "marca": "RAM", "modelo": "Dakota SRT", "ano": 2024, "tipoDeCombustivel": "Híbrido", "consumoKmL": "13.91", "potenciaCv": 194, "zeroACemKmH": 5.12, "classificacaoDeSeguranca": "5 estrelas", "preco": 125601.99},
    {"id": 13, "marca": "Chrysler", "modelo": "Imperial Crown", "ano": 2024, "tipoDeCombustivel": "Híbrido", "consumoKmL": "5.71", "potenciaCv": 504, "zeroACemKmH": 8.63, "classificacaoDeSeguranca": "3 estrelas", "preco": 225366.65},
    {"id": 14, "marca": "Dodge", "modelo": "Journey SRT", "ano": 2024, "tipoDeCombustivel": "Gasolina", "consumoKmL": None, "potenciaCv": 327, "zeroACemKmH": 8.04, "classificacaoDeSeguranca": "3 estrelas", "preco": 151066.22},
    {"id": 15, "marca": "Jeep", "modelo": "Gladiator Overland", "ano": 2024, "tipoDeCombustivel": "Diesel", "consumoKmL": "11.44", "potenciaCv": 159, "zeroACemKmH": 5.11, "classificacaoDeSeguranca": "3 estrelas", "preco": 150083.28},
    {"id": 16, "marca": "RAM", "modelo": "Bighorn", "ano": 2024, "tipoDeCombustivel": "Gasolina", "consumoKmL": "7.92", "potenciaCv": 554, "zeroACemKmH": 11.47, "classificacaoDeSeguranca": "3 estrelas", "preco": 219262.39},
    {"id": 17, "marca": "Chrysler", "modelo": "Pacifica Hybrid", "ano": 2024, "tipoDeCombustivel": "Híbrido", "consumoKmL": "9.87", "potenciaCv": 474, "zeroACemKmH": 3.92, "classificacaoDeSeguranca": "4 estrelas", "preco": 133540.92},
    {"id": 18, "marca": "Dodge", "modelo": "Neon SXT", "ano": 2024, "tipoDeCombustivel": "Diesel", "consumoKmL": "11.75", "potenciaCv": 466, "zeroACemKmH": 8.36, "classificacaoDeSeguranca": "3 estrelas", "preco": 332923.34},
    {"id": 19, "marca": "Jeep", "modelo": "Liberty Freedom", "ano": 2024, "tipoDeCombustivel": "Gasolina", "consumoKmL": "14.07", "potenciaCv": 508, "zeroACemKmH": 11.04, "classificacaoDeSeguranca": "3 estrelas", "preco": 267990.08},
    {"id": 20, "marca": "RAM", "modelo": "Express Quad", "ano": 2024, "tipoDeCombustivel": "Híbrido", "consumoKmL": "5.44", "potenciaCv": 362, "zeroACemKmH": 11.56, "classificacaoDeSeguranca": "3 estrelas", "preco": 198683.27},
    {"id": 21, "marca": "Chrysler", "modelo": "300C Luxury", "ano": 2024, "tipoDeCombustivel": "Híbrido", "consumoKmL": "12.83", "potenciaCv": 615, "zeroACemKmH": 9.29, "classificacaoDeSeguranca": "5 estrelas", "preco": 301631.51},
    {"id": 22, "marca": "Dodge", "modelo": "Challenger Fury", "ano": 2024, "tipoDeCombustivel": "Gasolina", "consumoKmL": "9.1", "potenciaCv": 395, "zeroACemKmH": 5, "classificacaoDeSeguranca": "5 estrelas", "preco": 292242.21},
    {"id": 23, "marca": "Jeep", "modelo": "Wrangler Sahara", "ano": 2024, "tipoDeCombustivel": "Diesel", "consumoKmL": None, "potenciaCv": 116, "zeroACemKmH": 5.46, "classificacaoDeSeguranca": "3 estrelas", "preco": 196136.87},
    {"id": 24, "marca": "RAM", "modelo": "Laramie Longhorn", "ano": 2024, "tipoDeCombustivel": "Diesel", "consumoKmL": None, "potenciaCv": 391, "zeroACemKmH": 4.5, "classificacaoDeSeguranca": "5 estrelas", "preco": 341129.93},
    {"id": 25, "marca": "Chrysler", "modelo": "Sebring Convertible", "ano": 2024, "tipoDeCombustivel": "Diesel", "consumoKmL": "11.01", "potenciaCv": 569, "zeroACemKmH": 9.64, "classificacaoDeSeguranca": "4 estrelas", "preco": 280458.69},
    {"id": 26, "marca": "Dodge", "modelo": "Durango Dominator", "ano": 2024, "tipoDeCombustivel": "Gasolina", "consumoKmL": "7.08", "potenciaCv": 589, "zeroACemKmH": 10.99, "classificacaoDeSeguranca": "5 estrelas", "preco": 270300.62},
    {"id": 27, "marca": "Jeep", "modelo": "Grand Cherokee Summit", "ano": 2024, "tipoDeCombustivel": "Gasolina", "consumoKmL": "6.73", "potenciaCv": 574, "zeroACemKmH": 7.1, "classificacaoDeSeguranca": "3 estrelas", "preco": 125210.36},
    {"id": 28, "marca": "RAM", "modelo": "Power Wagon Xtreme", "ano": 2024, "tipoDeCombustivel": "Elétrico", "consumoKmL": "-", "potenciaCv": 102, "zeroACemKmH": 5.99, "classificacaoDeSeguranca": "4 estrelas", "preco": 203052.36},
    {"id": 29, "marca": "Chrysler", "modelo": "Crossfire Roadster", "ano": 2024, "tipoDeCombustivel": "Diesel", "consumoKmL": None, "potenciaCv": 123, "zeroACemKmH": 9.29, "classificacaoDeSeguranca": "5 estrelas", "preco": 280220.28},
    {"id": 30, "marca": "Dodge", "modelo": "Charger Daytona", "ano": 2024, "tipoDeCombustivel": "Gasolina", "consumoKmL": "14.78", "potenciaCv": 248, "zeroACemKmH": 4.79, "classificacaoDeSeguranca": "3 estrelas", "preco": 137592.11}
]

@app.get("/carro")
async def get_carros():
    return JSONResponse(content=carros)
