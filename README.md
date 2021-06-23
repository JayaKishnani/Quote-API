# Quote API

At They Said So® have a huge collection of quotes in their database. Using REST style quote API gives easy access to the data.

## Why REST API ?

REST (Representational State Transfer) API can be used over any protocol, generally HTTP for Web APIs.

Since data is not tied to methods and resources, REST has the ability to handle multiple types of calls, return different data formats and even change structurally with the correct implementation of hypermedia independently.

## Approach

*The API sends HTTP request using GET request to the URI.

*Then the API fetches  the content from a particular resource URI. Python returns a response object. This response object would be used to access certain features such as content, headers, etc. This is returned in JSON format.

*The response is collected using response.json() method in requests library. It returns Python dictionary.

### References

*[Reference 1](https://theysaidso.com/api/)

*[Reference 2](https://www.mulesoft.com/resources/api/what-is-rest-api-design)