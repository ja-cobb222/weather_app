# Overview

The Weather Information Server project is designed to demonstrate the principles of client-server architecture while integrating external APIs. The goal is to provide a user-friendly web application that fetches and displays real-time weather data for any city using the OpenWeatherMap API. This project aims to enhance my understanding of web development, networking, and API integration.

The software consists of a server backend built using FastAPI and a client frontend using HTML, CSS, and JavaScript. Users can input a city name into the web interface to fetch weather details such as temperature, humidity, wind speed, and a brief description of current conditions. 

The purpose of this software is to explore how client-server communication works in practice and to refine my skills in designing modular, scalable, and user-friendly applications.

[Software Demo Video](https://youtu.be/G33p8E1eaOI)

# Network Communication

The architecture used in this project is a **client-server model**. The client, implemented as a web-based interface, communicates with the server through HTTP requests. 

The server utilizes **TCP** for reliable communication and listens on **port 8000** by default. The client sends HTTP POST requests with JSON payloads to the server for weather data retrieval. The server responds with JSON-encoded weather information.

Example JSON request from client:
```json
{
    "city": "London"
}
```

Example JSON reply from server:
```json
{
    "city": "London",
    "temperature": 68.0,
    "description": "clear sky",
    "humidity": 45,
    "wind_speed": 5.5
}
```

# Development Environment

The software was developed using the following tools and technologies:

* Programming Language: Python 3.11
* Web Framework: FastAPI
* Frontend: HTML, CSS, and JavaScript
* Libraries:
    * httpx for asynchronous HTTP requests
    * pydantic for data validation
    * uvicorn as the ASGI server

Development was carried out in a Python virtual environment to manage dependencies.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [OpenWeatherMap API Documentation](https://openweathermap.org/api)
* [Python AsyncIO Guide](https://realpython.com/async-io-python/)
* [MDN Web Docs: Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

# Future Work

* Enhance the user interface to include more styling and interactive elements.
* Add support for weather forecasts in addition to current conditions.
* Implement user authentication for personalized weather dashboards.
* Introduce error handling for invalid city names directly on the client side.
* Expand support for additional weather metrics like air quality or UV index.