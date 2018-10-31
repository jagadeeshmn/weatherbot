from apixu.client import ApixuClient

api_key = '8cf4dc262c664ae59b0223043183010'

client = ApixuClient(api_key)
current = client.getCurrentWeather(q='in atlanta')
print(current['current']['condition']['text'])