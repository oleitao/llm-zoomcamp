FROM python:3.10-slim

ENV STREAMLIT_PORT=8501
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.docker.txt .

RUN pip install --no-cache-dir -r requirements.docker.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
