import pandas as pd
import matplotlib.pyplot as plt

# Load data
final = pd.read_csv("Final_Dataset.csv")

# Convert date column
final["Month"] = pd.to_datetime(final["Month"])

# Create figure
plt.figure(figsize=(12,6))

# Main line
plt.plot(
    final["Month"],
    final["Search_Index"],
    linewidth=2,
    label="Search Index"
)

# Event lines
plt.axvline(
    pd.Timestamp("2020-03-01"),
    linestyle="--",
    linewidth=1.5
)

plt.axvline(
    pd.Timestamp("2022-02-01"),
    linestyle="--",
    linewidth=1.5
)

# COVID annotation
plt.annotate(
    "COVID-19",
    xy=(pd.Timestamp("2020-03-01"), 35),
    xytext=(pd.Timestamp("2018-01-01"), 55),
    arrowprops=dict(arrowstyle="->", lw=1.5),
    fontsize=12
)

# Ukraine annotation
plt.annotate(
    "Ukraine War",
    xy=(pd.Timestamp("2022-07-01"), 53),
    xytext=(pd.Timestamp("2021-01-01"), 50),
    arrowprops=dict(arrowstyle="->", lw=1.5),
    fontsize=12
)

# Labels
plt.title("Google Trends Search Index", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Search Index", fontsize=12)

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    "Search_Index.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Search Index graph saved!")