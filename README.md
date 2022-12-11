# Temperature Predictor
## How it Works
This Python program uses the streamlit, pandas and sklearn libraries to train a decision tree regression model on a dataset of 
daily temperature data. The dataset is read in using the pandas library and stored in a DataFrame called rawdata. 
The features (or independent variables) for the model are stored in the DataFrame X, while the target (or dependent variable) 
is stored in the variable y.

The sklearn library is then used to create a decision tree regression model and train it on the data stored in X and y. 
The trained model is then saved to a file called TemperatureMLModel.joblib using the joblib library.

The streamlit library is used to create a user interface for the program. The user is able to select a city from a list of options,
and the program uses the machine learning model to predict the temperature for that city for any day of the year.
The Program learns from over 800,000 data entries 
collected over 25 years across 88 cities and 46 countries to create a complex and accurate model.

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