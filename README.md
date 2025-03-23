
# 🚀 Deploying a Flask App on AWS EC2 with Docker

A simple yet complete DevOps project that demonstrates how to containerize a Python Flask app using Docker, push it to Docker Hub, and deploy it on an AWS EC2 instance.

---

## 🗂️ Table of Contents
- [📌 Project Overview](#-project-overview)
- [🧱 Tech Stack](#-tech-stack)
- [📁 Key Files](#-key-files)
- [🚀 Step-by-Step Deployment](#-step-by-step-deployment)
  - [1️⃣ Dockerize the App](#1-dockerize-the-app)
  - [2️⃣ Push to Docker Hub](#2-push-to-docker-hub)
  - [3️⃣ Launch EC2 Instance](#3-launch-ec2-instance)
  - [4️⃣ Deploy App on EC2](#4-deploy-app-on-ec2)
- [📸 Deployment Proof](#-deployment-proof)
- [🛠️ Future Improvements](#️-future-improvements)
- [📬 Contact](#-contact)

---

## 📌 Project Overview

This project shows how to:

✅ Dockerize a Flask web app  
✅ Push the Docker image to Docker Hub  
✅ Deploy the container on a remote AWS EC2 instance  
✅ Run the application and expose it via HTTP (port 80)

---

## 🧱 Tech Stack

| Purpose            | Tool                        |
|--------------------|-----------------------------|
| App Framework      | Flask (Python)              |
| Containerization   | Docker                      |
| Image Registry     | Docker Hub                  |
| Cloud Hosting      | AWS EC2 (Ubuntu 22.04)      |

---

## 📁 Key Files

| File                  | Description                            |
|-----------------------|----------------------------------------|
| `Dockerfile`          | Defines the Docker image               |
| `docker-compose.yml`  | (Optional) Multi-service config        |
| `app.py`              | Main Flask application                 |
| `requirements.txt`    | Python dependencies                    |

---

## 🚀 Step-by-Step Deployment

### 1️⃣ Dockerize the App

```bash
docker build -t your-app:v1 .
docker run -d -p 5000:5000 your-app:v1
```
### 2️⃣ Push to Docker Hub
```
docker login -u redskot
docker tag your-app:v1 redskot/your-app:v1
docker push redskot/your-app:v1` 
```
➡️ Image now available on Docker Hub.

----------

### 3️⃣ Launch EC2 Instance

-   Instance Type: `t2.micro` (Free Tier)
    
-   OS: `Ubuntu 22.04`
    
-   Open ports: `22` (SSH), `80` (HTTP), `5000` (App)
    

Connect via SSH:

bash

CopierModifier

`ssh -i "my-key.pem" ubuntu@<EC2_PUBLIC_IP>` 

Install Docker on EC2:


```
`sudo apt update -y
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER` 
```

Logout/login again to apply Docker permissions.

----------

### 4️⃣ Deploy App on EC2


```
docker pull redskot/your-app:v1
docker run -d -p 80:5000 --name my-app redskot/your-app:v1` 
```
➡️ App available at: `http://<EC2_PUBLIC_IP>`

----------

## 📸 Deployment Proof

https://www.notion.so/image/attachment%3A1ae4eccd-0763-4e30-a57f-228eb452fa6c%3Aimage.png?table=block&id=1b6eb982-b3f4-8091-9a2e-c362b8993698&spaceId=da4d5e6f-93f6-4955-b0ae-a4b8b257987a&width=2000&userId=c294cf5f-12a9-475c-ba4c-4944a5aeeb5a&cache=v2

## 🛠️ Future Improvements

-   ✅ Automate infrastructure with **Terraform**
    
-   ✅ Manage multi-host setup with **Ansible**
    
-   ✅ Add **CI/CD pipeline** using GitHub Actions
    
-   ⏳ Add domain + SSL (Let's Encrypt or Route 53 + ACM)
    

----------

## 📬 Contact

Made with 💻 by **Mohamed-Rédha Bouras**  
[LinkedIn](https://linkedin.com/in/redhabouras) · [GitHub](https://github.com/redskot)  
Open to collaboration and DevOps opportunities.


