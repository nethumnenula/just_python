import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import PyQt5

data = {
    "Name": "Nethum",
    "Age": 22,
    "Country": "Sri Lanka",
    "City": "Colombo",
    "University": "USJ"
}
df = pd.DataFrame(data, index=[1])
print(df)

index_ = 1

while True:
    user_input_add = input("To ADD a new row, \nPress A to Continue: \nPress E to Exit: ").lower()
    if user_input_add == "a":
        name = input("Enter a Name: ").capitalize()
        age = int(input(f"Enter {name}'s Age: "))
        country = input(f"Enter {name}'s Country: ").capitalize()
        city = input(f"Enter {name}'s City: ").capitalize()
        uni = input(f"Enter {name}'s University: ").capitalize()
        new_row = pd.DataFrame([{
            "Name": name,
            "Age": age,
            "Country": country,
            "City": city,
            "University": uni
        }], index=[index_ + 1])
        df = pd.concat([df, new_row])
        index_ += 1
        print(df)
    elif user_input_add == "e":
        print("Exiting...")
        break
    else:
        print("Enter a valid input!")
