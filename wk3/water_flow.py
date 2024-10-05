#Author John Russelle Domingo
#Date 2024-10-02
#updated 2024-10-05

from math import pow
def water_column_height(tower_height, tank_height):
    """calculates and returns the height of a column of water from a tower height and a tank wall height"""
    # h = t + (3/4) * w
    return tower_height + (3/4) * tank_height

def pressure_gain_from_water_height(height):
    """calculates and returns the pressure caused by Earth’s gravity pulling on the water stored in an elevated tank. """
     # Constants
    density = 998.2  # Density of water in kg/m^3
    g = 9.80665  # Gravitational acceleration in m/s^2
    return (density * g * height) / 1000
      # Pressure gain formula:
    # Pressure is the force per unit area, which is calculated by the formula:
    # pressure = (density of water * gravitational force * height of water column)
    # Dividing by 1000 to convert from Pascals to kilopascals (1 kPa = 1000 Pa)

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculates and returns the pressure loss due to friction within a pipe.
    Parameters:
    pipe_diameter (float): The diameter of the pipe in meters.
    pipe_length (float): The length of the pipe in meters.
    friction_factor (float): The friction factor of the pipe.
    fluid_velocity (float): The velocity of the water in meters per second.
    """
    density_of_water = 998.2  # kg/m^3, density of water
    # Pressure loss formula (in kilopascals)
    return - (friction_factor * pipe_length * density_of_water * fluid_velocity**2) / (2000 * pipe_diameter)    

#updated task
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
        # Constants
    density_water = 998.2  # kg/m^3
    constant = -0.04 / 2000  # Constant part of the equation
    # Calculate pressure loss
    #P = −0.04 ρ v2/n2000 
    # Return the pressure loss in kilopascals (kPa)
    return constant * density_water * (fluid_velocity ** 2) * quantity_fittings

def reynolds_number(hydraulic_diameter, fluid_velocity):
       # Constants
    density_water = 998.2  # kg/m^3
    dynamic_viscosity = 0.0010016  # Pa·s (Pascal seconds)
    # Calculate Reynolds number
    #R = ρdv/μ
    return (density_water * hydraulic_diameter * fluid_velocity) / dynamic_viscosity     
    
def pressure_loss_from_pipe_reduction(larger_diameter,
    fluid_velocity, reynolds_number, smaller_diameter):
    #  # Constants
    density_water = 998.2  # kg/m^3
    # # Formula to calculate 'k' (constant)
    # k = 0.1 + (50 / reynolds_number) * (pow((larger_diameter / smaller_diameter), 4) - 1)
    # # Formula to calculate pressure loss 'P' (in kPa)
    # pressure_loss = -k * density_water * pow(fluid_velocity, 2) / 2000
    # # print(f"k: {k}")  # Debugging line
    # # print(f"Pressure Loss: {pressure_loss}")  # Debugging line
        # Formula to calculate 'k' (constant)
    # Prevent division by zero and check for valid inputs
      # Constants
    density_water = 998.2  # kg/m^3
    #always check for () positions to avoid unexpected values
    # Formula to calculate 'k' (constant)
    k = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    
    # Formula to calculate pressure loss 'P' (in kPa)
    return  (-k * density_water * (fluid_velocity ** 2))/ 2000




#Test print value to check if its as expected output based on example
# ################################################################################
# print(water_column_height(0.0, 0.0))
# print(water_column_height(0.0, 10.0))
# print(water_column_height(25.0, 0.0))
# print(water_column_height(48.3, 12.8))
# print("\n")
# ################################################################################
# print(pressure_gain_from_water_height(0.0))
# print(pressure_gain_from_water_height(30.2))
# print(pressure_gain_from_water_height(50.0))
# print("\n")
# ################################################################################
# print(pressure_loss_from_pipe(0.048692,0.00,0.018,1.75))
# print(pressure_loss_from_pipe(0.048692,200.00,0.000,1.75))
# print(pressure_loss_from_pipe(0.048692,200.00,0.018,1.75))
# print(pressure_loss_from_pipe(0.048692,200.00,0.018,1.65))
# print(pressure_loss_from_pipe(0.286870,1000.00,0.013,1.65))
# print(pressure_loss_from_pipe(0.286870,1800.75,0.013,1.65))

# #Test task
# ################################################################################
# print("\n")
# print(pressure_loss_from_fittings(0.00,3))
# print(pressure_loss_from_fittings(1.65,0))
# print(pressure_loss_from_fittings(1.65,2))
# print(pressure_loss_from_fittings(1.75,2))
# print(pressure_loss_from_fittings(1.75,5))

# ################################################################################
# print("\n")
# print(reynolds_number(0.048692,0.00))
# print(reynolds_number(0.048692,1.65))
# print(reynolds_number(0.048692,1.75))
# print(reynolds_number(0.286870,1.65))
# print(reynolds_number(0.286870,1.75))

# ################################################################################
# print("\n")
# print(pressure_loss_from_pipe_reduction(0.28687,0.00,1,0.048692))
# print(pressure_loss_from_pipe_reduction(0.28687,1.65,471729,0.048692))
# print(pressure_loss_from_pipe_reduction(0.28687,1.75,500318,0.048692))

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
if __name__ == "__main__":
    main()
