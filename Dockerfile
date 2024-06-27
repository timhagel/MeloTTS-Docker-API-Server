FROM python:3.9
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN git clone https://github.com/myshell-ai/MeloTTS.git
WORKDIR /MeloTTS
RUN pip install --no-cache-dir -e .
RUN python -m unidic download
WORKDIR /
COPY . .
EXPOSE 8080
CMD ["python", "app.py"]