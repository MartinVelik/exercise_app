import requests
import datetime
import my_env_val
import os



def exercise():
    NUTRITION_ENDPOINT = "XXXXX"

    header = {
        "x-app-id": NUTRITION_ID,
        "x-app-key": APP_KEY,
        "Content-Type": "application/json"
    }
    json_data = {
        "query": query,
        "gender": 'male',
        "weight_kg": weight_kg,
        "height_cm": height_cm,
        "age": age

    }

    response = requests.post(url=NUTRITION_ENDPOINT, json=json_data, headers=header)
    data = response.json()

    user_input = data['exercises'][0]['user_input']
    duration_min = data['exercises'][0]['duration_min']
    calories = data['exercises'][0]['nf_calories']

    today = datetime.datetime.now()
    today_string = today.strftime("%d/%m/%Y")
    time_string = today.strftime("%H:%M:%S")

    SHEETY_ENDPOINT = 'XXXX'
    sheety_response = requests.get(url=SHEETY_ENDPOINT)
    sheety_response.json()

    workouts_data = {
        'workout': {'date': today_string,
                    'time': time_string,
                    'exercise': user_input,
                    "duration": duration_min,
                    "calories": calories
                    }

    }
    header = {
        "Authorization": TOKEN
    }

    return requests.post(url=SHEETY_ENDPOINT, json=workouts_data, headers=header)


user_choice = True

while user_choice:
    query = input("Please enter your activity: ")
    gender = input("Please enter your gender: ")
    weight_kg = int(input("Please enter your weight: "))
    height_cm = int(input("Please enter your height: "))
    age = int(input("Please enter your age: "))
    continue_input = input("Would you like to continue enter inputs yes or no: ").lower()
    if continue_input == 'no':
        exercise()
        print("The data has been written...")
        user_choice = False
    elif continue_input == 'yes':
        exercise()
        print("The data has been written...")

