import requests
import datetime
import os
Application_id = os.environ['Application_id']
Application_Keys = ''
Nutrionix_api_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
Nutrionix_api_params = {
    'query': input('What excercises you did ?'),

}
Nutrionix_api_header = {
    'x-app-id': Application_id,
    'x-app-key': Application_Keys
}

received_data = requests.post(
    url=Nutrionix_api_url, json=Nutrionix_api_params, headers=Nutrionix_api_header)
data_json = received_data.json()
sheety_url = 'https://api.sheety.co//dietStats/workouts'
auth = ('', '')
for i in data_json['exercises']:
    excersise_name = i['user_input']
    excersise_duration = i['duration_min']
    excersise_calories = i['nf_calories']
    sheety_body = {
        "workout": {'date': datetime.datetime.now().strftime('%d/%m/%Y'),
                    'time': datetime.datetime.now().strftime('%H:%M:%S'),
                    'exercise': f'{excersise_name.title()}',
                    'duration': f'{excersise_duration}',
                    'calories': f'{excersise_calories}'}
    }
    response_post = requests.post(
        url=sheety_url, json=sheety_body, auth=auth)


# sheety_url = 'https://api.sheety.co//dietStats/workouts'
# sheety_body = {
#     "workout": {'date': datetime.datetime.now().strftime('%d/%m/%Y'),
#                 'time': datetime.datetime.now().strftime('%H:%M:%S'),
#                 'exercise': f'{excersise_name.title()}',
#                 'duration': f'{excersise_duration}',
#                 'calories': f'{excersise_calories}'}
# }

#   getting the data
# response_get = requests.get(url=sheety_url)
# print(response_get.json())

#   posting the data   add row to data
# response_post = requests.post(url=sheety_url, json=sheety_body)
# print(response_post.text)
