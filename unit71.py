raw_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "

cleaned = raw_feedback.strip().lower()
cleaned = cleaned.replace("speaker", "presenter")
cleaned = " ".join(cleaned.split())
final_feedback = cleaned.title()

print(f"Cleaned feedback: {final_feedback}")
