filename = input("Input the Filename: ")
f_extns = filename.split(".")
extention=repr(f_extns[-1]).replace("'", "")
if str(extention) == "py":
    print("The extension of the file is: python")
elif extention == 'txt':
    print("The extension of the file is: text file")
elif extention == 'jpg':
    print("The extension of the file is: jpg image file")
else:
    print("sorry, we can't find "+ extention)

