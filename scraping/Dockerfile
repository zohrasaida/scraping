FROM python:3.10-slim-buster
WORKDIR  /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# EXPOSE 8000
# CMD ["uvicorn", "main:app", "0.0.0.0", "--port" , "8000"]