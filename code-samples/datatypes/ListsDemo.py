

if __name__ == '__main__':

    # Declare list
    programmingLangs = ["Python", "Java", "Scala", "Go-Lang", "Ruby"]
    print(programmingLangs)

    # Length of list
    print(f"Length of List : {len(programmingLangs)}")

    # Accessing list element
    print(f"Element at 0th index : {programmingLangs[0]}")
    print(f"Element at 1st index : {programmingLangs[1]}")
    print(f"Element at 2nd index : {programmingLangs[2]}")

    # Return specific elements from list
    print(programmingLangs[2:5])  # Return the third, fourth, and fifth item

    # Append values to list
    programmingLangs.append('Spark')
    print(f"After append operation : {programmingLangs}")

    # Insert list iterm at particular position
    programmingLangs.insert(1, "Hadoop")
    print(f"After insert operation : {programmingLangs}")

    # Sort list, by default alphanumerically, ascending
    programmingLangs.sort()
    print(f"After sorting : {programmingLangs}")

    # Copy list
    newList = programmingLangs.copy()
    print(f"New list after copy : {newList}")

    # Remove element from list
    programmingLangs.remove("Go-Lang")
    print(f"After remove operation : {programmingLangs}")

    programmingLangs.pop(1)   # Remove 2nd element
    programmingLangs.pop()    # Remove last element
    del programmingLangs[2]   # del keyword removes the specified index
    print(f"After delete operation : {programmingLangs}")

    programmingLangs.clear()  # clear() method empties the list
    print(f"After clear operation : {programmingLangs}")

    del programmingLangs      # Delete the entire list, list is no more accessible






