import json

import requests
import pandas as pd

test_input = {'text':'Macaroni and Cheese macaroni, cheese, small red onion diced ounce package small past','mode':'free_text','no_of_recipes':3}

response = requests.post('https://foodrecommendation.azurewebsites.net/', json=test_input)
#response = requests.post('http://127.0.0.1:5000/get-recipe', json=test_input)

print(response.json())

# convert server response into dataframe
data1 = json.loads(response.json())

df = pd.DataFrame(data1)

df.head()