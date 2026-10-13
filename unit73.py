try:
    with open("feedback.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("File not found. Please create feedback.txt first.")

except PermissionError:
    print("Permission denied. Close the file and try again.")

finally:
    print("Operation completed.")
