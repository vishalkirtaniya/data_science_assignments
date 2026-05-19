# Pandas — Data Analysis Assignments

> **Module:** Data Analysis with Pandas  
> **Course:** Data Science Internship — Coders of Delhi  
> **Prerequisites:** NumPy assignments completed

---

## What This Module Covers

These assignments are based on the Pandas section of the data science course. Topics covered:

- Series and DataFrame — core data structures
- Creating DataFrames from lists, dicts, arrays, CSV, Excel, JSON
- Exploratory Data Analysis (EDA) — head, info, describe, shape
- Data Selection — loc, iloc, at, iat, query
- Data Cleaning — missing values, duplicates, type conversion, string ops
- Data Transformation — sorting, ranking, renaming, apply, map, replace
- Reshaping — melt (wide → long) and pivot (long → wide)
- Aggregation & Groupby — agg, transform, filter
- Merging & Joining — inner, left, right, outer joins, concat
- Reading & Writing — CSV, Excel, JSON

---

## Assignments

| #   | File                                          | Topic                                                         | Difficulty |
| --- | --------------------------------------------- | ------------------------------------------------------------- | ---------- |
| 1   | [assignment1.md](./assignment1.md) | EDA, Cleaning, Selection, Filtering, Melt & Pivot, File I/O   | ⭐⭐⭐☆☆   |
| 2   | [assignment2.md](./assignment2.md)   | Merging, Groupby, Aggregation, Transform, String Ops, Reports | ⭐⭐⭐⭐☆  |

> Do them in order — Assignment 2 assumes you're comfortable with cleaning and selection from Assignment 1.

---

## How to Work Through These

1. Read the entire assignment before writing any code
2. Attempt each part without hints first
3. Only peek at a hint if you're stuck for more than 15 minutes — and only the hint for that specific part
4. Verify your output shapes and values at each step before moving on

---

## Setup

```bash
pip install pandas openpyxl
```

Run your solutions in a Jupyter notebook or a `.py` file — either works.

---

## Tools Used

- Python 3.x
- Pandas
- openpyxl (for Excel file writing)
- No NumPy directly — but it runs under the hood
