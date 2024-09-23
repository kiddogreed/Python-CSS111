package java.wk1;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.util.Scanner;

/**
 * Main
 */

public class Main {

    public class TireVolumeCalculator {
        public static double calculateTireVolume(double width, int aspectRatio, int diameter) {
            // Convert width to meters (1 mm = 0.001 meters)
            double width_m = width / 1000;
            // Convert diameter from inches to meters (1 inch = 0.0254 meters)
            double diameter_m = diameter * 0.0254;
            // Calculate the sidewall height (aspect ratio as a percentage of width)
            double sidewallHeight_m = (width * aspectRatio / 100) / 1000;
            // Calculate the outer diameter of the tire (rim + 2 sidewalls)
            double outerDiameter_m = diameter_m + 2 * sidewallHeight_m;
            // Calculate the volume of the outer tire (as a cylinder)
            double outerVolume_m3 = Math.PI * Math.pow(outerDiameter_m / 2, 2) * width_m;
            // Calculate the volume of the inner empty space (rim only)
            double innerVolume_m3 = Math.PI * Math.pow(diameter_m / 2, 2) * width_m;
            // The actual volume is the difference between the outer and inner volumes
            double tireVolume_m3 = outerVolume_m3 - innerVolume_m3;
            // Convert cubic meters to liters (1 cubic meter = 1000 liters)
            double volumeLiters = tireVolume_m3 * 1000;
            return volumeLiters;
        }

        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
  
          while (true) {
              // Get user input for tire dimensions
              System.out.print("Enter the width of the tire in mm (ex 205): ");
              double width = scanner.nextDouble();
  
              System.out.print("Enter the aspect ratio of the tire (ex 60): ");
              int aspectRatio = scanner.nextInt();
  
              System.out.print("Enter the diameter of the wheel in inches (ex 15): ");
              int diameter = scanner.nextInt();
  
              double volume = calculateTireVolume(width, aspectRatio, diameter);
              System.out.printf("The approximate volume is %.2f liters%n", volume);
  
              // Get current date (without time)
              LocalDate today = LocalDate.now();
  
              // Write data to file
              try (FileWriter fileWriter = new FileWriter("volumes.txt", true)) {
                  String dataString = String.format("%s, %.2f, %d, %d, %.2f %n", 
                                                    today, width, aspectRatio, diameter, volume);
                  fileWriter.write(dataString);
                  System.out.println("Tire volume: " + volume + " liters");
                  System.out.println("Data saved to volumes.txt");
              } catch (IOException e) {
                  System.out.println("An error occurred while writing to the file.");
                  e.printStackTrace();
              }
  
              // Ask user if they want to continue
              System.out.print("Do you want to calculate the volume for another tire? (yes/no): ");
              scanner.nextLine();  // Consume the newline
              String continueProgram = scanner.nextLine().trim().toLowerCase();
              if (!continueProgram.equals("yes")) {
                  System.out.println("Program terminated.");
                  break;
              }
          }
  
          scanner.close();
      }
    }

    
}
    
