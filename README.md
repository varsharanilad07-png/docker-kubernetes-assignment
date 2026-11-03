# docker-kubernetes-assignment

# 1. Project Title

**Containerization and Kubernetes Deployment of a Cloud-Native Web Application**

# 2. Objective

The objective of this project is to develop a simple web application and deploy it using modern cloud-native technologies. The application is first containerized using Docker and then deployed on a Kubernetes cluster.

The project demonstrates:
- Creating a Dockerfile for the application.
- Building and running a Docker image.
- Running the application inside a Docker container.
- Creating a Kubernetes Deployment with multiple replicas.
- Creating a Kubernetes Service to expose the application.
- Monitoring Pods, Deployments, and Services using Kubernetes commands.

# 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | Web application framework |
| Docker | Application containerization |
| Docker Desktop | Docker and Kubernetes environment |
| Kubernetes | Container orchestration |
| kubectl | Kubernetes command-line tool |
| YAML | Kubernetes configuration |
| Git | Version control |
| GitHub | Source code repository |
| VS Code | Development environment |

# 4. Project Structure

The project contains the following files and folders:

```text
docker-kubernetes-assignment/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
│
└── kubernetes/
    ├── deployment.yaml
    └── service.yaml
```

**Description of files:**

- `app.py` – Contains the Flask web application.
- `requirements.txt` – Contains the Python dependency required by the application.
- `Dockerfile` – Contains instructions for creating the Docker image.
- `.dockerignore` – Specifies files that should not be copied into the Docker image.
- `deployment.yaml` – Defines the Kubernetes Deployment and Pod configuration.
- `service.yaml` – Defines the Kubernetes Service used to expose the application.

# 5. Application Description

The project is a simple Flask-based web application created to demonstrate containerization and Kubernetes deployment.

When the user opens the application, it displays:

**Cloud Native Application**

**Docker + Kubernetes**

**Application deployed successfully!**

The Flask application runs on port **5000** and is configured to accept connections from outside the container using:

```python
app.run(host="0.0.0.0", port=5000)
```

The application is intentionally simple so that the main focus of the project remains on Docker containerization and Kubernetes deployment.

# 6. Docker Implementation

Docker is used to package the Flask application and its dependencies into a portable container image.

The Dockerfile uses the lightweight Python 3.11 Slim image as the base image.

Main Dockerfile instructions:

- `FROM python:3.11-slim` – Provides the Python environment.
- `WORKDIR /app` – Sets the working directory inside the container.
- `COPY requirements.txt .` – Copies the dependency file.
- `RUN pip install --no-cache-dir -r requirements.txt` – Installs Flask.
- `COPY app.py .` – Copies the application code.
- `EXPOSE 5000` – Documents the application port.
- `CMD ["python", "app.py"]` – Starts the Flask application.

The Docker image was created using:

```powershell
docker build -t cloud-native-app:1.0 .
```

The image was then used to create and run a container:

```powershell
docker run -d -p 5000:5000 --name cloud-native-container cloud-native-app:1.0
```

The running container was verified using:

```powershell
docker ps
```

The application was accessed through:

```text
http://localhost:5000
```

# 7. Kubernetes Deployment

Kubernetes is used to manage and run the Docker container.

A Kubernetes Deployment was created using the `deployment.yaml` configuration file.

The Deployment is configured with:

- **Deployment name:** `cloud-native-deployment`
- **Replicas:** 2
- **Container name:** `cloud-native-container`
- **Container port:** 5000
- **CPU request:** 100m
- **Memory request:** 128Mi
- **CPU limit:** 500m
- **Memory limit:** 256Mi

Two replicas were selected so that Kubernetes maintains two running instances of the application.

The Deployment was created using:

```powershell
kubectl apply -f kubernetes/deployment.yaml
```

The Deployment was verified using:

```powershell
kubectl get deployments
```

The Pods were checked using:

```powershell
kubectl get pods
```

The final result showed:

```text
cloud-native-deployment-xxxxx   1/1   Running
cloud-native-deployment-xxxxx   1/1   Running
```

This confirms that both application Pods were successfully running.

# 8. Kubernetes Service

A Kubernetes Service was created to provide network access to the application Pods.

The Service configuration uses:

- **Service name:** `cloud-native-service`
- **Service type:** `NodePort`
- **Service port:** 80
- **Target port:** 5000
- **NodePort:** 30080

The Service was created using:

```powershell
kubectl apply -f kubernetes/service.yaml
```

The Service was verified using:

```powershell
kubectl get services
```

The NodePort allows users to access the application through port **30080**.

The application can be accessed using:

```text
http://localhost:30080
```

The Service selects the application Pods using the label:

```yaml
app: cloud-native-app
```

# 9. Commands Used

The following commands were used during the implementation:

### Docker Commands

```powershell
docker build -t cloud-native-app:1.0 .
```

```powershell
docker images
```

```powershell
docker run -d -p 5000:5000 --name cloud-native-container cloud-native-app:1.0
```

```powershell
docker ps
```

```powershell
docker logs cloud-native-container
```

### Kubernetes Commands

Check Kubernetes node:

```powershell
kubectl get nodes
```

Create Deployment:

```powershell
kubectl apply -f kubernetes/deployment.yaml
```

Check Deployment:

```powershell
kubectl get deployments
```

Check Pods:

```powershell
kubectl get pods
```

Create Service:

```powershell
kubectl apply -f kubernetes/service.yaml
```

Check Services:

```powershell
kubectl get services
```

Check all Kubernetes resources:

```powershell
kubectl get all
```

Check application logs:

```powershell
kubectl logs <pod-name>
```

Restart Deployment when required:

```powershell
kubectl rollout restart deployment cloud-native-deployment
```

# 10. Output

The following outputs were obtained during the implementation:

### Docker Output

The Docker image was successfully built:

```text
cloud-native-app:1.0
```

The application successfully ran inside a Docker container and was accessible through:

```text
http://localhost:5000
```

### Kubernetes Output

The Kubernetes cluster was successfully running with a Ready node.

The Deployment showed:

```text
NAME                      READY   UP-TO-DATE   AVAILABLE
cloud-native-deployment   2/2     2            2
```

The Pods showed:

```text
cloud-native-deployment-xxxxx   1/1   Running
cloud-native-deployment-xxxxx   1/1   Running
```

This confirms that Kubernetes successfully created and managed two replicas of the application.

The Kubernetes Service was configured as a NodePort service using port `30080`.

The application was accessed through:

```text
http://localhost:30080
```

The browser displayed:

**Cloud Native Application**

**Docker + Kubernetes**

**Application deployed successfully!**

# 11. Conclusion

This project successfully demonstrated the containerization and deployment of a Flask web application using Docker and Kubernetes.

Docker was used to package the application and its dependencies into a portable image, while Kubernetes was used to manage the application containers through Pods and a Deployment. Two replicas were configured to demonstrate Kubernetes' ability to maintain multiple instances of an application.

A NodePort Service was also configured to provide external access to the application.

Overall, the project provided practical understanding of important cloud-native concepts such as **containerization, Docker images, containers, Kubernetes Pods, Deployments, replicas, Services, resource management, and application accessibility**.
