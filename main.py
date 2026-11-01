import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import PyQt5

df = pd.DataFrame()
# print(df)

index_ = 1


def tasks():
    print("Add a new row: Press A")
    print("Update a row: Press U")
    print("Delete a row: Press D")
    print("Show DataFrame: Press S")
    print("Export as a csv file: Press E")
    print("Exit: Press Q")

def update_tasks():
    print("Press N to update Name: ")
    print("Press A to update Age: ")
    print("Press C to update Country: ")
    print("Press T to update City: ")
    print("Press U to update University: ")
    print("Press Q to Exit update menu: ")


while True:
    tasks()
    user_input_select = input("Please Enter here: ").lower()
    match user_input_select:
        case "a":
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
            }], index=[index_])
            df = pd.concat([df, new_row])
            print(f"\n{name} added successfully!\n")
            index_ += 1



        case "u":
            if df.empty:
                print("\nEnter something first!\n")
            else:
                while True:
                    entered_index = int(input("Enter the index: "))
                    if entered_index not in df.index:
                        print("Invalid Index!")
                        continue
                    else:
                        filtered_index = df.loc[entered_index]
                        while True:
                            update_tasks()
                            user_input_update = input("Please Enter here: ").lower()
                            match user_input_update:
                                case "n":
                                    updated_name = input("Enter the new name: ").capitalize()
                                    df.loc[entered_index, "Name"] = updated_name
                                case "a":
                                    updated_age = int(input("Enter the new age: "))
                                    df.loc[entered_index, "Age"] = updated_age
                                case "c":
                                    updated_country = input("Enter the new country: ").capitalize()
                                    df.loc[entered_index, "Country"] = updated_country
                                case "t":
                                    updated_city = input("Enter the new city: ").capitalize()
                                    df.loc[entered_index, "City"] = updated_city
                                case "u":
                                    updated_uni = input("Enter the new university: ").capitalize()
                                    df.loc[entered_index, "University"] = updated_uni
                                case "q":
                                    # print("Exiting")
                                    break
                                case _:
                                    print("\nInvalid Input!\n")
                        break

        case "d":
            pass
        case "s":
            if df.empty:
                print("\nEnter something first!\n")
            else:
                print(df)
        case "e":
            pass
        case "q":
            print("Exiting...")
            break
        case _:
            print("\nInvalid Input!\n")
