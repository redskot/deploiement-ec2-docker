# Utilisez une image de base légère avec Python
FROM python:3.8-slim

# Créez et définissez le répertoire de travail
WORKDIR /app

# Copiez les fichiers nécessaires dans le conteneur
COPY requirements.txt .
COPY app.py .
COPY templates/ ./templates

# Installez les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposez le port sur lequel l'application sera accessible
EXPOSE 5000

# Commande pour démarrer l'application Flask
CMD ["python", "app.py"]
