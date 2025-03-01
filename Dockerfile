# Usa a imagem oficial do Python
FROM python:3-slim

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Define o diretório de trabalho
WORKDIR /app
COPY . /app

# Cria um usuário não-root
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Comando para rodar a aplicação
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "fabrica25.wsgi:application"]