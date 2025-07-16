# Working with Date, Time, and Advanced String Manipulation

## Task 1

Create a function `get_days_from_today(date)` that calculates the number of days between a given date and the current date.

### Requirements:
- The function takes one parameter: `date` — a string representing a date in the format `'YYYY-MM-DD'` (for example, `'2020-10-09'`).
- The function returns an integer that indicates the number of days from the given date to the current date.  
  If the given date is later than the current date, the result should be negative.
- Only days should be considered in the calculation, ignoring time (hours, minutes, seconds).
- The function must use Python’s `datetime` module to work with dates.

---

### Recommendations for Implementation:
- Import the `datetime` module.
- Convert the date string in `'YYYY-MM-DD'` format into a `datetime` object.
- Get the current date using `datetime.today()`.
- Calculate the difference between the current date and the given date.
- Return the difference in days as an integer.

---

### Evaluation Criteria:
- **Correctness**: The function must accurately calculate the number of days between dates.
- **Exception handling**: The function should handle incorrect input formats properly.
- **Code readability**: The code should be clean and well documented.

---
