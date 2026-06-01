# Cloud Full-Stack Deployment

## Final Project             

##Task Description

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

<br>

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



















