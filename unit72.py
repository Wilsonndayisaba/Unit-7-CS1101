# Read and display existing feedback
print("Feedback before appending:")

with open("feedback.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Append a new feedback message
with open("feedback.txt", "a", encoding="utf-8") as file:
    file.write("\n- The presenter was great and answered questions.")

# Read and display all feedback again
print("Feedback after appending:")

with open("feedback.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
