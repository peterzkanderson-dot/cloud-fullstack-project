# Cloud Full-Stack Deployment

### Final Project             

## Task Description

You are asked to create and deploy a full-stack application to the cloud, complete with performance optimization, security configurations, monitoring, and scaling strategies. This project will become part of your professional portfolio.
________________________________________

## Project Overview

This project demonstrates a real-time monitoring system that collects power metrics (voltage, current, power, etc.), processes them through a cloud pipeline, and visualizes them using Grafana.

## Technical Project Criteria

- CI/CD – Automatic Pipeline
- Deployment – Deployment on AWS
- Security – AWS Security Groups & Token-based authentication
- Monitoring – Log and Dashboard
- Scaling – Manual Scaling
- Documentation – A clear and complete README file

## Technologies Used

Here will be using a verity of tools to complete our project.
 
- AWS EC2 (cloud hosting) 
- Docker (containerization) 
- MQTT (data communication) 
- InfluxDB (time-series database) 
- Grafana (visualization) 
- Python (simulator + ingestion)

Here will break down step by step following the Technical Project Criteria and the tech I have used in this project. 



## CI/CD  - Pipeline


Here I created my folders and files to organize them for my repository.

<img width="463" height="261" alt="image" src="https://github.com/user-attachments/assets/1be52cba-befc-4318-a0f0-f541128bd505" />


<img width="491" height="262" alt="image" src="https://github.com/user-attachments/assets/8582983e-18d5-4288-ba83-cde4d113db4e" />


A basic CI/CD pipeline was implemented using GitHub Actions to automate the build and validation process. Every time code is pushed to the main branch, the workflow is triggered to install dependencies and run a simple validation script. This ensures that the project maintains consistency and correctness during development.


<img width="975" height="489" alt="image" src="https://github.com/user-attachments/assets/4520a227-4cfa-4d91-b3d7-1b89680f5dd2" />


CI/CD implemented using GitHub Actions to automate build and validation on code push. Here is a link to check it out:
https://github.com/peterzkanderson-dot/cloud-fullstack-project/actions/runs/26691330333



## Deployment – Deployment on AWS


The system was deployed on an AWS EC2 instance using Docker Compose. Core services including InfluxDB, Grafana, and the MQTT broker were containerized and managed efficiently. The simulator and ingestion services were executed on the instance to enable real-time data processing and visualization through Grafana.


<img width="975" height="441" alt="image" src="https://github.com/user-attachments/assets/d8b2ace0-25dd-4b61-8aa4-606b11e71a36" />


The system is deployed on AWS EC2, where the simulator sends real-time data and the ingestion service processes and stores it in InfluxDB, confirming successful cloud deployment.


<img width="975" height="519" alt="image" src="https://github.com/user-attachments/assets/12a61d56-81ef-4bfc-9257-df6a276d724d" />


<img width="974" height="466" alt="image" src="https://github.com/user-attachments/assets/c78869d8-e460-4457-b6ea-eb3c6cdb1a79" />


The application is deployed on an AWS EC2 instance, which serves as the cloud environment for running all system components. The instance hosts Docker containers for InfluxDB, Grafana, and the MQTT broker, as well as the simulator and ingestion services. This confirms that the system is successfully deployed and operational in a cloud-based infrastructure.


The Grafana dashboard confirms successful deployment by visualizing real-time data stored in InfluxDB, demonstrating that the system is fully functional.


<img width="975" height="446" alt="image" src="https://github.com/user-attachments/assets/f694d60a-1960-4dc6-b005-10e054432e3e" />


<img width="975" height="447" alt="image" src="https://github.com/user-attachments/assets/588f03f4-45f6-4921-be5b-73f67ee885af" />



## Security – AWS Security Groups & Token-based Authentication


Basic security measures were implemented by configuring AWS Security Groups to restrict access to only required ports (e.g., 3000 for Grafana, 8086 for InfluxDB, and 22 for SSH). Additionally, InfluxDB uses token-based authentication to securely manage access to the database, ensuring that sensitive operations are protected.


<img width="975" height="443" alt="image" src="https://github.com/user-attachments/assets/119d205a-8133-4e15-b181-7b494120a356" />


<img width="975" height="485" alt="image" src="https://github.com/user-attachments/assets/688971a7-27e9-46f4-a876-efd9701b5e25" />

Here, I used the token generated from InfluxDB for authentication. 



## Monitoring – Log and Dashboard


Monitoring was achieved through Grafana dashboards and system logs. Real-time data such as voltage, current, power, and other metrics are visualized using Grafana, while logs from the simulator and ingestion services provide insight into system activity and data flow. This allows effective tracking and debugging of the system.

Link for Grafana Dashboard: http://54.255.150.187:3000 


<img width="975" height="483" alt="image" src="https://github.com/user-attachments/assets/28f666c9-f46d-4758-b5b0-f283958a2a74" />


<img width="975" height="519" alt="image" src="https://github.com/user-attachments/assets/6b6c858c-8a59-4cee-8c6a-caa72fd062b6" />



## Scaling – Manual Scaling


The system supports manual scaling by allowing additional instances of services to be deployed if needed. For example, ingestion services can be replicated to handle increased data load, and the EC2 instance resources can be upgraded. This demonstrates the system’s ability to scale based on demand.



## Documentation – README File


A comprehensive README file was created and maintained in the project’s GitHub repository. It includes an overview of the system, architecture, technologies used, deployment steps, and usage instructions. This ensures that the project is well-documented and easy to understand and reproduce.












