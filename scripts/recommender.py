"""
Bluestock Mutual Fund Capstone

Purpose:
Recommends top mutual funds
based on investor risk appetite.
Author: Yash Chowdhary
"""
import pandas as pd

# =====================================================
# LOAD DATA
# =====================================================

scheme_perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

# Convert numeric columns
scheme_perf['sharpe_ratio'] = pd.to_numeric(
    scheme_perf['sharpe_ratio'],
    errors='coerce'
)

scheme_perf['return_3yr_pct'] = pd.to_numeric(
    scheme_perf['return_3yr_pct'],
    errors='coerce'
)

# =====================================================
# FUND RECOMMENDER FUNCTION
# =====================================================

def recommend_funds(risk_appetite):

    # Filter funds by risk grade
    filtered_funds = scheme_perf[
        scheme_perf['risk_grade']
        .str.contains(
            risk_appetite,
            case=False,
            na=False
        )
    ]

    # Sort by Sharpe Ratio
    recommendations = (
        filtered_funds
        .sort_values(
            'sharpe_ratio',
            ascending=False
        )
        .head(3)
    )

    # Return selected columns
    return recommendations[
        [
            'scheme_name',
            'fund_house',
            'risk_grade',
            'sharpe_ratio',
            'return_3yr_pct'
        ]
    ]


# =====================================================
# TEST OUTPUT
# =====================================================

print("\n===== MODERATE RISK FUNDS =====\n")
print(recommend_funds("Moderate"))

print("\n===== LOW RISK FUNDS =====\n")
print(recommend_funds("Low"))

print("\n===== HIGH RISK FUNDS =====\n")
print(recommend_funds("High"))