# Usa una imagen oficial con Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos y los instala
COPY requeri.txt .

RUN pip install --no-cache-dir -r requeri.txt

# Copia el resto del código fuente
COPY . .

# Expone el puerto donde correrá FastAPI (por defecto 8000)
EXPOSE 8000

# Comando para iniciar el servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
