# Assignment 2: NumPy Analytics — The Logistics Dashboard

> **Module:** Data Analytics with NumPy  
> **Topic:** 3D Arrays · Axis Operations · Broadcasting · Statistical Functions  
> **Difficulty:** ⭐⭐⭐⭐☆  
> **Prerequisite:** Assignment 1 — NumPy Fundamentals

---

## Background

DataForge's biggest client has sent over a **weekly shipment dataset** — 5 warehouses, tracked over 7 days, with 4 metrics recorded per day. Your job is to analyze it using NumPy's mathematical functions, axis operations, and broadcasting — **no pandas, no loops where avoidable**.

---

## The Dataset

Generate it programmatically — do **not** hardcode any values:

```python
import numpy as np

np.random.seed(42)

# Shape: (5 warehouses, 7 days, 4 metrics)
# Metrics → [shipments_sent, shipments_received, damaged_goods, processing_time_hrs]
warehouse_data = np.random.randint(
    low=[50, 40, 0, 2],
    high=[200, 180, 20, 12],
    size=(5, 7, 4)
)
```

This gives you a **3D array** of shape `(5, 7, 4)`.  
Always use `np.random.seed(42)` so your results are reproducible.

---

## Requirements

### Part A — Multidimensional Indexing

Using only indexing and slicing on `warehouse_data`:

1. Print the **entire data for Warehouse 3** (index 2) — verify its shape is `(7, 4)`
2. Extract **Day 1's data across all warehouses** — verify its shape is `(5, 4)`
3. Extract the **processing time column** (metric index 3) for all warehouses and all days — verify its shape is `(5, 7)`
4. Get the **damaged goods count** (metric index 2) for Warehouse 1 on Day 5 — single value

Print each result with a label and its shape:

```
Warehouse 3 data — shape: (7, 4)
Day 1 all warehouses — shape: (5, 4)
Processing times — shape: (5, 7)
Warehouse 1, Day 5, Damaged Goods: 11
```

---

### Part B — Axis-Based Aggregations

Answer the following business questions using NumPy functions. **No loops allowed.**

| #   | Question                                                            | Expected output shape |
| --- | ------------------------------------------------------------------- | --------------------- |
| 1   | Total shipments **sent** (metric 0) per warehouse across all 7 days | `(5,)`                |
| 2   | Average damaged goods (metric 2) per day across all warehouses      | `(7,)`                |
| 3   | Maximum processing time (metric 3) across the entire dataset        | scalar                |
| 4   | Which warehouse had the **highest** total shipments sent?           | scalar index          |
| 5   | Which day had the **lowest** average damaged goods?                 | scalar index          |

Print results with clear labels:

```
Total shipments sent per warehouse: [...]
Best performing warehouse index: 2
Worst day for damaged goods (index): 4
```

---

### Part C — Broadcasting in Action

Your manager provides a **reporting overhead** (fixed hours to add to each warehouse's processing time):

```python
overhead = np.array([1, 2, 1, 3, 2])  # shape: (5,) — one value per warehouse
```

1. Extract the processing time column as a `(5, 7)` array
2. Add the overhead to it using **broadcasting** — no loops. Each warehouse's overhead must apply to all 7 of its days
3. Print the result and verify its shape is still `(5, 7)`
4. Now **normalize** the shipments sent column (metric 0) across all warehouses and days:
   - Subtract the mean of the entire column
   - Divide by the standard deviation
   - Print the normalized values
   - Verify: `mean ≈ 0.0` and `std ≈ 1.0`

---

### Part D — Statistical Deep Dive

Using the full `warehouse_data` array, answer each question with one or two NumPy lines:

1. **Median** shipments received (metric 1) per warehouse — collapse the days axis
2. **95th percentile** of damaged goods (metric 2) across the entire dataset
3. **Cumulative shipments sent** (metric 0) for Warehouse 1 across the 7 days — what does the last value represent?
4. **Correlation** between total shipments sent and total shipments received across the 5 warehouses:
   - First collapse the days axis using `np.sum` to get shape `(5,)` for each metric
   - Then pass both to `np.corrcoef()`
5. **Unique values** of damaged goods across the entire dataset — print the count of unique values

---

### Part E — Daily Report Function

Write a function `daily_report(data, day_index)` that takes the full 3D array and a day index (0–6) and prints a formatted summary.

**Expected output for `daily_report(warehouse_data, 2)`:**

```
--- Daily Report: Day 3 ---
Total shipments sent across all warehouses : 782
Average shipments received                 : 118.4
Warehouse with most damaged goods today    : Warehouse 2
Average processing time today              : 6.8 hrs
```

Rules:

- All values must be **computed dynamically** — no hardcoding
- Numbers should be rounded to 1 decimal place
- "Day 3" means `day_index=2` — display as `day_index + 1`
- Test it by calling the function for **every day** in a loop:

```python
for i in range(7):
    daily_report(warehouse_data, i)
    print()
```

---

## Hints

> 💡 **Part A** — 3D indexing is `arr[depth, row, col]`. "All warehouses on day 1" means you want all depths, first row, all columns → `arr[:, 0, :]`.

> 💡 **Part B** — `axis=1` collapses the days dimension when you want a per-warehouse result. `axis=0` collapses warehouses when you want a per-day result.

> 💡 **Part C broadcasting** — `overhead` is shape `(5,)` but processing times are `(5, 7)`. Reshape overhead to `(5, 1)` using `.reshape(5, 1)` so NumPy broadcasts correctly across the 7 days.

> 💡 **Part D correlation** — Extract metric 0 with `warehouse_data[:, :, 0]`, then `np.sum(..., axis=1)` gives you shape `(5,)`. Do the same for metric 1, then `np.corrcoef(sent_totals, received_totals)`.

> 💡 **Part E** — `np.argmax()` on a 1D slice gives the index of the highest value. Add 1 when displaying warehouse numbers so they're human-readable (Warehouse 1, not Warehouse 0).

---

## Submission Checklist

- [ ] Part A: all 4 indexing operations correct, shapes verified and printed
- [ ] Part B: all 5 questions answered using correct axis arguments, no loops
- [ ] Part C: broadcasting overhead works without reshaping manually in a loop, normalization mean ≈ 0 and std ≈ 1
- [ ] Part D: all 5 statistical operations computed correctly
- [ ] Part E: `daily_report()` works for all 7 days in a loop with no errors

---

## Bonus Challenge (Optional)

If you finish early:

- **Bonus 1:** Add a `weekly_summary(data)` function that calls `daily_report()` for all 7 days and then prints an overall best and worst warehouse based on total shipments sent
- **Bonus 2:** Find the warehouse + day combination with the single highest damaged goods count — use `np.unravel_index(np.argmax(...), shape)` to get the exact index
