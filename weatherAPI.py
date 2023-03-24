import requests

print("Hello!")

while True:
    try:
        city = input("Which city's weather would you like to see?")

        api_key = "1212c1d211eb7875adfdacfdd449b8e8"

        url = (
            "https://api.openweathermap.org/data/2.5/weather?q=+"
            f"{city}" + "&appid=" + f"{api_key}"
        )

        res = requests.get(url)

        data = res.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wdesc = data["weather"][0]["description"]

        print("Temperature:", temp, "Humidity:", humidity, "Description:", wdesc)

    except:
        pass
    else:
        break
