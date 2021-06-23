import requests

# input data
name = input(" Enter the category " )

#API 
# obtaining resource from the server using GET request

api_token = "GET http://quotes.rest/quote/search.json?category=" + name 

headers = {'content-type': 'application/json',
	   'X-TheySaidSo-Api-Secret': format(api_token)}

# requesting responses to the URL
response = requests.get('https://quotes.rest/qod?category='+ name)

# storing responses in JSON format
quotes=response.json()

#print dictionary
print(quotes)

