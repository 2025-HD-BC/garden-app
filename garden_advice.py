"""
Garden Advice Application

This application provides gardening advice based on the season and plant type.
It offers seasonal recommendations and plant-specific tips to help gardening
enthusiasts care for their plants effectively.

Author: Garden App Team
Version: 2.0
"""


def get_seasonal_advice(season):
    """
    Get gardening advice based on the current season.
    
    Args:
        season (str): The current season (spring, summer, autumn/fall, winter)
        
    Returns:
        str: Seasonal gardening advice
    """
    season = season.lower().strip()
    
    seasonal_advice = {
        "spring": "Perfect time for planting and fertilizing. Start preparing your garden beds.",
        "summer": "Water your plants regularly and provide some shade during hot days.",
        "autumn": "Prepare your garden for winter and harvest your vegetables.",
        "fall": "Prepare your garden for winter and harvest your vegetables.",  # Alternative name for autumn
        "winter": "Protect your plants from frost with covers and reduce watering."
    }
    
    return seasonal_advice.get(season, f"No specific advice for '{season}'. Please enter spring, summer, autumn, or winter.")


def get_plant_type_advice(plant_type):
    """
    Get gardening advice based on the type of plant.
    
    Args:
        plant_type (str): The type of plant (flower, vegetable, etc.)
        
    Returns:
        str: Plant-specific gardening advice
    """
    plant_type = plant_type.lower().strip()
    
    # Dictionary mapping plant types to their advice
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms and deadhead spent flowers.",
        "flowers": "Use fertiliser to encourage blooms and deadhead spent flowers.",
        "vegetable": "Keep an eye out for pests and ensure adequate watering!",
        "vegetables": "Keep an eye out for pests and ensure adequate watering!",
        "veggie": "Keep an eye out for pests and ensure adequate watering!",
        "veggies": "Keep an eye out for pests and ensure adequate watering!"
    }
    
    return plant_advice.get(plant_type, f"No specific advice for '{plant_type}'. Try 'flower' or 'vegetable'.")


def get_user_input():
    """
    Collect user input for season and plant type.
    
    Returns:
        tuple: A tuple containing (season, plant_type)
    """
    print("Welcome to the Garden Advice App!")
    print("-" * 35)
    
    season = input("Enter the current season (spring/summer/autumn/winter): ")
    plant_type = input("Enter your plant type (flower/vegetable): ")
    
    return season, plant_type


def display_advice(seasonal_advice, plant_advice):
    """
    Display the combined gardening advice in a formatted way.
    
    Args:
        seasonal_advice (str): Advice based on season
        plant_advice (str): Advice based on plant type
    """
    print("\n" + "="*50)
    print("🌱 GARDEN ADVICE 🌱")
    print("="*50)
    print(f"Seasonal Advice: {seasonal_advice}")
    print(f"Plant Care Tip: {plant_advice}")
    print("="*50)
    print("Happy gardening! 🌸")


def main():
    """
    Main function that orchestrates the garden advice application flow.
    """
    try:
        # Get user input
        season, plant_type = get_user_input()
        
        # Generate advice based on inputs
        seasonal_advice = get_seasonal_advice(season)
        plant_advice = get_plant_type_advice(plant_type)
        
        # Display the combined advice
        display_advice(seasonal_advice, plant_advice)
        
    except KeyboardInterrupt:
        print("\n\nGoodbye! Happy gardening! 🌱")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try again.")


# Entry point of the application
if __name__ == "__main__":
    main()
