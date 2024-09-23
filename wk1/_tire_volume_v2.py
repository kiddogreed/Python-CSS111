#author: JOHN RUSSELLE DOMINGO
from math import pi
import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
    # Convert width to meters (1 mm = 0.001 meters)
    width_m = width / 1000
    # Convert diameter from inches to meters (1 inch = 0.0254 meters)
    diameter_m = diameter * 0.0254
    # Calculate the sidewall height (aspect ratio as a percentage of width)
    sidewall_height_m = (width * aspect_ratio / 100) / 1000
    # Calculate the outer diameter of the tire (rim + 2 sidewalls)
    outer_diameter_m = diameter_m + 2 * sidewall_height_m
    # Calculate the volume of the outer tire (as a cylinder)
    outer_volume_m3 = pi * (outer_diameter_m / 2)**2 * width_m
    # Calculate the volume of the inner empty space (rim only)
    inner_volume_m3 = pi * (diameter_m / 2)**2 * width_m
    # The actual volume is the difference between the outer and inner volumes
    tire_volume_m3 = outer_volume_m3 - inner_volume_m3
    # Convert cubic meters to liters (1 cubic meter = 1000 liters)
    volume_liters = tire_volume_m3 * 1000
    return volume_liters

while True:
    # Get user input for tire dimensions
    width = float(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    volume = calculate_tire_volume(width, aspect_ratio, diameter)
    print(f"The approximate volume is {volume:.2f} liters")

    # Get current date (without time)
    today = datetime.date.today()

    # Open file for appending
    with open("wk1/volumes.txt", "a") as file:  # Use "with" for automatic closing
        # Prepare data string
        data_string = f"{today}, {width}, {aspect_ratio}, {diameter}, {volume:.2f} \n"
        # Write data to file
        file.write(data_string)

    print(f"Tire volume: {volume:.2f} liters")
    print(f"Data saved to volumes.txt")

    # Ask user if they want to continue
    continue_program = input("Do you want to calculate the volume for another tire? (yes/no): ").strip().lower()
    if continue_program != 'yes':
        print("Program terminated.")
        break
