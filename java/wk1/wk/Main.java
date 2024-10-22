/**
 * Main
 */

 import java.util.ArrayList;
import java.util.List;


public class Main {
    public static void main(String[] args) {
          // Create a list with more than 100 items
          List<Integer> itemList = new ArrayList<>();
        
          // Add 150 items to the list as an example
          for (int i = 1; i <= 150; i++) {
              itemList.add(i);
          }
          
          // Display the first 100 items
          int limit = 100;
          int iterations = 0;
  
          for (int i = 0; i < itemList.size() && iterations < 2; i++) {
              if (i < limit) {
                  System.out.println("Item: " + itemList.get(i));
              }
              if (i == limit - 1) {
                  iterations++;
              }
            }
    }
    
}