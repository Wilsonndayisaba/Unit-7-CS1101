try:
    with open("feedback.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Skip the title on the first line
    feedback_lines = lines[1:]

    total_feedback = len(feedback_lines)

    great_count = sum(
        1 for line in feedback_lines
        if "great" in line.lower()
    )

    summary = (
        "=== Workshop Feedback Summary ===\n"
        f"Total Feedback: {total_feedback}\n"
        f"Mentions of 'Great': {great_count}\n"
    )

    with open("summary.txt", "w", encoding="utf-8") as file:
        file.write(summary)

    print(summary, end="")

except FileNotFoundError:
    print("File not found. Please create feedback.txt first.")

except PermissionError:
    print("Permission denied. Close the file and try again.")

finally:
    print("Operation completed.")
