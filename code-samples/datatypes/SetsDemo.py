if __name__ == '__main__':
    programmingLangsSet = {"Python", "Java", "Scala", "Go-Lang", "Ruby","Scala", "Go-Lang", True, 1}
    sqlLangs = {"Oracle", "db2", "bigquery"}
    print(f"Programming Language Set :: {programmingLangsSet}")
    print(f"SQL Language Set :: {sqlLangs}")

    # Check if element is available in set
    print("Python" in programmingLangsSet)

    # Add an item to a set
    sqlLangs.add("MySQL")
    print(f"Printing SQL Set after addition :: {sqlLangs}")

    # Adding elements from 1 set to another
    programmingLangsSet.update(sqlLangs)
    print(f"Programming Language Set after update() :: {programmingLangsSet}")

    # append another datastructure to set
    frameworks = ["HDFS", "GFS"]
    programmingLangsSet.update(frameworks)
    print(f"Programming Language Set after 2nd update() :: {programmingLangsSet}")

    # Remove set elements
    sqlLangs.remove("db2")
    print(f"Printing SQL Set after element removal :: {sqlLangs}")

    # Discard set elements
    sqlLangs.discard("sqllite")
    print(f"Printing SQL Set after element discard :: {sqlLangs}")

    # Empty the set
    frameworks.clear()
    print(f"Printing framework Set after clear() :: {frameworks}")

    # delete set
    del sqlLangs





