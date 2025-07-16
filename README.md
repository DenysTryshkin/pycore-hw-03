# Working with Date, Time, and Advanced String Manipulation

Task 1: get_days_from_today(date)

📝 Description:
Create a function get_days_from_today(date) that calculates the number of days between a given date and the current date.

✅ Requirements:
The function takes one parameter:
date — a string representing a date in the 'YYYY-MM-DD' format (e.g., '2020-10-09').
It returns an integer indicating the number of days from the given date to today:
If the given date is in the future, the result should be negative.
The calculation should consider only full days, ignoring time (hours, minutes, seconds).
Use Python’s built-in datetime module to handle date operations.
🛠️ Implementation Hints:
Import the datetime module.
Convert the input string into a datetime object using datetime.strptime().
Get the current date using datetime.today().
Subtract the given date from today’s date.
Return the difference in days as an integer using .days.
🧪 Evaluation Criteria:
Correctness: The function must accurately compute the number of days between dates.
Exception Handling: The function should properly handle incorrect input formats (e.g., raise a ValueError).
Code Quality: The code must be clean, readable, and well-documented.