def printList(*languages):
    print("2nd lang in the list is :" + languages[2])


if __name__ == '__main__':
    # Handling arbitrary args
    printList("python", "java", "scala", "db2", "mysql")
