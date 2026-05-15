# Assignment 1: CodeConnect — The Developer Network

> **Course:** Data Science Internship  
> **Topic:** Pure Python · Data Loading · Data Cleaning  
> **Difficulty:** ⭐⭐☆☆☆  

---

## Background

You've been hired as a Data Science Intern at **DevCircle**, a new social platform for developers. Your manager has handed you a raw dataset of users, their connections, and the tech communities they follow.

The data is messy and needs to be cleaned before any analysis can begin. Your job is to load it, fix all the issues programmatically, and produce a clean output file — all using **pure Python**.

---

## The Dataset

Create a file called `devCircle_data.json` with the following data **exactly as given**. Do not clean it manually — your code must handle everything:

```json
{
  "users": [
    {"id": 1, "name": "Aryan",  "friends": [2, 3, 5], "liked_pages": [201, 202]},
    {"id": 2, "name": "Neha",   "friends": [1, 3, 3], "liked_pages": [202, 203]},
    {"id": 3, "name": "Karan",  "friends": [1, 2],    "liked_pages": [201]},
    {"id": 4, "name": "",       "friends": [5],        "liked_pages": [204]},
    {"id": 5, "name": "Simran", "friends": [1],        "liked_pages": []},
    {"id": 6, "name": "Dev",    "friends": [],         "liked_pages": []}
  ],
  "pages": [
    {"id": 201, "name": "Open Source India"},
    {"id": 202, "name": "Backend Dev Talks"},
    {"id": 203, "name": "Cloud & DevOps"},
    {"id": 204, "name": "Frontend Masters"},
    {"id": 202, "name": "Backend Engineering"}
  ]
}
```

---

## Requirements

### Part A — Load & Display

1. Load `devCircle_data.json` using Python's built-in `json` module
2. Print all users with their friends and liked pages in a clean, readable format
3. Print all pages in the format `ID: Page Name`

**Expected output format:**
```
Users and Their Connections:

Aryan (ID: 1) - Friends: [2, 3, 5] - Liked Pages: [201, 202]
Neha  (ID: 2) - Friends: [1, 3, 3] - Liked Pages: [202, 203]
...

Pages:
201: Open Source India
202: Backend Dev Talks
...
```

---

### Part B — Clean the Data

Write a function `clean_data(data)` that performs **all four** of the following operations:

| # | Problem | Fix |
|---|---------|-----|
| 1 | Users with a missing or empty name | Remove them |
| 2 | Duplicate entries in a user's friends list | Remove duplicates, keep unique entries |
| 3 | Inactive users (empty friends **and** empty liked_pages) | Remove them |
| 4 | Duplicate page IDs | Keep the **first** occurrence, discard the rest |

After cleaning, save the result to `cleaned_devCircle_data.json` with indentation for readability.

---

### Part C — Cleaning Report

Write a function `cleaning_report(original, cleaned)` that takes the original and cleaned data dictionaries and prints a summary of what was fixed.

**Expected output format:**
```
--- Cleaning Report ---
Users removed: 2
Duplicate friend entries fixed: 1
Pages deduplicated: 1
```

> You'll need to compare counts **before and after** cleaning. Think about what to measure in the original data before you call `clean_data()`.

---

## Constraints

- ✅ Pure Python only — `json` and other built-in modules are fine
- ❌ No `pandas`, `numpy`, or any third-party libraries
- ✅ Your cleaning logic must work on **any** valid input in this format — no hardcoded answers

---

## Hints

> 💡 For removing duplicate friends — what data structure automatically eliminates duplicates? How do you convert back after?

> 💡 To keep the *first* occurrence of a duplicate page — think about what happens when you loop and check if you've already seen an ID before adding it.

> 💡 For the cleaning report — compute your counts *before* you mutate the data, then compare against the cleaned version.

---

## Submission Checklist

- [ ] `devCircle_data.json` created with the given data
- [ ] Part A: data loads and prints correctly
- [ ] Part B: `clean_data()` handles all four issues
- [ ] Part B: cleaned data saved to `cleaned_devCircle_data.json`
- [ ] Part C: `cleaning_report()` prints accurate counts
- [ ] No hardcoded fixes — logic works programmatically

---

*Assignment 2 builds on the output of this one. Complete and verify `cleaned_devCircle_data.json` before moving on.*