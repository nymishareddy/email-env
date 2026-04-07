FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir fastapi==0.110.0 uvicorn==0.29.0 pydantic==2.6.4 openenv-core>=0.2.0

CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]
