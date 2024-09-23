
#author: JOHN RUSSELLE DOMINGO
#--TODO-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#INPUTS 
# w = float(input("Enter the width of the tire in mm (ex 205):"))
# a = int(input("Enter the aspect ratio of the tire (ex 60):"))
# d = int(input("Enter the diameter of the wheel in inches (ex 15)::"))

#FORMULA
# volume = (pi)(w*w)(a)((w*a) + (2540*d))/10_000_000   

#IMPORT PI
from math import pi
#import Date
import datetime

#USING FUNCTION
def calculate_tire_volume(width, aspect_ratio, diameter):
    #Calculates the approximate volume of a tire in liters.

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

# Get user input
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = calculate_tire_volume(width, aspect_ratio, diameter)
print(f"The approximate volume is {volume:.2f} liters")


#GUIDE
    # # Convert units to meters
    # width= width_mm / 1000
    # diameter = diameter_in * 0.0254

    # # Calculate sidewall height and outer diameter
    # sidewall_height_m = (width_mm * aspect_ratio / 100) / 1000
    # outer_diameter_m = diameter_m + 2 * sidewall_height_m

    # # Calculate volumes
    # outer_volume_m3 = pi * (outer_diameter_m / 2)**2 * width_m
    # inner_volume_m3 = pi * (diameter_m / 2)**2 * width_m
    # tire_volume_m3 = outer_volume_m3 - inner_volume_m3

    # # Convert to liters
    # volume_liters = tire_volume_m3 * 1000
    
#----------------------------------------------------------------------------    
 #additional   
#Gets the current date from the computer’s operating system. 
today = datetime.date.today()

print(today)
#print(testDate)