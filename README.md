# Weather Forecast Application

## Overview

This project is a web application built using Streamlit and Plotly that allows users to view weather forecasts for a specified number of days. The application utilizes the OpenWeatherMap API to retrieve forecast data and displays temperature trends and sky conditions. Users can select a place and the number of days for which they want to view the forecast.

## Features

- **Temperature Forecast**: Displays a line chart showing temperature trends over the specified number of days.
- **Sky Condition**: Shows images representing different sky conditions based on the forecast data.

## Installation

### Prerequisites

Ensure you have Python 3.7 or later installed on your system. You will also need to have an API key from OpenWeatherMap.

### Setup

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
2. **Create a virtual environment** 
     ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
4. **Set Up Environmental variables**
   Add your OpenWeatherMap API key to your environment variables. You can do this in your terminal or configure it in your IDE (e.g., PyCharm):
   ```bash
   export Api_key1="your_api_key_here"
5. **Run the streamlit App**
    ```bash
   streamlit run main.py