# Assignment 2: SmartSuggest — Recommendations Engine

> **Course:** Data Science Internship  
> **Topic:** Pure Python · Mutual Friend Suggestions · Collaborative Filtering  
> **Difficulty:** ⭐⭐⭐☆☆  
> **Prerequisite:** Assignment 1 — `cleaned_devCircle_data.json` must exist

---

## Background

Your manager at DevCircle is impressed with the cleaned data. Now she wants you to build **two core features** for the platform:

1. **"Developers You May Know"** — suggest new connections based on mutual friends
2. **"Communities You Might Like"** — suggest pages using collaborative filtering

This is the same logic that powers friend suggestions on LinkedIn and content recommendations on Facebook — you're building a simplified version of it from scratch using pure Python.

---

## Requirements

Use `cleaned_devCircle_data.json` from Assignment 1 as your data source.

---

### Part A — Developers You May Know

Write a function `people_you_may_know(user_id, data)` that:

1. Finds all users who are **not** already friends with `user_id` and are **not** `user_id` themselves
2. Counts how many **mutual friends** each of those users shares with `user_id`
3. Returns a **sorted list** of suggested user IDs — highest mutual friend count first
4. If two users have the same mutual friend count, sort by user ID ascending as a tiebreaker

**Expected output format** (resolve names — don't just print IDs):

```
Developers You May Know for Aryan (ID: 1):
  → Neha (ID: 2) — 1 mutual friend(s)
  → Karan (ID: 3) — 2 mutual friend(s)
```

> The order above is just an example — your output will depend on your cleaned dataset.

---

### Part B — Communities You Might Like

Write a function `pages_you_might_like(user_id, data)` that:

1. Finds all other users who share **at least one** liked page with `user_id`
2. For each page those similar users like that `user_id` has **not** already liked, assign a **score = number of shared pages** between the two users
3. If multiple similar users recommend the same page, **add** their scores together
4. Return pages sorted by score, highest first

**Expected output format** (resolve page names — don't just print IDs):

```
Communities You Might Like for Aryan (ID: 1):
  → Cloud & DevOps (ID: 203) — score: 1
```

---

### Part C — Edge Cases

Your functions must handle all of the following gracefully — no crashes allowed:

| Situation                                  | Expected Output                                   |
| ------------------------------------------ | ------------------------------------------------- |
| `user_id` does not exist in the data       | `"User not found."`                               |
| User exists but has **no friends**         | `"No suggestions — user has no connections yet."` |
| User already likes **all available pages** | `"You're already following everything!"`          |

**Test these explicitly** by calling your functions with:

- `user_id = 99` (non-existent user)
- Any user in your dataset who has no friends after cleaning

---

## The Logic Behind It

### Mutual Friends (Part A)

```
User A's friends → loop through each friend
  → loop through that friend's friends
    → if they're not User A, and not already User A's friend
      → they're a suggestion candidate — count the mutual connection
```

The more times the same candidate appears, the more mutual friends they share with User A.

### Collaborative Filtering (Part B)

```
"If two people like some of the same pages, they probably share interests.
 Pages liked by one can be recommended to the other."
```

The **similarity score** between two users = number of pages they both like.  
Use this score to rank which pages to recommend first.

---

## Constraints

- ✅ Pure Python only — no `pandas`, `numpy`, or third-party libraries
- ✅ All name resolution must be dynamic (build lookup dicts from the data)
- ❌ Do not hardcode user names, page names, or expected outputs

---

## Hints

> 💡 At the start of each function, build two lookup dictionaries:  
> `{user_id: set(friends)}` and `{user_id: set(liked_pages)}`  
> This makes every subsequent operation much cleaner.

> 💡 For mutual friends — loop over the target user's friends, then loop over _each friend's_ friends. Every time you encounter a non-friend of the target user, increment their suggestion count.

> 💡 For page scoring — `set.intersection()` gives you the shared pages between two users. Its **length** is your similarity score for that pair.

> 💡 For name resolution — build a `{user_id: name}` and `{page_id: page_name}` lookup dict from the data at the start of your display logic.

---

## Submission Checklist

- [ ] `people_you_may_know()` returns correctly sorted suggestions with names
- [ ] `pages_you_might_like()` returns correctly scored page recommendations with names
- [ ] All three edge cases in Part C are handled without crashing
- [ ] Edge cases tested with `user_id = 99` and a friendless user
- [ ] No hardcoded values — logic works on any valid cleaned dataset

---

## Bonus Challenge (Optional)

If you finish early and want to push further:

- **Bonus 1:** Modify `people_you_may_know()` to also consider users who like the same pages as a secondary signal (not just mutual friends)
- **Bonus 2:** Print a combined "For You" feed that merges both suggestions into one ranked output

---

_Completed both assignments? Push them to GitHub with a `README.md` explaining what each script does — future you will thank present you._
