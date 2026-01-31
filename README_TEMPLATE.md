# Your Assignment Parameters

These are your unique values for Lab 2. Use these exact values in your code.

## Task Values

| Parameter | Your Value |
|-----------|------------|
| Grade Thresholds | {grade_thresholds} |
| Test Samples | {test_samples} |
| Drilling Depths | {drilling_depths} |
| Base Rate | ${base_rate}/meter |

## Task 1: Grade Classification (20 marks)

Create `src/lab2_classify.py` with a function that classifies ore grades using YOUR thresholds:

```python
# lab2_classify.py
# Your Name: [YOUR NAME]
# Student ID: [YOUR ID]

def classify_grade(grade):
    """
    Classify an ore grade value into categories.

    Args:
        grade: Numeric grade value (can be float or int)

    Returns:
        str: Classification category

    YOUR THRESHOLDS:
    - High Grade: grade >= {grade_thresholds}['high']
    - Medium Grade: grade >= {grade_thresholds}['medium']
    - Low Grade: grade >= {grade_thresholds}['low']
    - Sub-economic: grade < {grade_thresholds}['low']
    - Invalid: grade < 0
    """
    # TODO: Implement the classification logic using if/elif/else
    pass


# Test with YOUR sample values
if __name__ == "__main__":
    test_grades = {test_samples}

    print("Grade Classification Results:")
    print("-" * 40)
    for grade in test_grades:
        result = classify_grade(grade)
        print(f"Grade {grade:6.2f} -> {result}")
```

## Task 2: Sample Processing with For Loops (20 marks)

Create `src/lab2_processing.py` that processes sample data:

```python
# lab2_processing.py

def process_samples(samples):
    """
    Process a list of sample grades and return statistics.

    Args:
        samples: List of numeric grade values

    Returns:
        dict: Dictionary containing:
            - 'count': total number of valid samples (>= 0)
            - 'total': sum of all valid grades
            - 'average': average of valid grades (or 0 if no valid samples)
            - 'max_grade': highest valid grade (or None if no valid samples)
            - 'min_grade': lowest valid grade (or None if no valid samples)
    """
    # TODO: Use a for loop to iterate through samples
    # TODO: Skip negative values (they are invalid)
    pass


def count_by_category(samples, thresholds):
    """
    Count samples in each category based on thresholds.

    Args:
        samples: List of grade values
        thresholds: Dict with 'high', 'medium', 'low' threshold values

    Returns:
        dict: Count of samples in each category
              {'high': n, 'medium': n, 'low': n, 'subeconomic': n, 'invalid': n}
    """
    # TODO: Use for loop and conditionals to count each category
    pass


if __name__ == "__main__":
    samples = {test_samples}
    thresholds = {grade_thresholds}

    stats = process_samples(samples)
    print("Sample Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")

    print("\nCategory Counts:")
    counts = count_by_category(samples, thresholds)
    for category, count in counts.items():
        print(f"  {category}: {count}")
```

## Task 3: Input Validation with While Loops (15 marks)

Create `src/lab2_validation.py` demonstrating while loop validation:

```python
# lab2_validation.py

def get_valid_grade():
    """
    Prompt user for a valid grade value using a while loop.

    Valid grades are between 0 and 100 (inclusive).
    Keep prompting until a valid value is entered.

    Returns:
        float: Valid grade value
    """
    # TODO: Use while loop to repeatedly prompt until valid input
    pass


def get_valid_depth():
    """
    Prompt user for a valid depth value using a while loop.

    Valid depths are positive integers.
    Keep prompting until a valid value is entered.

    Returns:
        int: Valid depth value
    """
    # TODO: Use while loop with try/except for input validation
    pass


def collect_samples(num_samples):
    """
    Collect a specified number of valid sample grades.

    Args:
        num_samples: Number of samples to collect

    Returns:
        list: List of valid grade values
    """
    # TODO: Use while or for loop with validation
    pass


if __name__ == "__main__":
    print("=== Grade Input Validation Demo ===")

    # Demonstrate single value validation
    grade = get_valid_grade()
    print(f"Valid grade entered: {grade}")

    depth = get_valid_depth()
    print(f"Valid depth entered: {depth}")

    # Collect multiple samples
    print("\nCollecting 3 samples...")
    samples = collect_samples(3)
    print(f"Collected samples: {samples}")
```

## Task 4: Drilling Cost Calculator (25 marks)

Create `src/lab2_calculator.py` with a drilling cost function using YOUR base rate:

```python
# lab2_calculator.py

def calculate_drilling_cost(depth, base_rate={base_rate}, hardness='medium'):
    """
    Calculate the total drilling cost based on depth and conditions.

    Args:
        depth: Drilling depth in meters (positive integer)
        base_rate: Base cost per meter (default: {base_rate})
        hardness: Rock hardness - 'soft', 'medium', or 'hard'

    Returns:
        float: Total drilling cost, or -1 if invalid input

    Pricing Rules:
    - First 200 meters: base_rate per meter
    - 200-500 meters: base_rate * 1.25 per meter (25% surcharge)
    - Over 500 meters: base_rate * 1.5 per meter (50% surcharge)

    Hardness Adjustments (applied to total):
    - 'soft': 10% discount
    - 'medium': no adjustment
    - 'hard': 20% surcharge

    Invalid inputs (return -1):
    - Negative or zero depth
    - Invalid hardness value
    """
    # TODO: Implement the cost calculation with conditional logic
    pass


def format_cost_report(depth, cost, hardness):
    """
    Format a drilling cost as a report string.

    Args:
        depth: Drilling depth
        cost: Calculated cost
        hardness: Rock hardness

    Returns:
        str: Formatted report
    """
    # TODO: Create a formatted string report
    pass


if __name__ == "__main__":
    print("=== Drilling Cost Calculator ===")
    print(f"Base Rate: ${base_rate}/meter")
    print()

    # Test with YOUR drilling depths
    test_depths = {drilling_depths}
    hardness_options = ['soft', 'medium', 'hard']

    for depth in test_depths:
        print(f"Depth: {depth}m")
        for hardness in hardness_options:
            cost = calculate_drilling_cost(depth, {base_rate}, hardness)
            print(f"  {hardness}: ${cost:,.2f}")
        print()
```

## Task 5: Grade Statistics Report (20 marks)

Create `src/lab2_statistics.py` combining all control structures:

```python
# lab2_statistics.py

from lab2_classify import classify_grade
from lab2_processing import process_samples, count_by_category


def generate_report(samples, thresholds):
    """
    Generate a comprehensive grade statistics report.

    Args:
        samples: List of grade values
        thresholds: Dict with grade threshold values

    Returns:
        str: Formatted multi-line report
    """
    # TODO: Combine functions to generate a complete report
    # Include:
    # - Summary statistics (count, average, min, max)
    # - Category breakdown with counts and percentages
    # - List of high-grade samples (highlight these)
    pass


def find_anomalies(samples, threshold_multiplier=2.0):
    """
    Find grade values that are anomalously high.

    An anomaly is defined as a grade > (average * threshold_multiplier)

    Args:
        samples: List of grade values
        threshold_multiplier: Multiplier for anomaly detection

    Returns:
        list: List of anomalous grade values
    """
    # TODO: Calculate average and find anomalies using loops
    pass


if __name__ == "__main__":
    samples = {test_samples}
    thresholds = {grade_thresholds}

    report = generate_report(samples, thresholds)
    print(report)

    print("\n=== Anomaly Detection ===")
    anomalies = find_anomalies(samples)
    if anomalies:
        print(f"Found {len(anomalies)} anomalous values: {anomalies}")
    else:
        print("No anomalies detected.")
```

## Code Quality (included in each task)

- Include docstrings for all functions
- Use meaningful variable names
- Handle edge cases appropriately
- Format output clearly

## Testing Your Code

Run the automated tests locally:

```bash
pytest tests/visible/ -v
```

Push to GitHub to see your score on the Actions tab.
