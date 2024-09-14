
# FLAMES Relationship Predictor

This Python program implements the popular "FLAMES" game, predicting the relationship between two names based on the number of unique characters remaining after common letters are removed.

## How It Works

1. **Remove Common Letters**: Takes two input names and removes all common letters between them.
2. **Count Remaining Letters**: The remaining letters are concatenated and counted.
3. **FLAMES Result**: Using the count from the previous step, the program iterates through the `FLAMES` list and removes one option per round until a single relationship remains.

## FLAMES Outcomes

- **Friends**
- **Lovers**
- **Affectionate**
- **Marriage**
- **Enemies**
- **Siblings**

## Prerequisites

- Python 3.x

## Installation

1. Clone this repository or copy the code to a Python file, such as `flames.py`.
2. Ensure you have Python 3.x installed on your machine.

## How to Run

Run the program in your terminal or command prompt:

```bash
python flames.py
