# DS-EXP3 — Mean, Median, Mode (without built-in functions)

**Dataset:** Sub_Division_IMD_2017.csv — IMD subdivision-wise monthly rainfall. Sample used: ANNUAL rainfall for Konkan & Goa (117 years, 1901–2017).

**Use case:** KJS-AGR-01 — AI Irrigation Advisory System

## What's covered
Mean, Median, and Mode computed manually — no built-in library functions (no `numpy.mean`, no `statistics.mode`) — just plain Python loops and sorting.

## Files
- `exp3_mean_median_mode.py` — standalone script
- `EXP3_MeanMedianMode_16014324020.ipynb` — notebook with output
- `EXP3_MeanMedianMode_notebook.pdf` — notebook as PDF
- `Sub_Division_IMD_2017.csv` — dataset

## Result
```
Mean   = 2987.53
Median = 2968.5
Mode   = 2792.9  (occurs 1 time(s))
```

Mean and Median are close, suggesting a fairly symmetric distribution. Mode isn't very meaningful here since rainfall values are continuous and rarely repeat exactly.
