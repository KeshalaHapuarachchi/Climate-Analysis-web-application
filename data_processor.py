def process_data(data):
    if data["cod"] != "404":
        main = data["main"]
        wind = data["wind"]
        weather = data["weather"]

        processed_data = {
            "temperature": main["temp"],
            "pressure": main["pressure"],
            "humidity": main["humidity"],
            "wind_speed": wind["speed"],
            "description": weather[0]["description"],
        }
        return processed_data
    else:
        return None
