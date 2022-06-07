import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "wei"
TOKEN = "wei489489"

header = {
     "X-USER-TOKEN":TOKEN
 }

# user_params = {
#     "token":TOKEN,
#     "username":USERNAME,
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
#
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id":"graph1",
#     "name":"Cycling Graph",
#     "unit":"Km",
#     "type":"float",
#     "color":"shibafu",
# }

#
# graph_response = requests.post(url=graph_endpoint,json=graph_config,headers=header)
# print(graph_response.text)
# post_pixel= f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
#
today = datetime(year=2022,month=5,day=30)
#
# pixel_params = {
#     "date":today.strftime("%Y%m%d"),
#     "quantity":"10",
# }
# pixel_response = requests.post(url=post_pixel,json=pixel_params,headers=header)
# print(pixel_response.text)

# update data
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
# update_params = {
#     "quantity":"11.5",
# }
# response = requests.put(url=update_endpoint,json=update_params,headers=header)
# print(response.text)

# delete data

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint,headers=header)
print(response.text)