FROM python:3.8.10
# Define o diretóŕio de trabalho como sendo /app
WORKDIR /app
# Copia os conteúdos locais para dentro do container
ADD . /app
# Instala as dependências necessárias
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]