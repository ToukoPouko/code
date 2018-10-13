import requests
import ast
from pprint import pprint

response = requests.get("https://montanaflynn-text-to-speech.p.mashape.com/speak?text=This+is+a+test!")
data = response.json()

print(data)