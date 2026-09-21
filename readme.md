# Weather Data Pipeline & API

A modular weather data pipeline that fetches real-time weather information from an external Weather API, processes and cleans the raw response, performs feature engineering, and exposes the processed weather data through a FastAPI backend.

---

## 🚀 Features

* 🌤️ Real-time weather data retrieval
* 📍 Location-based weather search
* 🔑 Secure API-key management using environment variables
* 🧹 Data cleaning and transformation
* ⚙️ Feature engineering
* 📊 Structured Pandas DataFrame processing
* ⚡ FastAPI REST API
* 🌐 CORS support for frontend integration
* 🧩 Modular data-pipeline architecture
* 🗄️ Optional PostgreSQL support for storing historical weather data

---

## 🏗️ Architecture

```text
                         USER
                           │
                           │ City / Location
                           ▼
                    ┌───────────────┐
                    │    FastAPI    │
                    │   REST API    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  Weather API  │
                    │  Data Fetch   │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   Raw JSON    │
                    │     Data      │
                    └───────┬───────┘
                            │
                            ▼
               ┌────────────────────────┐
               │ Data Cleaning &        │
               │ Transformation         │
               │                        │
               │ • Missing values       │
               │ • Data types           │
               │ • Unit conversion      │
               │ • Data normalization   │
               └───────────┬────────────┘
                           │
                           ▼
               ┌────────────────────────┐
               │ Feature Engineering    │
               │                        │
               │ • Temperature features│
               │ • Humidity features    │
               │ • Wind features        │
               │ • Time features        │
               │ • Weather indicators   │
               └───────────┬────────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Processed Data  │
                  │ Pandas DataFrame│
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   API Response  │
                  └────────┬────────┘
                           │
                           ▼
                      Frontend /
                    Other Clients
```

---

## 📁 Project Structure

```text
DATAPIPELINEREPO/
│
├── backend/
│   │
│   ├── API/
│   │   └── main.py
│   │
│   ├── ingestion/
│   │   └── fetch_weather.py
│   │
│   ├── processing/
│   │   └── clean_transform.py
│   │
│   ├── storage/
│   │   ├── db.py
│   │   └── insert_data.py
│   │
│   └── pipeline.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### Module Responsibilities

| Module                          | Responsibility                                                 |
| ------------------------------- | -------------------------------------------------------------- |
| `API/main.py`                   | FastAPI application and REST endpoints                         |
| `ingestion/fetch_weather.py`    | Fetches weather data from the external API                     |
| `processing/clean_transform.py` | Cleans, transforms, and engineers weather features             |
| `storage/db.py`                 | PostgreSQL connection management                               |
| `storage/insert_data.py`        | Stores processed weather data when database storage is enabled |
| `pipeline.py`                   | Coordinates the data-processing workflow                       |

---

## 🔄 Data Pipeline

The project follows a simple data-processing pipeline:

```text
User Input
    ↓
City / Location
    ↓
Weather API Request
    ↓
Raw JSON Response
    ↓
Data Cleaning
    ↓
Data Transformation
    ↓
Feature Engineering
    ↓
Processed Pandas DataFrame
    ↓
JSON Response
    ↓
Frontend / Client
```

---

## 🧹 Data Cleaning & Transformation

Weather API responses contain nested and sometimes unnecessary information. The processing layer converts the raw API response into a structured dataset.

The pipeline handles tasks such as:

* Handling missing values
* Converting data types
* Standardizing units
* Extracting required fields
* Flattening nested API responses
* Removing unnecessary attributes
* Normalizing weather information
* Converting timestamps into readable formats

---

## ⚙️ Feature Engineering

The pipeline derives useful features from the raw weather information.

### Raw weather attributes

```text
Temperature
Humidity
Pressure
Wind Speed
Cloudiness
Visibility
Rainfall
Timestamp
```

### Derived features

```text
Temperature Category
Humidity Category
Wind Category
Rain Indicator
Hour
Day
Month
Day of Week
```

Feature engineering makes the raw API data more structured and useful for downstream analytics and visualization.

---

## 🌐 API

### Base URL

```text
http://127.0.0.1:8000
```

### Health Check

```http
GET /
```

Example response:

```json
{
  "message": "Weather API is running. Use /weather/{city}"
}
```

### Get Weather by City

```http
GET /weather/{city}
```

Example:

```http
GET /weather/chennai
```

Example response:

```json
{
  "source": "weather_api",
  "city": "chennai",
  "data": [
    {
      "temperature": 30.5,
      "humidity": 78,
      "pressure": 1008,
      "wind_speed": 4.2
    }
  ]
}
```

---

## 🔐 Environment Configuration

API keys are stored using environment variables rather than being hard-coded in the application.

Create a `.env` file:

```env
WEATHER_MAP_KEY=your_api_key_here
```

Load the key using `python-dotenv`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_MAP_KEY = os.getenv("WEATHER_MAP_KEY")
```

### Security

Add `.env` to `.gitignore`:

```gitignore
.env
__pycache__/
*.pyc
.venv/
weather/
```

**Never commit API keys or database credentials to GitHub.**

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### Data Processing

* Pandas
* NumPy

### Data Source

* Weather API

### Database

* PostgreSQL
* Psycopg2

### Configuration

* Python Dotenv

### Development

* Git
* GitHub
* Python Virtual Environment

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd DATAPIPELINEREPO
```

### 2. Create a virtual environment

```bash
python -m venv weather
```

Activate on Linux/macOS:

```bash
source weather/bin/activate
```

Windows:

```bash
weather\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env`:

```env
WEATHER_MAP_KEY=your_api_key
```

---

## ▶️ Running the Application

Run the FastAPI server from the project root:

```bash
python -m uvicorn backend.API.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### Interactive API Documentation

FastAPI automatically provides Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative documentation:

```text
http://127.0.0.1:8000/redoc
```

---

## 🧪 Testing the API

Using a browser:

```text
http://127.0.0.1:8000/weather/chennai
```

Using `curl`:

```bash
curl http://127.0.0.1:8000/weather/chennai
```

---

## 🗄️ Optional Database Layer

PostgreSQL can optionally be used to store processed weather data for historical analysis.

```text
Weather API
     ↓
Data Processing
     ↓
Feature Engineering
     ↓
PostgreSQL
     ↓
Historical Weather Data
```

The current weather endpoint can also operate directly without PostgreSQL:

```text
Weather API
     ↓
Data Processing
     ↓
API Response
```

This allows the project to support both **real-time processing** and **historical data storage**.

---

## 🔮 Future Enhancements

* [ ] Historical weather dashboard
* [ ] Interactive weather charts
* [ ] Automated periodic data collection
* [ ] Expanded feature engineering
* [ ] PostgreSQL-based historical analysis
* [ ] Redis caching
* [ ] Frontend dashboard
* [ ] Docker deployment
* [ ] Automated API testing
* [ ] CI/CD pipeline
* [ ] Location-based weather detection

---

## 🔒 Security Considerations

* API keys are stored using environment variables.
* Secrets are excluded from version control.
* Database credentials should not be hard-coded.
* User input should be validated before sending API requests.
* Production CORS configuration should restrict allowed origins instead of using `["*"]`.

---

## 📌 Project Status

**Development**

Current implementation includes:

1. Weather API integration
2. Weather data ingestion
3. Data cleaning
4. Data transformation
5. Feature engineering
6. FastAPI REST API
7. Optional PostgreSQL storage

---

## 👨‍💻 Author

**Dhinesh S**

B.Tech — Artificial Intelligence & Data Science
Bannari Amman Institute of Technology

---

## 📄 License

This project is intended for educational and development purposes. Add an appropriate open-source license if you plan to distribute the project publicly.
