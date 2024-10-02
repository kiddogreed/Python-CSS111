#Author John Russelle Domingo
#Date 2024-10-02

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
    
    
#Test print value to check if its as expected output based on example
################################################################################
print(water_column_height(0.0, 0.0))
print(water_column_height(0.0, 10.0))
print(water_column_height(25.0, 0.0))
print(water_column_height(48.3, 12.8))
print("\n")
################################################################################
print(pressure_gain_from_water_height(0.0))
print(pressure_gain_from_water_height(30.2))
print(pressure_gain_from_water_height(50.0))
print("\n")
################################################################################
print(pressure_loss_from_pipe(0.048692,0.00,0.018,1.75))
print(pressure_loss_from_pipe(0.048692,200.00,0.000,1.75))
print(pressure_loss_from_pipe(0.048692,200.00,0.018,1.75))
print(pressure_loss_from_pipe(0.048692,200.00,0.018,1.65))
print(pressure_loss_from_pipe(0.286870,1000.00,0.013,1.65))
print(pressure_loss_from_pipe(0.286870,1800.75,0.013,1.65))