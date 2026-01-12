"""
Descriptive Statistics Analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

sns.set_theme(style="whitegrid")
sns.set_context("notebook", font_scale=1.1)

# ============================================================
# SETTINGS (Modify this section only)
# ============================================================

DATA_PATH = "data.csv"

VARIABLES = ["var1", "var2", "var3"]   # Variables to analyze
GROUP_BY = None                         # Optional: grouping variable (set None if not needed)

# ============================================================
# Helper Functions
# ============================================================

def get_numeric_insights(stats):
    """Generate insights for numeric variables"""
    insights = []
    
    # Skewness interpretation
    skewness_val = stats.get('skewness', 0)
    if abs(skewness_val) < 0.5:
        insights.append(f"Roughly symmetrical (skewness = {skewness_val:.2f})")
    elif abs(skewness_val) < 1:
        insights.append(f"Moderately skewed (skewness = {skewness_val:.2f})")
    else:
        insights.append(f"Highly skewed (skewness = {skewness_val:.2f})")
    
    # Coefficient of Variation
    mean_val = stats.get('mean', 0)
    std_dev = stats.get('std_dev', 0)
    if mean_val != 0:
        cv = (std_dev / abs(mean_val)) * 100
        if cv < 15:
            insights.append(f"Low variability (CV = {cv:.1f}%)")
        elif cv < 30:
            insights.append(f"Moderate variability (CV = {cv:.1f}%)")
        else:
            insights.append(f"High variability (CV = {cv:.1f}%)")
    
    return insights

# ============================================================
# Load Data
# ============================================================

df = pd.read_csv(DATA_PATH)

# ============================================================
# Data Overview
# ============================================================

print("=" * 60)
print("DESCRIPTIVE STATISTICS ANALYSIS")
print("=" * 60)

print(f"\n[Data Information]")
print(f"Total rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")
print(f"Variables to analyze: {VARIABLES}")
if GROUP_BY:
    print(f"Group by: {GROUP_BY}")

# ============================================================
# Analyze Each Variable
# ============================================================

for var in VARIABLES:
    print("\n" + "=" * 60)
    print(f"VARIABLE: {var}")
    print("=" * 60)
    
    series = df[var].copy()
    is_numeric = pd.api.types.is_numeric_dtype(series)
    
    # --------------------------------------------------------
    # Numeric Variable Analysis
    # --------------------------------------------------------
    if is_numeric:
        numeric_series = pd.to_numeric(series, errors='coerce')
        clean_series = numeric_series.dropna()
        
        if clean_series.empty:
            print("No valid numeric data to analyze.")
            continue
        
        # Basic statistics
        stats = {
            'count': int(clean_series.count()),
            'missing': int(numeric_series.isnull().sum()),
            'mean': float(clean_series.mean()),
            'std_dev': float(clean_series.std()),
            'min': float(clean_series.min()),
            'q1': float(clean_series.quantile(0.25)),
            'median': float(clean_series.quantile(0.50)),
            'q3': float(clean_series.quantile(0.75)),
            'max': float(clean_series.max()),
            'skewness': float(skew(clean_series)),
            'kurtosis': float(kurtosis(clean_series)),
        }
        
        print(f"\n[Type: Numeric]")
        print(f"\n[Descriptive Statistics]")
        print(f"  Count: {stats['count']}")
        print(f"  Missing: {stats['missing']}")
        print(f"  Mean: {stats['mean']:.4f}")
        print(f"  Std Dev: {stats['std_dev']:.4f}")
        print(f"  Min: {stats['min']:.4f}")
        print(f"  Q1 (25%): {stats['q1']:.4f}")
        print(f"  Median: {stats['median']:.4f}")
        print(f"  Q3 (75%): {stats['q3']:.4f}")
        print(f"  Max: {stats['max']:.4f}")
        print(f"  Skewness: {stats['skewness']:.4f}")
        print(f"  Kurtosis: {stats['kurtosis']:.4f}")
        
        # Insights
        insights = get_numeric_insights(stats)
        print(f"\n[Insights]")
        for insight in insights:
            print(f"  - {insight}")
        
        # Grouped analysis
        if GROUP_BY and GROUP_BY in df.columns:
            print(f"\n[Grouped by {GROUP_BY}]")
            grouped = df.groupby(GROUP_BY)
            
            for name, group in grouped:
                group_series = pd.to_numeric(group[var], errors='coerce').dropna()
                if not group_series.empty:
                    print(f"\n  {GROUP_BY} = {name}:")
                    print(f"    Count: {group_series.count()}")
                    print(f"    Mean: {group_series.mean():.4f}")
                    print(f"    Std Dev: {group_series.std():.4f}")
                    print(f"    Min: {group_series.min():.4f}")
                    print(f"    Median: {group_series.median():.4f}")
                    print(f"    Max: {group_series.max():.4f}")
    
    # --------------------------------------------------------
    # Categorical Variable Analysis
    # --------------------------------------------------------
    else:
        clean_series = series.dropna()
        
        if clean_series.empty:
            print("No valid categorical data to analyze.")
            continue
        
        freq_table = clean_series.value_counts().reset_index()
        freq_table.columns = ['Value', 'Frequency']
        total = freq_table['Frequency'].sum()
        freq_table['Percentage'] = (freq_table['Frequency'] / total) * 100
        
        print(f"\n[Type: Categorical]")
        print(f"\n[Summary]")
        print(f"  Count: {total}")
        print(f"  Missing: {series.isnull().sum()}")
        print(f"  Unique values: {clean_series.nunique()}")
        print(f"  Mode: {clean_series.mode().iloc[0] if not clean_series.mode().empty else 'N/A'}")
        
        print(f"\n[Frequency Table]")
        for _, row in freq_table.iterrows():
            print(f"  {row['Value']}: {row['Frequency']} ({row['Percentage']:.1f}%)")
        
        # Insights
        print(f"\n[Insights]")
        if not freq_table.empty:
            top_category = freq_table.iloc[0]
            if top_category['Percentage'] > 50:
                print(f"  - '{top_category['Value']}' is dominant ({top_category['Percentage']:.1f}%)")
            else:
                print(f"  - Most frequent: '{top_category['Value']}' ({top_category['Percentage']:.1f}%)")
        
        # Grouped analysis
        if GROUP_BY and GROUP_BY in df.columns:
            print(f"\n[Grouped by {GROUP_BY}]")
            grouped = df.groupby(GROUP_BY)
            
            for name, group in grouped:
                group_series = group[var].dropna()
                if not group_series.empty:
                    print(f"\n  {GROUP_BY} = {name}:")
                    group_freq = group_series.value_counts()
                    for val, freq in group_freq.items():
                        pct = freq / len(group_series) * 100
                        print(f"    {val}: {freq} ({pct:.1f}%)")

# ============================================================
# Visualizations
# ============================================================

print("\n" + "=" * 60)
print("GENERATING PLOTS...")
print("=" * 60)

n_vars = len(VARIABLES)
n_cols = min(2, n_vars)
n_rows = (n_vars + n_cols - 1) // n_cols

fig, axes = plt.subplots(n_rows, n_cols, figsize=(7 * n_cols, 5 * n_rows))

if n_vars == 1:
    axes = [axes]
else:
    axes = axes.flatten()

for idx, var in enumerate(VARIABLES):
    ax = axes[idx]
    series = df[var].copy()
    is_numeric = pd.api.types.is_numeric_dtype(series)
    
    if is_numeric:
        numeric_series = pd.to_numeric(series, errors='coerce').dropna()
        if not numeric_series.empty:
            sns.histplot(numeric_series, kde=True, ax=ax, color='#5B9BD5')
            ax.set_xlabel('Value', fontsize=11)
            ax.set_ylabel('Frequency', fontsize=11)
    else:
        clean_series = series.dropna()
        if not clean_series.empty:
            top_n = clean_series.value_counts().nlargest(20)
            sns.barplot(x=top_n.values, y=top_n.index, ax=ax, orient='h', palette='crest')
            ax.set_xlabel('Frequency', fontsize=11)
            ax.set_ylabel(var, fontsize=11)
    
    ax.set_title(f'Distribution of {var}', fontsize=12, fontweight='bold')

# Hide empty subplots
for idx in range(n_vars, len(axes)):
    axes[idx].set_visible(False)

plt.tight_layout()
plt.savefig('descriptive_statistics_plots.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# Summary Table (for numeric variables)
# ============================================================

print("\n" + "=" * 60)
print("SUMMARY TABLE (NUMERIC VARIABLES)")
print("=" * 60)

numeric_vars = [var for var in VARIABLES if pd.api.types.is_numeric_dtype(df[var])]

if numeric_vars:
    summary_data = []
    for var in numeric_vars:
        series = pd.to_numeric(df[var], errors='coerce').dropna()
        if not series.empty:
            summary_data.append({
                'Variable': var,
                'N': series.count(),
                'Mean': series.mean(),
                'Std': series.std(),
                'Min': series.min(),
                'Median': series.median(),
                'Max': series.max()
            })
    
    if summary_data:
        summary_df = pd.DataFrame(summary_data)
        print(f"\n{summary_df.round(4).to_string(index=False)}")
else:
    print("\nNo numeric variables to summarize.")

print("\n" + "=" * 60)
print("Analysis completed.")
print("=" * 60)
