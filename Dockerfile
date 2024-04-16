# Use a imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie todos os arquivos do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Exponha a porta em que o Flask está sendo executado
EXPOSE 3000

# Comando para iniciar o aplicativo Flask quando o contêiner for iniciado
CMD ["python", "app.py"]