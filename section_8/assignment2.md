# Assignment 2: CodeHire — Recruitment Analytics Platform

> **Module:** Data Analysis with Pandas  
> **Topic:** Merging & Joining · Groupby · Aggregation · Transform · String Ops · Reports  
> **Difficulty:** ⭐⭐⭐⭐☆  
> **Prerequisite:** Assignment 1 — PandasMart  

---

## Background

**CodeHire** is a tech recruitment platform. Their candidate data, job listings, and application records are split across three separate tables. Your job is to merge them, clean them up, and generate aggregated reports for the hiring team — all using pandas.

---

## The Datasets

Create these three DataFrames directly in your script:

```python
import pandas as pd

candidates = pd.DataFrame({
    "CandidateID": [1, 2, 3, 4, 5, 6],
    "Name": ["Aarav", "Bhavna", "Chirag", "Divya", "Eshan", "Fatima"],
    "City": ["Delhi", "Mumbai", "Bangalore", "Delhi", "Mumbai", "Bangalore"],
    "Skills": ["Python", "SQL", "Python", "ML", "Python", "SQL"],
    "YearsExp": [2, 5, 3, 7, 1, 4]
})

jobs = pd.DataFrame({
    "JobID": [101, 102, 103, 104],
    "Title": ["Data Analyst", "ML Engineer", "Python Dev", "SQL Specialist"],
    "MinExp": [2, 5, 2, 3],
    "Location": ["Delhi", "Bangalore", "Mumbai", "Delhi"]
})

applications = pd.DataFrame({
    "AppID": [1, 2, 3, 4, 5, 6, 7, 8],
    "CandidateID": [1, 2, 3, 1, 4, 5, 6, 3],
    "JobID": [101, 103, 102, 104, 101, 102, 103, 104],
    "Status": ["Selected", "Rejected", "Selected", "Pending",
               "Selected", "Rejected", "Pending", "Selected"],
    "InterviewScore": [88, 45, 92, 76, 85, 38, 67, 90]
})
```

---

## Requirements

### Part A — Merging

1. Merge `applications` with `candidates` on `CandidateID` using an **inner join**
2. Merge the result with `jobs` on `JobID` using an **inner join** — store as `df`
3. Print the shape and all column names of `df`
4. Separately, create a **left join** of `candidates` with `applications` on `CandidateID` — identify which candidates have **never applied** using `.isnull()`

**Expected output for task 4:**
```
Candidates who have never applied:
   CandidateID   Name    City Skills  YearsExp
...
```

---

### Part B — Groupby & Aggregation

Using the merged `df` from Part A:

1. Find the **average InterviewScore per City** — sort by score descending
2. Find the **total number of applications per Job Title**
3. Find the **highest InterviewScore per Status** (Selected / Rejected / Pending)
4. Use `.agg()` to compute `mean`, `max`, and `min` of `InterviewScore` grouped by `Skills`
5. Use multi-column groupby — find average `InterviewScore` grouped by both `City` and `Status`

Print each result with a clear label above it.

---

### Part C — Transform & Filter

1. Use `.transform()` to add a column `CityAvgScore` — the average interview score for each candidate's city (every row in the same city gets the same value)
2. Add a boolean column `AboveAvg` — `True` if the candidate's `InterviewScore` is above their `CityAvgScore`
3. Use `.filter()` on a groupby object to keep only rows from cities where the **average InterviewScore is above 70**
4. Add a `ScoreRank` column using `.rank(method='dense', ascending=False)` on `InterviewScore`

---

### Part D — String Operations & Type Conversion

1. Convert all names in `Name` to uppercase using `.str.upper()`
2. Find all candidates who have `"Python"` in their `Skills` using `.str.contains()`
3. Add a column `ExpLevel` using `.apply()`:

   | YearsExp | ExpLevel   |
   |----------|------------|
   | >= 5     | `"Senior"` |
   | >= 3     | `"Mid"`    |
   | < 3      | `"Junior"` |

4. Convert `InterviewScore` to `int32` using `.astype()` and confirm with `.dtypes`
5. Replace `"Pending"` in the `Status` column with `"Under Review"` using `.replace()`

---

### Part E — Full Recruitment Report

Write a function `recruitment_report(df, jobs)` that takes the merged DataFrame and the original jobs DataFrame, and prints this summary — **all values computed dynamically, nothing hardcoded**:

```
===== CodeHire Recruitment Report =====

Total Applications     : 8
Selected               : 3
Rejected               : 2
Under Review           : 3

Top Hiring City        : Delhi
Average Interview Score: 72.6

Best Performer         : Chirag (Score: 92)
Least Experienced      : Eshan (1 year)

Jobs with no Selections: SQL Specialist
```

Rules:
- Round average score to 1 decimal place
- "Top Hiring City" = city with the most applications
- "Best Performer" = candidate with the highest InterviewScore
- "Least Experienced" = candidate with the lowest YearsExp
- "Jobs with no Selections" = job titles where no application has `Status == "Selected"`

---

## Hints

> 💡 **Part A task 4** — After a left join, candidates with no applications will have `NaN` in the `AppID` column. Filter with `df[df["AppID"].isnull()]` to find them.

> 💡 **Part B task 4** — Pass a dict to `.agg()`:
> ```python
> .agg({"InterviewScore": ["mean", "max", "min"]})
> ```

> 💡 **Part C task 1** — `.transform("mean")` returns a Series of the **same length** as the original DataFrame — that's what makes it perfect for adding as a new column alongside the original rows.

> 💡 **Part C task 3** — `.filter()` takes a lambda where `x` is the entire group (a sub-DataFrame). Return `True` to keep the group, `False` to discard it.

> 💡 **Part E "Jobs with no Selections"** — Get the set of JobIDs that have at least one "Selected" application. Then find jobs from the `jobs` DataFrame whose `JobID` is **not** in that set using `~df["JobID"].isin(selected_job_ids)`.

---

## Submission Checklist

- [ ] Part A: inner join produces correct shape, unapplied candidates identified correctly
- [ ] Part B: all 5 aggregations correct with labels printed
- [ ] Part C: `CityAvgScore` column added via transform, filter removes low-scoring cities, rank column added
- [ ] Part D: string ops, apply, astype, and replace all working — dtypes verified
- [ ] Part E: `recruitment_report()` prints all values dynamically with correct numbers

---

## Bonus Challenge (Optional)

If you finish early:

- **Bonus 1:** Add a `PassRate` metric to the report — percentage of applications that resulted in "Selected"
- **Bonus 2:** Export the full report as a formatted Excel file with separate sheets for each city's data
- **Bonus 3:** Find candidates whose `YearsExp` meets the `MinExp` requirement for the job they applied to — add an `Eligible` boolean column to `df`