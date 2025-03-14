🚀 Déploiement d'une application Flask sur AWS EC2 avec Docker
📌 Objectif
Ce projet consiste à déployer une application Flask sur une instance AWS EC2 en utilisant Docker. L’application est dockerisée, poussée sur Docker Hub, puis récupérée et exécutée sur EC2.

🛠 Technologies utilisées
AWS EC2 → Hébergement de l'application
Docker → Conteneurisation de l'application
Docker Hub → Stockage de l'image de l'application
Python + Flask → Application web
📂 Fichiers importants
Dockerfile → Définit l’image Docker de l’application
docker-compose.yml → Configuration du service avec PostgreSQL
app.py → Code de l’application Flask
requirements.txt → Liste des dépendances Python
🔹 1️⃣ Préparation : Dockerisation de l'application
Avant de la déployer sur AWS, l’application doit être conteneurisée avec Docker.

✔ Construire l’image Docker
bash
Copier
docker build -t your-app:v1 .
✔ Tester en local
bash
Copier
docker run -d -p 5000:5000 your-app:v1
📌 Accéder à l’application sur http://localhost:5000

🔹 2️⃣ Pousser l’image sur Docker Hub
✔ Se connecter à Docker Hub
bash
Copier
docker login -u redskot
✔ Tagger l’image avec le namespace Docker Hub
bash
Copier
docker tag your-app:v1 redskot/your-app:v1
✔ Pousser l’image sur Docker Hub
bash
Copier
docker push redskot/your-app:v1
📌 Vérification : L’image est maintenant disponible sur Docker Hub.

🔹 3️⃣ Déployer sur AWS EC2
✔ Lancer une instance EC2
Type : t2.micro (Free Tier)
OS : Ubuntu 22.04
Ports ouverts : 22 (SSH), 80 (HTTP), 5000 (Application)
✔ Se connecter en SSH
bash
Copier
ssh -i "ma_cle.pem" ubuntu@IP_DE_L_INSTANCE
✔ Installer Docker sur EC2
bash
Copier
sudo apt update -y
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
📌 Déconnecte-toi et reconnecte-toi pour appliquer les permissions Docker.

🔹 4️⃣ Récupérer et exécuter l'application sur EC2
✔ Télécharger l’image depuis Docker Hub
bash
Copier
docker pull redskot/your-app:v1
✔ Lancer l'application
bash
Copier
docker run -d -p 80:5000 --name mon-app redskot/your-app:v1
📌 Vérification : Accéder à http://IP_DE_L_INSTANCE pour voir l’application.

📷 Preuve du déploiement
Ajoute ici une capture d’écran montrant :

L’application en ligne sur AWS EC2
Le résultat de docker ps prouvant que le conteneur tourne
📌 Améliorations futures
✅ Automatiser avec Terraform
✅ Gérer plusieurs machines avec Ansible
✅ Ajouter un CI/CD avec GitHub Actions