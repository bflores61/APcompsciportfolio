#Benjamin Flores
#password
#writes a program that continuously asks for a password until user types python

#functions

def main():
  while True:
        check = input("Enter the password: ")
        if check == "boi":
            print("access granted")
            break
        else:
            print("incorrect password")
            continue

#main
main()
