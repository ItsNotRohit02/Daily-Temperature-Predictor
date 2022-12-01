# Temperature Predictor
## How it Works
This Program uses a Machine Learning Algorithm called Decision Tree Regression to learn from over 800,000 data entries 
collected over 25 years across 88 cities and 46 countries to create a complex and accurate model to predict the temperature of any 
city at any given day of the year.
## Click Link Below 
[Click Here to see the Program in action](https://itsnotrohit02-daily-temperature-predictor-temperatureapp-1ia1gd.streamlit.app/)
## How to Use the Program
* Download the DailyTemperatures.csv file.
* Download the required libraries as mentioned in the requirements.txt file.
* Run TemperatureFinal.py . This creates the TemperatureMLModel.joblib file.
* Run the TemperatureApp.py using "streamlit run TemperatureApp.py" command in the command prompt while in the program directory.
* This should open a webpage that looks like [this](https://itsnotrohit02-daily-temperature-predictor-temperatureapp-1ia1gd.streamlit.app/).

## Extra
* The Accuracy Score of the ML Model is 91%.
* Due to 100MB file size restriction on GitHub, I had to severely reduce the 
number of cities in the Program. 
* Download FullTemperaturePredictor.zip and check it out as it contains the original program
with 148 cities along with the original csv file.
* The original program used 1,500,000 data entries.