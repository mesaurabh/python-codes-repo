if __name__ == '__main__':
    capitals = {"USA": "Washington D.C.", "France": "Paris", "India": "New Delhi"}

    d = {}  # empty dictionary

    numNames = {1: "One", 2: "Two", 3: "Three"}  # int key, string value

    decNames = {1.5: "One and Half", 2.5: "Two and Half", 3.5: "Three and Half"}  # float key, string value

    items = {("Parker", "Reynolds", "Camlin"): "pen",
             ("LG", "Whirlpool", "Samsung"): "Refrigerator"}  # tuple key, string value

    romanNums = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}  # string key, int value

    dict_obj = {"Fruit": ["Mango", "Banana"], "Color": ["Blue", "Red"]} # List as value

    # Access Dictionary
    print(capitals["USA"])
    print(capitals.get("USA"))

    capitals['Canada'] = 'Ottawa'
    print(capitals)

    del capitals['Canada']
    print(capitals)

    print(capitals.keys())
    print(capitals.values())

    # Multi-dimensional Dictionary
    person1 = {"name": "Steve", "age": 30}
    person2 = {"name": "Ana", "age": 27}

    employee = {1:person1, 2:person2}
    print(employee)

    print(employee[1].get('name'))




