FROM python:3.9
RUN git clone https://github.com/myshell-ai/MeloTTS.git
WORKDIR /MeloTTS
RUN pip install -e .
RUN python -m unidic download
WORKDIR /
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "app.py"]