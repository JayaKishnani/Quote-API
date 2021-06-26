import argparse
import requests

#initialise the parser
parser = argparse.ArgumentParser()

# Initialize parser
parser.add_argument("-o", "--Output", help = "Show Output")

args = parser.parse_args()

if args.Output:
    print("The category is : % s" % args.Output)

#API 
# obtaining resource from the server using GET request

api_token = "GET http://quotes.rest/quote/search.json?category=" + args.Output 

headers = {'content-type': 'application/json',
	   'X-TheySaidSo-Api-Secret': format(api_token)}

# requesting responses to the URL
response = requests.get('https://quotes.rest/qod?category='+ args.Output) 

# storing responses in JSON format
quotes = response.json()