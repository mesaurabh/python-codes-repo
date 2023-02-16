import array as arr

if __name__ == '__main__':

    # Declare array with integer elements
    intArray = arr.array('i', [34, 22, 63])

    # Declare array with double type
    dblArray = arr.array('d', [34.55, 22.33, 63.34])

    # Printing array elements by position
    print(f"Element at 0th position : {dblArray[0]}")
    print(f"Element at 1st position : {dblArray[1]}")
    print(f"Element at 2nd position : {dblArray[2]}")

    # Insert element to array

    dblArray.insert(1, 3.14)

    # Element after insertion
    print(f"Element after insertion at 1st position : {dblArray[1]}")

    # Remove element from array
    dblArray.remove(22.33)
    print(dblArray)




