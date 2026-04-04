FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Avisa ao Docker que o contêiner vai usar a porta 8000
EXPOSE 8000

# Inicia o servidor web uvicorn mantendo o contêiner vivo
CMD ["uvicorn", "monitor_api:app", "--host", "0.0.0.0", "--port", "8000"]