from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field
from typing import List, Dict
from datetime import date

app = FastAPI(
    title="API de Reportes de Inversión y Gastos",
    description="Endpoints para inversión por tipo de producto y evolución de gastos por campaña.",
    version="1.0.0"
)

# ---------------------------------------------------
# 📦 Modelos
class InversionPorLocalidad(BaseModel):
    tipo_producto: str
    inversion_total: float
    localidad: str

class GastoPorFecha(BaseModel):
    fecha: date
    monto: float

# ---------------------------------------------------
# 🔄 Datos de ejemplo
INVERSION_LOCALIDAD = {
    1: [
        {"tipo_producto": "Redes Sociales", "inversion_total": 5000.0, "localidad": "Santiago"},
        {"tipo_producto": "Publicidad en Google", "inversion_total": 3000.0, "localidad": "Valparaíso"}
    ],
    2: [
        {"tipo_producto": "Anuncios en video", "inversion_total": 8000.0, "localidad": "Bogotá"}
    ]
}

EVOLUCION_GASTOS = {
    1: [
        {"fecha": date(2025, 6, 1), "monto": 2500.0},
        {"fecha": date(2025, 6, 2), "monto": 3000.0},
        {"fecha": date(2025, 6, 3), "monto": 4500.0}
    ],
    2: [
        {"fecha": date(2025, 7, 1), "monto": 4000.0},
        {"fecha": date(2025, 7, 2), "monto": 2000.0}
    ]
}

# ---------------------------------------------------
# 41) GET /reportes/inversion/localidad
@app.get("/reportes/inversion/localidad", response_model=List[InversionPorLocalidad], summary="Inversión por tipo de producto y localidad")
async def inversion_por_localidad(
    id_campaña: int = Path(..., description="ID de la campaña")
):
    datos = INVERSION_LOCALIDAD.get(id_campaña)
    if not datos:
        raise HTTPException(status_code=404, detail="No hay datos de inversión para esta campaña.")
    return datos

# 42) GET /reportes/evolucion-gastos
@app.get("/reportes/evolucion-gastos", response_model=List[GastoPorFecha], summary="Evolución de gastos de una campaña")
async def evolucion_gastos(
    id_campaña: int = Path(..., description="ID de la campaña")
):
    datos = EVOLUCION_GASTOS.get(id_campaña)
    if not datos:
        raise HTTPException(status_code=404, detail="No hay datos de gastos para esta campaña.")
    return datos

# ---------------------------------------------------
# Endpoint raíz de prueba
@app.get("/", summary="API de Reportes de Inversión y Gastos operativa")
def read_root():
    return {"message": "API de Inversión y Gastos lista y funcionando."}
