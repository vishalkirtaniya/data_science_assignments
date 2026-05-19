# data_science_assignments

# Data Science Assignments

Practice assignments to reinforce data science concepts, structured in the CS50 style: clear problem specs, hints, no solutions handed to you.

Based on topics from the **Coders of Delhi — Data Science Internship** course.

---

## Sections

| Section                              | Module      | Topics                                         | Assignments |
| ------------------------------------ | ----------- | ---------------------------------------------- | ----------- |
| [Section 5](#section-5--pure-python) | Pure Python | JSON, data cleaning, deduplication, algorithms | 2           |
| [Section 7](#section-7--numpy)       | NumPy       | Arrays, broadcasting, indexing, statistics     | 2           |
| [Section 8](#section-8--pandas)      | Pandas      | EDA, cleaning, groupby, merging, reshaping     | 2           |

> Complete sections in order — each builds on the previous one.

---

## Section 5 — Pure Python

> **Prerequisites:** None — this is the starting point.

### What This Module Covers

- Loading and parsing JSON data
- Data cleaning and deduplication
- Implementing algorithms (mutual friends, collaborative filtering) from scratch
- Handling edge cases in pure Python

### Assignments

| #   | Assignment                            | Topics Covered                                                | Difficulty |
| --- | ------------------------------------- | ------------------------------------------------------------- | ---------- |
| 1   | CodeConnect — The Developer Network   | JSON loading, data cleaning, deduplication                    | ⭐⭐☆☆☆    |
| 2   | SmartSuggest — Recommendations Engine | Mutual friends algorithm, collaborative filtering, edge cases | ⭐⭐⭐☆☆   |

> Assignment 2 depends on the output of Assignment 1 — do them in order.

### Tools Used

- Python 3.x (built-in modules only — `json`, etc.)
- No pandas, numpy, or third-party libraries

---

## Section 7 — NumPy

> **Prerequisites:** Section 5 (Pure Python) completed.

### What This Module Covers

- Why NumPy is faster and more memory-efficient than Python lists
- Creating and inspecting NumPy arrays
- Data types, memory usage, and type casting
- Indexing, slicing, and the view vs copy trap
- Fancy indexing and boolean masking
- Multidimensional arrays and axis-based operations
- Broadcasting — operations across arrays of different shapes
- Built-in mathematical and statistical functions

### Assignments

| #   | Assignment     | Topic                                     | Difficulty |
| --- | -------------- | ----------------------------------------- | ---------- |
| 1   | assignment1.md | Array creation, dtypes, slicing, masking  | ⭐⭐☆☆☆    |
| 2   | assignment2.md | 3D arrays, axes, broadcasting, statistics | ⭐⭐⭐⭐☆  |

> Assignment 2 assumes comfort with the concepts in Assignment 1.

### Setup

```bash
pip install numpy
```

### Tools Used

- Python 3.x
- NumPy only — no pandas, no matplotlib for these assignments

---

## Section 8 — Pandas

> **Prerequisites:** Section 7 (NumPy) completed.

### What This Module Covers

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

### Assignments

| #   | Assignment     | Topic                                                         | Difficulty |
| --- | -------------- | ------------------------------------------------------------- | ---------- |
| 1   | assignment1.md | EDA, Cleaning, Selection, Filtering, Melt & Pivot, File I/O   | ⭐⭐⭐☆☆   |
| 2   | assignment2.md | Merging, Groupby, Aggregation, Transform, String Ops, Reports | ⭐⭐⭐⭐☆  |

> Assignment 2 assumes you're comfortable with cleaning and selection from Assignment 1.

### Setup

```bash
pip install pandas openpyxl
```

### Tools Used

- Python 3.x
- Pandas
- openpyxl (for Excel file writing)
- No NumPy directly — but it runs under the hood

---

## How to Work Through Assignments

1. Read the entire assignment before writing a single line of code
2. Attempt each part without hints first
3. If stuck for more than 15 minutes — read the hint for that part only
4. Verify your output shapes and values before moving to the next part

---

_More assignments will be added as new lecture topics are covered._
