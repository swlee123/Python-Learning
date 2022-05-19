try:
    file = open("text.txt")
    a_dic = {"key":"value"}
    print(a_dic["key"])
except FileNotFoundError:
    file = open("text.txt", "w")
    file.write("something")
except KeyError as error_message:
    print("The key does not exist")
    print(f"the key {error_message} does not exist!")

else:
    content = file.read()
    print(content)

finally:
    # no matter wht happen
    file.close()
    print("File was closed")
    raise TypeError("This is the error i made up")
    # make your own errors


