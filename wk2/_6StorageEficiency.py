#Author: JOHN RUSSELLE DOMINGO
"""The storage efficiency of a steel can is computed by dividing the volume of a can by its surface area.

storage_efficiency =
volume
surface_area"""

#volume = ((Math.pi)*(radius*radius))*(height)
#surface_area = (2*(Math.pi)) radius (radius + height)
#radius is the radius of the cylinder
#height is the height of the cylinder
#storage_efficiency =volume /surface_area

# import math
# def main():
    
#     radius = float(6.83)
#     height = float(10.16)
#     def compute_volume(radius,height):
#         volume = ((math.pi)*(radius*radius))*(height)
#         return volume
        
#     def compute_surface_area(radius,height):
#         surface_area = (2*(math.pi))*(radius*(radius + height))
#         return surface_area
        
#     def storage_efficiency(compute_volume,compute_surface_area):
#         return compute_volume/compute_surface_area
    
#     print(f"storage efficiency is {storage_efficiency:.2f}")
      
# main()


# import math

# def compute_volume(radius, height):
#     volume = ((math.pi)*(radius*radius))*(height)
#     return volume

# def compute_surface_area(radius, height):
#     surface_area = (2*(math.pi))*(radius*(radius + height))
#     return surface_area

# def storage_efficiency(volume, surface_area):
#     return volume / surface_area

# def main():
#     radius = float(6.83)
#     height = float(10.16)

#     volume = compute_volume(radius, height)
#     surface_area = compute_surface_area(radius, height)
#     storage_efficiency = storage_efficiency(volume, surface_area)

#     print(f"storage efficiency is {storage_efficiency:.2f}")

# if __name__ == "__main__":
#     main()

import math

def main():
    radius = 6.83  # You don't need to cast this to float since it's already a float
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
    print(f"Storage efficiency is {efficiency:.2f}")

# Call the main function
main()