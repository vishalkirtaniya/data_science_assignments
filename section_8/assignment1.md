# Assignment 1: PandasMart — Retail Data Analysis

> **Module:** Data Analysis with Pandas  
> **Topic:** EDA · Data Cleaning · Selection & Filtering · Sorting · Melt & Pivot · File I/O  
> **Difficulty:** ⭐⭐⭐☆☆  

---

## Background

You've joined **PandasMart**, a retail chain that just migrated all their data from Excel to Python. Your manager has handed you a messy sales dataset and needs you to clean it, explore it, and reshape it for the analytics team — all using pandas.

---

## The Dataset

Create a file called `pandasmart_sales.csv` with the following data **exactly as given**:

```csv
OrderID,CustomerName,City,Category,Quantity,UnitPrice,OrderDate,SalesRep
1001,Alice,Delhi,Electronics,2,15000,2024-01-15,Raj
1002,Bob,Mumbai,Clothing,5,800,2024-01-20,Priya
1003,Charlie,Delhi,Electronics,1,25000,2024-02-10,Raj
1004,,Bangalore,Furniture,3,12000,2024-02-14,Amit
1005,Eve,Mumbai,Clothing,2,1500,2024-03-05,Priya
1006,Frank,Delhi,Electronics,4,8000,2024-03-18,Raj
1007,Bob,Mumbai,Clothing,5,800,2024-01-20,Priya
1008,Grace,Bangalore,Furniture,1,22000,2024-04-02,Amit
1009,Heidi,Delhi,,2,5000,2024-04-15,Raj
1010,Ivan,Mumbai,Electronics,3,18000,2024-05-01,Priya
1011,Alice,Delhi,Electronics,2,15000,2024-01-15,Raj
```

> Do **not** fix the data manually — your code must handle every issue programmatically.

---

## Requirements

### Part A — Load & Explore

1. Load `pandasmart_sales.csv` into a DataFrame
2. Print the first 5 rows, last 3 rows, and the shape
3. Print column names, data types, and non-null counts using `.info()`
4. Print summary statistics for all numeric columns using `.describe()`
5. Print how many missing values exist in **each column**

---

### Part B — Data Cleaning

1. Drop rows where `CustomerName` is missing
2. Fill missing `Category` values with the string `"Unknown"`
3. Identify duplicates using `.duplicated()`, print how many exist, then drop them
4. Convert `OrderDate` to datetime using `pd.to_datetime()`
5. Add a new column `TotalSale` = `Quantity × UnitPrice`
6. Standardize the `City` column to title case using `.str.title()`

After all cleaning steps, print the final shape and confirm no nulls remain in `CustomerName`.

**Expected shape after cleaning:** `(8, 9)` — verify this before moving on.

---

### Part C — Selection & Filtering

Using the cleaned DataFrame:

1. Select only the `CustomerName`, `Category`, and `TotalSale` columns
2. Use `.loc[]` to get all rows where `City` is `"Delhi"`
3. Use `.iloc[]` to get the first 3 rows and first 4 columns
4. Use `.query()` to find all orders where `TotalSale > 30000` and `City == 'Mumbai'`
5. Use boolean masking to find all Electronics orders placed by `SalesRep` `"Raj"`
6. Use `.at[]` to retrieve the `CustomerName` of the order at index `0`

---

### Part D — Sorting & Transformation

1. Sort the DataFrame by `TotalSale` descending — print the top 3
2. Sort by `City` ascending, then by `TotalSale` descending (multi-column sort)
3. Add a column `SaleCategory` using `.apply()` with this logic:

   | TotalSale | SaleCategory |
   |-----------|-------------|
   | >= 50000  | `"High"`    |
   | >= 20000  | `"Medium"`  |
   | < 20000   | `"Low"`     |

4. Rename the column `SalesRep` → `Representative`
5. Reorder columns so `TotalSale` and `SaleCategory` appear immediately after `OrderID`

---

### Part E — Melt & Pivot

Create this wide-format summary DataFrame in your script:

```python
summary = pd.DataFrame({
    "SalesRep": ["Raj", "Priya", "Amit"],
    "Q1_Sales": [48000, 12500, 36000],
    "Q2_Sales": [32000, 54000, 22000],
    "Q3_Sales": [61000, 29000, 47000]
})
```

1. Use `melt()` to convert it to long format with columns: `SalesRep`, `Quarter`, `Sales`
2. Use `pivot()` on the melted DataFrame to convert it back to wide format
3. Print both DataFrames — what do you notice about the column order after pivoting?

---

### Part F — Read & Write

1. Save the cleaned DataFrame to `cleaned_pandasmart.csv` — no index
2. Save the melted summary DataFrame to `quarterly_summary.json`
3. Save **both** the cleaned DataFrame and the pivot table to a single Excel file called `pandasmart_report.xlsx` with:
   - Sheet 1 named `"Sales"` → cleaned DataFrame
   - Sheet 2 named `"Quarterly"` → pivot table

---

## Hints

> 💡 **Part B task 3** — `.duplicated()` returns a boolean Series. Wrap it in `df[...]` to see the actual duplicate rows before dropping.

> 💡 **Part B task 4** — After converting with `pd.to_datetime()`, check that the dtype changed from `object` to `datetime64` using `.dtypes`.

> 💡 **Part C task 4** — In `.query()`, string values go inside single quotes within the query string. Use `and` not `&`.

> 💡 **Part D task 3** — Define a named function or lambda for `.apply()`. The function receives one value (a single `TotalSale`) and returns a string.

> 💡 **Part D task 5** — Build the new column order as a list: start with `["OrderID", "TotalSale", "SaleCategory"]`, then add the remaining columns.

> 💡 **Part E** — `id_vars` keeps the fixed column, `value_vars` lists the columns to melt. Set `var_name="Quarter"` and `value_name="Sales"` to name the new columns.

> 💡 **Part F task 3** — Use `pd.ExcelWriter` as a context manager with a `with` statement. Call `.to_excel()` twice inside it — once per sheet.

---

## Submission Checklist

- [ ] Part A: load and explore — all 5 steps complete
- [ ] Part B: all 6 cleaning steps done, final shape is `(8, 9)`, no nulls in `CustomerName`
- [ ] Part C: all 6 selection and filtering operations working correctly
- [ ] Part D: sorted, `SaleCategory` column added, column renamed and reordered
- [ ] Part E: melt and pivot both work, shapes verified
- [ ] Part F: `cleaned_pandasmart.csv`, `quarterly_summary.json`, and `pandasmart_report.xlsx` all saved correctly

---

*Assignment 2 is heavier on groupby, merging, and aggregation — get comfortable with selection and cleaning here first.*