import requests

# Weatherstack API endpoint
api_key = "INSERT YOUR API KEY"
endpoint = "http://api.weatherstack.com/current"

# Specify the location you want to get the weather information for
location = input("Enter the name of the city: ").upper()

# Construct the API request URL
url = f"{endpoint}?access_key={api_key}&query={location}"

try:
    # Make the API request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and print relevant weather information
        temperature = data['current']['temperature']
        description = data['current']['weather_descriptions'][0]

        print(f"Temperature in {location}: {temperature}°C")
        print(f"Description: {description}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

except Exception as e:
    print(f"An error occurred: {e}")
