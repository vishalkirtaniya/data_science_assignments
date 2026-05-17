# Assignment 1: NumPy Fundamentals — The Data Warehouse

> **Module:** Data Analytics with NumPy  
> **Topic:** Array Creation · Data Types · Slicing · Indexing · Boolean Masking  
> **Difficulty:** ⭐⭐☆☆☆

---

## Background

You've joined **DataForge**, a company that processes large numerical datasets for logistics clients. Your senior has asked you to ditch Python lists entirely and rebuild the team's data pipeline using NumPy. Your job is to prove you understand how NumPy arrays work — from creation to manipulation to memory efficiency.

---

## Requirements

### Part A — Array Creation & Properties

Create the following arrays **without hardcoding values** — use NumPy's built-in creation functions:

| #   | Array to create                                            |
| --- | ---------------------------------------------------------- |
| 1   | A 1D array of all odd numbers from 1 to 19                 |
| 2   | A 4×4 identity matrix                                      |
| 3   | A 3×5 array filled entirely with the value `7`             |
| 4   | An array of 8 evenly spaced values between `0.0` and `1.0` |
| 5   | A 2D array of shape `(3, 4)` filled with zeros             |

For **each** of the five arrays, print its `shape`, `size`, `ndim`, and `dtype`.

---

### Part B — Data Types & Memory

Your senior is worried about memory usage on large datasets. Demonstrate you understand dtypes:

1. Create an array `[1.7, 2.9, 3.1, 4.8, 5.5]` and print its default dtype
2. Convert it to `int32` — print the result and explain in a **comment** what happened to the decimal values
3. Create two identical arrays of 10,000 elements — one as `int64`, one as `int32`. Print the memory (`.nbytes`) of both and calculate how much memory was saved
4. Create a complex number array `[2+3j, 4+5j, 6+7j]` and print its dtype

**Expected output format for task 3:**

```
int64 array: 80000 bytes
int32 array: 40000 bytes
Memory saved: 40000 bytes
```

---

### Part C — Reshaping, Flattening & Slicing

You've received a flat array of 12 sensor readings:

```python
readings = np.arange(1, 13)  # [1, 2, 3, ..., 12]
```

Using only NumPy operations on this array:

1. Reshape it into a `(3, 4)` matrix representing 3 days × 4 time slots
2. Extract only the readings from **Day 2** (second row)
3. Extract the readings from the **last 2 time slots of every day** (last 2 columns, all rows)
4. Flatten it back to 1D
5. From the flat array, slice every alternate reading (index 0, 2, 4, ...)

---

### Part D — The View Trap ⚠️

This is the most important conceptual part of this assignment.

```python
arr = np.array([10, 20, 30, 40, 50, 60])
sliced = arr[2:5]
sliced[0] = 999
```

1. Print `arr` after the above code runs — add a comment explaining **why** it changed
2. Fix it so that modifying `sliced` does **not** affect `arr`
3. Prove the fix worked — modify the new slice and print `arr` to confirm it's unchanged

---

### Part E — Fancy Indexing & Boolean Masking

You have daily temperature readings (°C) from a weather station:

```python
temps = np.array([22, 35, 18, 41, 29, 15, 38, 27, 44, 12])
```

1. Use **fancy indexing** to extract temperatures at positions `[1, 3, 6, 8]`
2. Use **boolean masking** to find all temperatures above `30°C`
3. Use **boolean masking** to find temperatures between `20°C` and `35°C` inclusive
4. **Cap all temperatures above 40°C at exactly 40** — do this in one line using boolean masking assignment

---

## Hints

> 💡 **Part A** — `np.arange`, `np.eye`, `np.full`, `np.linspace`, `np.zeros` each solve one of the five tasks. Match each to the right one.

> 💡 **Part B** — Use `np.ones(10000, dtype=np.int64)` and the same with `int32`. Compare `.nbytes`.

> 💡 **Part C** — For the last 2 columns of all rows, think about what `arr[:, -2:]` means.

> 💡 **Part D** — The entire fix is one method call. Look up `.copy()`.

> 💡 **Part E task 3** — Combine two conditions using `&`. Each condition needs its own parentheses: `(cond1) & (cond2)`.

> 💡 **Part E task 4** — Boolean masking works on the **left side** of an assignment too: `arr[mask] = value`.

---

## Submission Checklist

- [ ] Part A: all 5 arrays created using NumPy functions, properties printed for each
- [ ] Part B: dtype conversion done, memory comparison printed with savings calculated
- [ ] Part C: reshape, row/column slicing, flatten, and alternate elements all correct
- [ ] Part D: view trap demonstrated with comment, `.copy()` fix applied and verified
- [ ] Part E: fancy indexing, 3 boolean masks, and in-place cap all working

---

_Make sure slicing and masking feel natural before moving to Assignment 2 — it gets heavier._
