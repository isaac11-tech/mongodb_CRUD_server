# 🛡️ Enemy Soldiers CRUD API

This project provides a RESTful API built with **FastAPI** to perform CRUD operations on a MongoDB database containing enemy soldier records. The application is containerized with Docker and deployable to OpenShift.

## 📦 Project Structure

data-loader/
├── services/
│   └── data_loader/       # Data loading service  
├── scripts/               # OS and deployment scripts  
├── infrastructure/
│   └── k8s/               # Kubernetes manifests (YAMLs)  
├── Dockerfile             # Container image definition  
├── requirements.txt       # Python dependencies  
└── README.md              # Project documentation  

## 🧠 Features

- Create, Read, Update, Delete operations on soldier records  
- RESTful API endpoints using FastAPI  
- MongoDB integration via Docker or OpenShift  
- Deployment-ready Docker image  
- OpenShift-compatible manifests and routing  

## 🗃️ Data Model

Each soldier record includes the following fields:  
- `id`: Unique numeric identifier  
- `first_name`: First name of the soldier  
- `last_name`: Last name of the soldier  
- `phone_number`: Contact number  
- `rank`: Military rank  

## 🚀 API Endpoints

Base route: `/soldiersdb/`

| Method | Endpoint        | Description            |
|--------|-----------------|------------------------|
| GET    | `/soldiersdb/`  | Retrieve all soldiers  |
| POST   | `/soldiersdb/`  | Add a new soldier      |
| PUT    | `/soldiersdb/`  | Update soldier details |
| DELETE | `/soldiersdb/`  | Delete a soldier       |

## 🐳 Docker Instructions

1. Build the image:  
   `docker build -t <your-image-name> .`

2. Run MongoDB locally with Docker:  
   `docker run -d -p 27017:27017 --name mongodb mongo`

3. Push image to Docker Hub:  