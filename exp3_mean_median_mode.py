"""
EXP 3 - Measures of Central Tendency (Mean, Median, Mode)
Dataset: Sub_Division_IMD_2017.csv (IMD subdivision-wise monthly rainfall, India)
Use case: KJS-AGR-01 (AI Irrigation Advisory) -- same dataset used in EXP1 & EXP2

No built-in statistics functions used (no np.mean, np.median, statistics.mode, etc.)
Everything is computed manually with plain Python loops.
"""

import pandas as pd

df = pd.read_csv("Sub_Division_IMD_2017.csv")

# single-attribute sample: ANNUAL rainfall for Konkan & Goa, 1901-2017 (117 values)
konkan = df[df['SUBDIVISION'] == 'Konkan & Goa'].sort_values('YEAR').reset_index(drop=True)
data = konkan['ANNUAL'].tolist()

print("Sample size (n):", len(data))
print("First 10 values:", data[:10])


# ---------------------------------------------------------
# MEAN - sum of all values / number of values
# ---------------------------------------------------------
def manual_mean(values):
    total = 0
    for x in values:
        total += x
    return total / len(values)


# ---------------------------------------------------------
# MEDIAN - middle value after sorting
# ---------------------------------------------------------
def manual_median(values):
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    else:
        return sorted_vals[mid]


# ---------------------------------------------------------
# MODE - most frequently occurring value
# ---------------------------------------------------------
def manual_mode(values):
    counts = {}
    for x in values:
        counts[x] = counts.get(x, 0) + 1

    best_val = None
    best_count = 0
    for val, c in counts.items():
        if c > best_count:
            best_val = val
            best_count = c
    return best_val, best_count


mean_val = manual_mean(data)
median_val = manual_median(data)
mode_val, mode_count = manual_mode(data)

print("\n--- Results ---")
print("Mean   =", round(mean_val, 2))
print("Median =", round(median_val, 2))
print("Mode   =", mode_val, " (occurs", mode_count, "time(s))")
