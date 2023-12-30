# Weather Information App

This simple Python script utilizes the Weatherstack API to provide you with current weather information for a specified city. Follow the steps below to get started:

## Prerequisites

Make sure you have the following prerequisites installed on your system:

- Python 3.x
- Requests library (`pip install requests`)

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/thevoidop/weatherapp.git
   cd weatherapp
   ```
2. **Get API Key:**
  - Obtain your Weatherstack API key by signing up at Weatherstack.

3. **Configure API Key:**
  - Open the script in a text editor of your choice.
  - Replace the api_key variable value with your Weatherstack API key.

4. **Run the Script:**
  - Open a terminal and navigate to the project directory.
  - Run the script using the following command:
      ```bash
      python weatherapp.py
      ```
  - Enter the name of the city when prompted.
      ```bash
      Enter the name of the city: PARIS
      Temperature in PARIS: 25°C
      Description: Partly cloudy
      ```
## Error Handling

If an error occurs during the API request, an error message will be displayed.
## Notes

- The temperature is provided in degrees Celsius.
- Make sure to respect the usage limits of your Weatherstack API key.
- Feel free to customize and enhance the script according to your preferences! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.
