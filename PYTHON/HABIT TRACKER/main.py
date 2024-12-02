import datetime
import requests


#   creating new user
pixela_api_create_user_url = 'https://pixe.la/v1/users'
pixela_parameters_create_user = {
    'token': '',
    'username': '',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
# received_data = requests.post(url=pixela_api_create_user_url, json=pixela_parameters_create_user)
# data_json = received_data.json()
# print(data_json)


#   creating new graph
username = ''
token = ''
# pixela_api_create_graph_url = f'{pixela_api_create_user_url}/{username}/graphs'
# pixela_parameters_create_graph = {
#     'id': 'graph1',
#     'name': 'coding_graph',
#     'unit': 'hr',
#     'type': 'float',
#     'color': 'ichou'
# }
pixela_api_header = {
    'X-user-TOKEN': token
}
graphID = 'graph1'
# response = requests.post(url=pixela_api_create_graph_url,
#                          json=pixela_parameters_create_graph, headers=pixela_api_header)
# print(response.text)


# posting value to graph
# posting_graph_endpoint = f'{pixela_api_create_user_url}/{username}/graphs/{graphID}'
# today = datetime.datetime.now()
# posting_parameters = {
#     'date': today.strftime('%Y%m%d'),
#     'quantity': '3.5'
# }
# data = requests.post(url=posting_graph_endpoint,
#                      json=posting_parameters, headers=pixela_api_header)
# print(data.text)


#   updating value of graph
# update_graph_url = f'{pixela_api_create_user_url}/{username}/graphs/graph1/20240114'
# update_params = {
#     'quantity': '5.6'
# }
# update_data = requests.put(
#     url=update_graph_url, json=update_params, headers=pixela_api_header)
# print(update_data.text)

#   delete a grapg data
delete_graph_url = f'{pixela_api_create_user_url}/{username}/graphs/graph1/20240114'
delete_data = requests.delete(url=delete_graph_url, headers=pixela_api_header)
print(delete_data.text)
