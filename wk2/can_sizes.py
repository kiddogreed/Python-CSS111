#Author: JOHN RUSSELLE DOMINGO
"""The storage efficiency of a steel can is computed by dividing the volume of a can by its surface area.

storage_efficiency =
volume
surface_area"""

#volume = ((Math.pi)*(radius*radius))*(height)
#surface_area = (2*(Math.pi)) radius (radius + height)
#radius is the radius of the cylinder
#height is the height of the cylinder
import math

def main():
    name = "#1 Picnic"
    radius = 6.83
    height = 10.16

    # Function to compute the volume of a cylinder
    def compute_volume(radius, height):
        volume = (math.pi * radius ** 2) * height
        return volume
    # Function to compute the surface area of a cylinder
    def compute_surface_area(radius, height):
        surface_area = 2 * math.pi * radius * (radius + height)
        return surface_area
    # Function to calculate storage efficiency
    def storage_efficiency(volume, surface_area):
        return volume / surface_area
    # Calculate volume and surface area
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    # Calculate and print storage efficiency
    efficiency = storage_efficiency(volume, surface_area)
    print(f"{name} {efficiency:.2f}")
# Call the main function
main()