# Descriptive Statistics Validation Report

Cross-Validation with JASP

---

## Validation Environment

| Item | Details |
|------|---------|
| JASP Version | 0.19.3 |
| Validation Date | January 2025 |
| Test Dataset | mtcars (n=32) |
| Test Variable | mpg (miles per gallon) |

---

## Numeric Variable Validation

| Statistic | This Site | JASP | Match |
|-----------|-----------|------|-------|
| Count | 32 | 32 | ✓ |
| Missing | 0 | 0 | ✓ |
| Mean | 20.091 | 20.091 | ✓ |
| Std Dev | 6.027 | 6.027 | ✓ |
| Min | 10.400 | 10.400 | ✓ |
| 25th Percentile (Q1) | 15.425 | 15.425 | ✓ |
| Median | 19.200 | 19.200 | ✓ |
| 75th Percentile (Q3) | 22.800 | 22.800 | ✓ |
| Max | 33.900 | 33.900 | ✓ |
| Skewness | 0.611 | 0.611 | ✓ |
| Kurtosis | -0.373 | -0.373 | ✓ |

---

## Categorical Variable Validation

Test Dataset: mtcars - `cyl` (cylinder count)

| Statistic | This Site | JASP | Match |
|-----------|-----------|------|-------|
| Count | 32 | 32 | ✓ |
| Unique | 3 | 3 | ✓ |
| Mode | 8 | 8 | ✓ |

### Frequency Table

| Value | Frequency (This Site) | Frequency (JASP) | Percentage | Match |
|-------|----------------------|------------------|------------|-------|
| 4 | 11 | 11 | 34.4% | ✓ |
| 6 | 7 | 7 | 21.9% | ✓ |
| 8 | 14 | 14 | 43.8% | ✓ |

---

## Grouped Analysis Validation

Test: mpg grouped by `am` (transmission type)

| Group | Statistic | This Site | JASP | Match |
|-------|-----------|-----------|------|-------|
| Automatic (0) | Count | 19 | 19 | ✓ |
| Automatic (0) | Mean | 17.147 | 17.147 | ✓ |
| Automatic (0) | Std Dev | 3.834 | 3.834 | ✓ |
| Manual (1) | Count | 13 | 13 | ✓ |
| Manual (1) | Mean | 24.392 | 24.392 | ✓ |
| Manual (1) | Std Dev | 6.167 | 6.167 | ✓ |

---

## Validation Summary

| Category | Items Tested | Items Matched | Match Rate |
|----------|--------------|---------------|------------|
| Numeric Statistics | 11 | 11 | 100% |
| Categorical Statistics | 3 | 3 | 100% |
| Frequency Table | 3 | 3 | 100% |
| Grouped Statistics | 6 | 6 | 100% |
| **Total** | **23** | **23** | **100%** |

All values compared to 3 decimal places.

---

## Metrics Definitions

| Metric | Description |
|--------|-------------|
| Count | The number of non-missing observations |
| Missing | The number of missing (null or empty) values |
| Mean | The arithmetic average of the data |
| Std Dev | Standard deviation: a measure of the amount of variation |
| Min | The minimum value in the dataset |
| Q1 | The 25th percentile; 25% of data falls below this value |
| Median | The middle value of the dataset |
| Q3 | The 75th percentile; 75% of data falls below this value |
| Max | The maximum value in the dataset |
| Skewness | A measure of the asymmetry of the distribution |
| Kurtosis | A measure of the "tailedness" of the distribution |
| Unique | The number of distinct categories |
| Mode | The most frequently occurring value |

---

## References

- JASP Team (2025). JASP (Version 0.19.3) [Computer software]. https://jasp-stats.org/
- Test Data: R built-in dataset `mtcars`

---

*Last Updated: January 2025*
