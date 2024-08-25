# Borovnica Prehrana

Borovnica Prehrana is a web application for calculating and managing nutrition plans for blueberry plantations. This application allows users to input quantities of various preparations and plot sizes, then calculates the required amounts of each preparation per plot.

## Features

- Input quantities for different preparations (in g/plant)
- Input number of plants for each plot
- Calculate required preparation quantities per plot
- Specify the number of applications
- Export results to TXT and Excel formats
- User-friendly web interface using Streamlit

## Files

- `app.py`: Main application file containing the Streamlit web interface and calculation logic
- `export.py`: Module for exporting results to a text file
- `export_excel.py`: Module for exporting results to an Excel file
- `preparati.txt`: List of preparations
- `parcele.txt`: List of plots and their default plant counts
- `run_app.bat`: Batch file to run the application

## Requirements

- Python 3.7+
- Streamlit
- openpyxl

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/borovnica-prehrana.git
   cd borovnica-prehrana
   ```

2. Install the required packages:
   ```
   pip install streamlit openpyxl
   ```

## Usage

1. Run the application:
   ```
   streamlit run app.py
   ```
   or double-click on `run_app.bat`


