# Olympic Medals Prediction App

This application predicts the number of medals a country might win in the Olympics based on various factors like team size, previous performance, and athlete statistics.

## Prerequisites

Before running the application, make sure you have the following installed:

1. Python 3.8 or higher
2. Node.js and npm (LTS version)

## Setup

### Backend Setup

1. Navigate to the api directory:
```bash
cd api
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Make sure your trained model file (`model.joblib`) is in the api directory

4. Start the backend server:
```bash
uvicorn main:app --reload
```

The backend will be running at http://localhost:8000

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be running at http://localhost:5173

## Using the Application

1. Open your web browser and go to http://localhost:5173
2. Fill in the form with the team's data:
   - Team Code (e.g., "USA", "GBR")
   - Country name
   - Year (e.g., 2024)
   - Number of events the team is participating in
   - Number of athletes
   - Average age of athletes
   - Average height of athletes (in cm)
   - Average weight of athletes (in kg)
   - Previous Olympics medals
   - Average medals in the last 3 Olympics
3. Click "Predict Medals" to get the prediction

## API Endpoints

- GET `/`: Welcome message
- POST `/predict`: Predict medals based on input data

## Technologies Used

- Backend: FastAPI, scikit-learn, pandas
- Frontend: React, TypeScript, Material-UI
- Model: Trained using scikit-learn 