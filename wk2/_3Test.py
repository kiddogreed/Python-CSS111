# # Example 1
# import math
# # Define a function named print_cylinder_volume.
# def print_cylinder_volume():
#   """Compute and print the volume of a cylinder.
#   Parameters: none
#   Return: nothing
#   """
#   # Get the radius and height from the user.
#   radius = float(input("Enter the radius of a cylinder: "))
#   height = float(input("Enter the height of a cylinder: "))
#   # Compute the volume of the cylinder.
#   volume = math.pi * radius**2 * height
#   # Print the volume of the cylinder.
#   print(f"Volume: {volume:.2f}")



# # Example 2
# import math
# # Define a function named print_cylinder_volume.
# def print_cylinder_volume(radius, height):
#   """Compute and print the volume of a cylinder.
#   Parameters
#   radius: the radius of the cylinder
#   height: the height of the cylinder
#   Return: nothing
#   """
#   # Compute the volume of the cylinder.
#   volume = math.pi * radius**2 * height
#   # Print the volume of the cylinder.
#   print(volume)



# # Example 3
# import math
# # Define a function named computer_cylinder_volume.
# def compute_cylinder_volume(radius, height):
#   """Compute and return the volume of a cylinder.
#   Parameters
#   radius: the radius of the cylinder
#   height: the height of the cylinder
#   Return: the volume of the cylinder
#   """
#   # Compute the volume of the cylinder.
#   volume = math.pi * radius**2 * height
#   # Return the volume of the cylinder so that the
#   # volume can be used somewhere else in the program.
#   return volume



# # Example 4
# import math
# # Get the radius and height from the user.
# radius = float(input("Enter the radius of a cylinder: "))
# height = float(input("Enter the height of a cylinder: "))
# # Compute the volume of the cylinder.
# volume = math.pi * radius**2 * height
# # Print the volume of the cylinder.
# print(f"Volume: {volume:.2f}")


# # Example 5
# import math
# # Define a function named main.
# def main():
#   # Get the radius and height from the user.
#   radius = float(input("Enter the radius of a cylinder: "))
#   height = float(input("Enter the height of a cylinder: "))
#   # Compute the volume of the cylinder.
#   volume = math.pi * radius**2 * height
#   # Print the volume of the cylinder.
#   print(f"Volume: {volume:.2f}")
# # Start this program by
# # calling the main function.
# main()

# with open("wk2\cans.txt", "r") as file:
#     for line in file:
#         print(line.rstrip())


with open("wk2\cans.txt", "r") as file:
    names = []
    for line in file:
        words = line.split()
        if words:
            name = words[0] + words[1]
            names.append(name)

for i, name in enumerate(names, 1):
    print(f"{i}. {name}")