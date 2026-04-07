FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install fastapi uvicorn pydantic openenv-core

COPY . .

CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]
