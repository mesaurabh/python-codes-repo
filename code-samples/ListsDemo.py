

if __name__ == '__main__':

    # Declare list
    programmingLangs = ["Python", "Java", "Scala", "Go", "Ruby"]
    print(programmingLangs)

    # Length of list
    print(len(programmingLangs))

    # Accessing list element
    print(programmingLangs[0])
    print(programmingLangs[1])
    print(programmingLangs[2])

    # Return specific elements from list
    print(programmingLangs[2:5]) # Return the third, fourth, and fifth item

    # Append values to list
    programmingLangs.append('Spark')
    print(programmingLangs)

    # Insert list iterm at particular position
    programmingLangs.insert(1, "Hadoop")
    print(programmingLangs)

    # Remove element from list
    programmingLangs.remove("Go-Lang")
    print(programmingLangs)

    programmingLangs.pop(1)   # Remove 2nd element
    programmingLangs.pop()    # Remove last element
    del programmingLangs[2]   # del keyword removes the specified index
    print(programmingLangs)

    programmingLangs.clear()  # clear() method empties the list
    print(programmingLangs)

    del programmingLangs      # Delete the entire list, list is no more accessible






