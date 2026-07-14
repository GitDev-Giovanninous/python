
"""TO DO LIST:
- Add activity
- View all activities
- Delete activity
- Modify activity
- """

import json
import datetime as dt

DATE_FORMAT = "%m/%d/%Y"
TIME_FORMAT = "%H:%M"
FILE_NAME = "activities.json"

to_do_list = []

def menu_choice():
    while True:
        try:

            menu_choice_ = int(input("\nPlease enter your choice: "))

            if 1 <= menu_choice_ <= 6:
                return menu_choice_

            print("Please enter a valid choice")

        except ValueError:
            print("Please enter a valid choice")

def title_already_exists(title, current_activity=None):
    for activity in to_do_list:
        if activity != current_activity and activity["title"].lower() == title.lower():
            return True
    return False

def has_activities():
    if not to_do_list:
        print("No activities.")
        return False
    return True

def save_activities():
    activities = []

    for activity in to_do_list:
        activity_copy = activity.copy()
        activity_copy["date"] = activity["date"].strftime(DATE_FORMAT)
        activity_copy["time"] = activity["time"].strftime(TIME_FORMAT)
        activities.append(activity_copy)

    with open(FILE_NAME, "w") as file:
        json.dump(activities, file, indent=4)

def load_activities():
    global to_do_list

    try:
        with open(FILE_NAME, "r") as file:
            activities = json.load(file)

            for activity in activities:
                activity["date"] = dt.datetime.strptime(
                    activity["date"],
                    DATE_FORMAT
                ).date()

                activity["time"] = dt.datetime.strptime(
                    activity["time"],
                    TIME_FORMAT
                ).time()

                activity.setdefault("completed", False)

            to_do_list = activities

    except (FileNotFoundError, json.JSONDecodeError):
        to_do_list = []

def add_activity():
    while True:
        title = input("title of the activity: ")

        if title_already_exists(title):
            print("An activity with this title already exists.")
        else:
            break

    description = input("description: ")

    while True:

        try:
            date = input("date of activity (MM/DD/YYYY): ")
            date = dt.datetime.strptime(date, DATE_FORMAT).date()
            break

        except ValueError:
            print("Please enter a valid date")

    while True:

        try:
            time = input("time of activity (HH:MM): ")
            time = dt.datetime.strptime(time, TIME_FORMAT).time()
            break

        except ValueError:
            print("Please enter a valid time")

    activity = {
        "title": title,
        "description": description,
        "date": date,
        "time": time,
        "completed": False,
    }

    to_do_list.append(activity)
    save_activities()
    print("activity added")

def view_all_activities():
    if not has_activities():
        return

    print("\nHere are your activities:")

    for i, activity in enumerate(to_do_list, start=1):
        print(f"\nActivity {i}")
        print(f"Title: {activity['title']}")
        print(f"Description: {activity['description']}")
        print(f"Date: {activity['date']}")
        print(f"Time: {activity['time']}")
        status = "Completed" if activity["completed"] else "Not completed"
        print(f"Status: {status}")

def delete_activity():
    if not has_activities():
        return

    view_all_activities()

    activity_to_delete = input("\nWrite the name of the activity to delete: ")

    for activity in to_do_list:
        if activity["title"].lower() == activity_to_delete.lower():
            to_do_list.remove(activity)
            save_activities()
            print("Activity deleted.")
            return

    print("Please enter a valid activity.")

def modify_activity():
    if not has_activities():
        return

    view_all_activities()
    activity_to_modify = input("\nWrite the name of the activity to modify: ")
    for activity in to_do_list:
        if activity["title"].lower() == activity_to_modify.lower():

            print("\nLeave blank if you don't want to change the value.")

            new_title = input("New title: ")
            new_description = input("New description: ")

            if new_title:
                if title_already_exists(new_title, activity):
                    print("An activity with this title already exists.")
                    return
                activity["title"] = new_title

            if new_description:
                activity["description"] = new_description

            save_activities()
            print("Activity modified.")
            return

    print("Please enter a valid activity.")

def complete_activity():
    if not has_activities():
        return

    view_all_activities()
    activity_to_complete = input("\nWrite the name of the activity to complete: ")
    for activity in to_do_list:
        if activity["title"].lower() == activity_to_complete.lower():
            activity["completed"] = True
            print("Activity completed.")
            save_activities()
            return

    print("Please enter a valid activity.")

def main():

    load_activities()

    while True:
        print("""\nWelcome to your to-do list! What do you want to do today? 
1. Add an activity
2. View all activities
3. Delete an activity
4. Modify an activity
5. Complete an activity
6. Exit""")

        choice = menu_choice()

        if choice == 1:
            add_activity()
        elif choice == 2:
            view_all_activities()
        elif choice == 3:
            delete_activity()
        elif choice == 4:
            modify_activity()
        elif choice == 5:
            complete_activity()
        elif choice == 6:
            print("Thank you for your time!")
            break


if __name__ == "__main__":
    main()