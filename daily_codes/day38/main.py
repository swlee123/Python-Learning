
import requests
from datetime import datetime

APP_KEY = "981f43a27a5f256ff1efe9564312accb"
APP_ID = "7b0404bc"
API_END_POINT = "https://trackapi.nutritionix.com/v2"
SHEETY_API = "https://api.sheety.co/f3d237bc0b3539fec75652ab034dbf18/myWorkouts/workouts"

header = {
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,

}

exercise_text = input("What exercise you have done today? :")

param_body = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 168,
    "age": 19
}

response = requests.post(url=f"{API_END_POINT}/natural/exercise",json=param_body,headers=header)
response = response.json()

# create row

sheety_header ={
    "Authorization":"Basic c3dzdzpTV3FxNTIwMCEh"
}

duration = response["exercises"][0]
exercise = response["exercises"][0]
calories = response["exercises"][0]
today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

sheety_params = {

}
for exercise in response["exercises"]:
    sheety_params= {
        "workout":{
            "date":date,
            "time":time,
            "exercise":exercise["name"].title(),
            "duratiom":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }
sheety = requests.post(SHEETY_API,json=sheety_params,headers=sheety_header)
print(sheety.json())