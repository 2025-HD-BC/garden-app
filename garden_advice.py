# Get user input for the season and plant type
print("Welcome to the Garden Advice App!")
print("-" * 35)

season = input("Enter the current season (spring/summer/autumn/winter): ").lower().strip()
plant_type = input("Enter your plant type (flower/vegetable): ").lower().strip()

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
if season in ["summer"]:
    advice += "Water your plants regularly and provide some shade.\n"
elif season in ["winter"]:
    advice += "Protect your plants from frost with covers.\n"
elif season in ["spring"]:
    advice += "Perfect time for planting and fertilizing.\n"
elif season in ["autumn", "fall"]:
    advice += "Prepare your garden for winter and harvest vegetables.\n"
else:
    advice += f"No specific advice for '{season}'. Please enter spring, summer, autumn, or winter.\n"

# Determine advice based on the plant type
if plant_type in ["flower", "flowers"]:
    advice += "Use fertiliser to encourage blooms."
elif plant_type in ["vegetable", "vegetables", "veggie", "veggies"]:
    advice += "Keep an eye out for pests!"
else:
    advice += f"No specific advice for '{plant_type}'. Please enter 'flower' or 'vegetable'."

# Print the generated advice
print("\n" + "="*40)
print("GARDEN ADVICE")
print("="*40)
print(advice)
print("="*40)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
