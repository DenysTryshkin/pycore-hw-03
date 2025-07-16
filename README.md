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

## Task 2

To win the grand prize in a lottery, you need to match several numbers on your ticket with randomly drawn numbers within a certain range during the drawing. For example, you might need to guess six numbers from 1 to 49, or five numbers from 1 to 36, etc.

You need to write a function `get_numbers_ticket(min, max, quantity)` that helps generate a set of unique random numbers for such lotteries. The function should return a random set of numbers within the specified parameters, ensuring all numbers in the set are unique.

### Requirements:
- Function parameters:
  - `min` — the minimum possible number in the set (at least 1).
  - `max` — the maximum possible number in the set (no more than 1000).
  - `quantity` — the number of numbers to pick (value between `min` and `max`).
- The function generates the specified quantity of unique numbers within the given range.
- The function returns a sorted list of randomly selected unique numbers.
- If the parameters do not meet the constraints, the function returns an empty list.

---

### Recommendations for Implementation:
- Ensure input parameters meet the specified constraints.
- Use the `random` module to generate random numbers.
- Use a set or another mechanism to ensure the uniqueness of the numbers.
- Remember that `get_numbers_ticket` returns a sorted list of unique numbers.

---

### Evaluation Criteria:
- **Input validity**: The function must validate the parameters correctly.
- **Uniqueness**: All numbers in the output must be unique.
- **Requirement compliance**: The result must be a sorted list.
- **Code readability**: The code should be clean and well documented.

---

### Example:

Suppose you need to pick 6 unique numbers for a lottery ticket, where the numbers must be in the range from 1 to 49. You can use your function like this:

```python
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)

