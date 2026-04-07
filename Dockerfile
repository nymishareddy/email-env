FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn pydantic openenv-core

CMD ["python", "-m", "uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]
