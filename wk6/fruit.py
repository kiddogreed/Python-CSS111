


def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")
#Add code to reverse and print fruit_list.
  fruit_list.reverse()
  print(f"reversed: {fruit_list}")
  #Add code to append "orange" to the end of fruit_list and print the list.
  fruit_list.append("orange")
  print(f"original: {fruit_list}")
  #Add code to find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
  where  = fruit_list.find("apple")
  print(where)

if __name__ == "__main__":
    main()