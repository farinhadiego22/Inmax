FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip \
    && pip install fastapi uvicorn \
    && if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
