# Quote API

At They Said So® have a huge collection of quotes in their database. Using REST style quote API gives easy access to the data.

## CLI

A computer program where user interact with  lines of text commands. It interacts with command line script.

#### Advantages of using CLI

1. light weight, no- user interface library involved
2. Uses less RAM, CPU, GPU

## Building CLI using Python

Using **argparse** python module.

1. Import the Python argparse library
2. Create the parser
3. Add optional and positional arguments to the parser
4. Execute .parse_args()

## Why REST API ?

REST (Representational State Transfer) API can be used over any protocol, generally HTTP for Web APIs.

Since data is not tied to methods and resources, REST has the ability to handle multiple types of calls, return different data formats and even change structurally with the correct implementation of hypermedia independently.

## Approach

1. The API sends HTTP request using GET request to the URI.
2. Then the API fetches  the content from a particular resource URI. Python returns a response object. This response object would be used to access certain features such as content, headers, etc. This is returned in JSON format.
3. The response is collected using response.json() method in  requests library. It returns Python dictionary.

### References

1. [Reference 1](https://theysaidso.com/api/)
2. [Reference 2](https://www.mulesoft.com/resources/api/what-is-rest-api-design)
3. [Reference 3](https://www.geeksforgeeks.org/command-line-option-and-argument-parsing-using-argparse-in-python/)
4. [Reference 4](https://docs.python.org/3/howto/argparse.html#id1)