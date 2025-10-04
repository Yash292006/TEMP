# Program to display temperature alert based on input value

# Take temperature input
temp = float(input("Enter the temperature (in °C): "))

# Check temperature range and display message
if temp < 0:
    print("Alert: Freezing temperature! Stay warm ")
elif 0 <= temp < 20:
    print("Weather is Cold. Wear a jacket ")
elif 20 <= temp < 30:
    print("Weather is Normal. Enjoy your day ")
elif 30 <= temp < 40:
    print("Alert: It's Hot! Stay hydrated ")
else:
    print("Alert: Extreme Heat! Avoid going outside ")