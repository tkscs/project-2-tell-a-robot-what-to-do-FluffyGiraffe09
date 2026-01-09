current_state="black"

while current_state != "in drawer":

    if current_state == "black":
        print("light is off")
    elif current_state == "white":
        print("white light is on")
    elif current_state == "red":
        print("red light is on")
    elif current_state == "in_drawer":
        print("the flashlight is in the drawer")
    current_input = input("You can click press (c), hold press (h), do nothing (n), or put it away (a)")

    if current_state == "black":
        if current_input == "c":
            current_state="white"
        elif current_input == "h":
            current_state="red"
        elif current_input == "n":
            current_state="black"
        elif current_input == "a":
            current_state="in_drawer"
        else:
            print("ERROR")

    elif current_state == "white":
        if current_input == "c":
            current_state="black"
        elif current_input == "h":
            current_state="red"
        elif current_input == "n":
            current_state="white"
        elif current_input == "a":
            current_state="in_drawer"
        else:
            print("ERROR")
    elif current_state == "red":
        if current_input == "c":
            current_state="black"
        elif current_input == "h":
            current_state="white"
        elif current_input == "n":
            current_state="red"
        elif current_input == "a":
            current_state="in_drawer"
        else:
            print("ERROR")
    elif current_state == "in_drawer":
        break
    else:
        print ("ERROR!!!!!")