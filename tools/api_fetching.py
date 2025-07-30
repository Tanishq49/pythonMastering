import requests

#Giving the request to the URL
request = requests.get("https://api.currencyapi.com/v3/latest?apikey=cur_live_r24zapM5aF3EDPEGQE1XlOjdhMGE1bjsVZzhs2Db")
status_code = request.status_code

if status_code == 200:
    data = request.json()
    currency = input("Enter your currency name:")
    if 'data' in data and currency in data['data']:
        rate = data['data'][currency]['value']
        print("Result:",rate)
    else:
        print("Not found")
else:
    print("Cant connect to the server")