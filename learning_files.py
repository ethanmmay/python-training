import os


def check_for_file():
    if os.path.exists("demo_file.txt"):
        pass
    else:
        x = open("demo_file.txt", "wt")
        x.write("test words\nmore words")
        x.close()


def learning_files():
    a = open("demo_file.txt", "rt")
    print(a.read(3))
    print(a.readline())
    a.close()

    b = open("demo_file.txt", "at")
    b.write("\nfile has more content")
    b.write("\neven more content")
    b.close()

    c = open("demo_file.txt", "rt")
    print(c.read())
    c.close()

    d = open("demo_file.txt", "wt")
    d.write("\nOops! erased it all!\n")
    d.close()

    e = open("demo_file.txt", "rt")
    print(e.read())
    e.close()

    ask_to_restore()


def ask_to_restore():
    def restore_file():
        z = open("demo_file.txt", "wt")
        z.write("test words\nmore words")
        z.close()

    restore = input("Restore file? y/n: ")
    if restore == "y":
        restore_file()
    else:
        delete = input("Delete file? y/n: ")
        if delete == "y":
            os.remove("demo_file.txt")


def ask_to_start():
    start = input("Start program? y/n: ")
    if start == "y":
        check_for_file()
        learning_files()
        ask_to_start()
    else:
        print("Did not start program.")


ask_to_start()

# Finished "Python Tutorial" on w3schools.com/python
# Moved to "Machine Learning" on w3schools.com/python
