import requests

import configuration
import data


#   Creating a user
def post_new_user(user_body):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
	                     json = user_body,
	                     headers = data.headers)


#   Getting an authToken for a user
def get_new_user_token():
	response = post_new_user(data.user_body)
	return response.json().get("authToken")


#   Creating a kit
def post_new_client_kit(kit_body):
	data.headers["Authorization"] += get_new_user_token()
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCTS_KIT_PATH,
	                     json = kit_body,
	                     headers = data.headers)