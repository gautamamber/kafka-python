# KafkaUserSync

**KafkaUserSync** is a microservice that synchronizes user data between a MongoDB database and Kafka topics. The service consists of two main features:
- **Create User**: Creates new user records in MongoDB and publishes the events to a Kafka topic (`user_creations`).
- **Update User**: Updates user records in MongoDB and publishes the events to a Kafka topic (`user_updates`).

The service uses **FastAPI** for the API layer, **Confluent Kafka** for event streaming with **Avro schema** for data serialization, and **MongoDB** for user data storage.

## Features
- Create new users via API.
- Update existing users via API.
- Kafka Producer for publishing events to different topics.
- Kafka Consumer for reading user events and updating MongoDB.
- Avro schema for structured and serialized messaging.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)

## Technologies Used
- **Python**
- **FastAPI** for API endpoints
- **Confluent Kafka** for producer/consumer services
- **MongoDB** for data persistence
- **Avro** for data serialization
- **Docker** for setting up Kafka, MongoDB, and Schema Registry
- **Uvicorn** for running FastAPI

## Project Structure

```bash
kafka_user_sync/
│
├── avro_schemas/
│   └── user_update.avsc        # Avro schema for user events
│
├── app/
│   ├── __init__.py             # Initializes the FastAPI app
│   ├── main.py                 # Contains the FastAPI app with user APIs
│   ├── producer.py             # Kafka producer logic
│   └── consumer.py             # Kafka consumer logic
│
├── docker-compose.yml          # Docker setup for Kafka, MongoDB, and Schema Registry
│
├── requirements.txt            # Python dependencies
│
├── README.md                   # Project documentation
│
└── scripts/
    └── create_topics.sh        # Script to create Kafka topics
# kafka-python
