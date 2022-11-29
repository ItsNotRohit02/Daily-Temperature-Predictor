import joblib
import streamlit as st
import datetime


model=joblib.load('TemperatureMLModel.joblib')
st.set_page_config(page_title="Temperature Predictor",page_icon=":bar_chart:")
st.title('Welcome to Temperature Predictor!')


with st.container():
    st.header('How we predict ?')
    st.write('We use a Machine Learning Algorithm called Decision Tree Regression to learn from over 800,000 data entries'
             ' collected over 25 years across 88 cities and 46 countries to create a complex and accurate model to predict the temperature of any'
             ' city at any given day of the year.')


with st.container():
    st.write('---')
    st.header('Select from Options below')
    city = st.selectbox('Select the City (Start Typing to Search)',['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'London',
                                                                    'Los Angeles', 'New York City', 'Las Vegas', 'Singapore', 'Paris',
 'Cairo', 'Lagos', 'Capetown', 'Dhaka', 'Beijing',
 'Shanghai', 'Hong Kong',  'Jakarta',
 'Osaka', 'Tokyo', 'Kuala Lumpur', 'Katmandu', 'Islamabad', 'Karachi',
  'Seoul', 'Colombo', 'Taipei', 'Bangkok',
 'Canberra', 'Melbourne',  'Sydney', 'Vienna', 'Brussels', 'Prague',
 'Athens', 'Budapest', 'Reykjavik', 'Dublin', 'Milan', 'Rome', 'Amsterdam',
  'Moscow', 'Barcelona', 'Madrid',
 'Stockholm', 'Geneva', 'Zurich', 'Kiev', 'Belfast',  'Tel Aviv',
 'Kuwait',  'Muscat', 'Doha', 'Riyadh','Istanbul',
 'Abu Dhabi', 'Dubai', 'Halifax', 'Montreal',
 'Toronto', 'Vancouver',  'Mexico City',
 'Rio de Janeiro',
 'Phoenix',  'Sacramento',
 'San Diego', 'San Francisco', 'Denver',
 'Washington DC',  'Miami', 'Orlando',
 'Honolulu', 'Chicago',
 'New Orleans', 'Portland',
 'Boston', 'Omaha', 'Reno',
  'Cleveland', 'Oklahoma City',
 'Philadelphia', 'Pittsburgh', 'Memphis', 'Nashville', 'Austin',
 'Houston', 'Salt Lake City', 'Seattle'])
    citydict={'Cairo':0, 'Nairobi':1, 'Lagos':2, 'Freetown':3, 'Capetown':4, 'Dhaka':5, 'Beijing':6,
 'Shanghai':7, 'Hong Kong':8, 'Mumbai':9, 'Kolkata':10, 'Chennai':11, 'Delhi':12, 'Jakarta':13,
 'Osaka':14, 'Tokyo':15, 'Kuala Lumpur':16, 'Katmandu':17, 'Islamabad':18, 'Karachi':19, 'Manila':20,
 'Singapore':21, 'Seoul':22, 'Colombo':23, 'Taipei':24, 'Bangkok':25, 'Hanoi':26, 'Brisbane':27,
 'Canberra':28, 'Melbourne':29, 'Perth':30, 'Sydney':31, 'Vienna':32, 'Brussels':33, 'Prague':34,
 'Copenhagen':35, 'Helsinki':36, 'Paris':37, 'Bordeaux':38, 'Frankfurt':39, 'Munich':40, 'Tbilisi':41,
 'Athens':42, 'Budapest':43, 'Reykjavik':44, 'Dublin':45, 'Milan':46, 'Rome':47, 'Amsterdam':48,
 'Oslo':49, 'Warsaw':50, 'Lisbon':51, 'Bucharest':52, 'Moscow':53, 'Barcelona':54, 'Madrid':55,
 'Stockholm':56, 'Bern':57, 'Geneva':58, 'Zurich':59, 'Kiev':60, 'Belfast':61, 'London':62, 'Tel Aviv':63,
 'Kuwait':64, 'Beirut':65, 'Muscat':66, 'Doha':67, 'Riyadh':68, 'Ankara':69, 'Istanbul':70,
 'Abu Dhabi':71, 'Dubai':72, 'Calgary':73, 'Edmonton':74, 'Halifax':75, 'Montreal':76, 'Ottawa':77,
 'Quebec':78, 'Toronto':79, 'Vancouver':80, 'Winnipeg':81, 'Mexico City':82, 'Buenos Aires':83,
 'Rio de Janeiro':84, 'Sao Paulo':85, 'Bogota':86, 'San Jose':87, 'Havana':88,
 'Guatemala City':89, 'Panama City':90, 'Birmingham':91, 'Huntsville':92, 'Anchorage':93,
 'Fairbanks':94, 'Phoenix':95, 'Tucson':96, 'Fresno':97, 'Los Angeles':98, 'Sacramento':99,
 'San Diego':100, 'San Francisco':101, 'Colorado Springs':102, 'Denver':103, 'Washington':104,
 'Washington DC':105, 'Daytona Beach':106, 'Jacksonville':107, 'Miami':108, 'Orlando':109,
 'Tampa St. Petersburg':110, 'Atlanta':111, 'Honolulu':112, 'Chicago':113, 'Rockford':114,
 'Springfield':115, 'Indianapolis':116, 'Louisville':117, 'New Orleans':118, 'Portland':119,
 'Baltimore':120, 'Boston':121, 'Detroit':122, 'Minneapolis':123, 'Kansas City':124, 'Omaha':125, 'Reno':126,
 'Las Vegas':127, 'Atlantic City':128, 'Newark':129, 'Buffalo':130, 'New York City':131,
 'Charlotte':132, 'Cincinnati':133, 'Cleveland':134, 'Oklahoma City':135, 'Tulsa':136,
 'Philadelphia':137, 'Pittsburgh':138, 'Rhode Island':139, 'Memphis':140, 'Nashville':141, 'Austin':142,
 'Houston':143, 'Salt Lake City':144, 'Seattle':145, 'Milwaukee':146, 'San Juan (Puerto Rico)':147}
    c=citydict[city]

    month = st.select_slider('Select Month',['Jan','Feb','March','April','May','June','July','Aug','Sep','Oct','Nov','Dec'])
    monthdict={'Jan':1,'Feb':2,'March':3,'April':4,'May':5,'June':6,'July':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    m=monthdict[month]

    d = st.slider('Select Day', 1, 31)
    today = datetime.date.today()
    y = today.year


with st.container():
    p=model.predict([[c,m,d,y]])
    f=p[0]
    t=(f-32)*(5/9)
    t1=round(t,2)
    f1=round(f,2)
    if(t<=0):
        st.snow()


col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label='Predicted Temperature', value=f"{t1} °C")
with col2:
    st.metric(label='', value=f"{f1} °F")


with st.container():
    st.success(f"The Temperature in {city} on {d} {month} is most likely going to be {t1} °C ")
    st.caption("Made by Rohit")

