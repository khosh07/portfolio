import pandas as pd
import plotly.express as px
import numpy as np

# ---------------------------
# 1️⃣ Load CSV
# ---------------------------
df = pd.read_csv("WDI_csv_data.csv")

# ---------------------------
# 2️⃣ Filter Pakistan ONLY
# ---------------------------
df = df[df["Country Name"] == "Pakistan"]

# ---------------------------
# 3️⃣ Filter indicators (Water & Electricity, Urban/Rural)
# ---------------------------
df = df[
    df["Series Name"].str.contains("water|electricity", case=False, na=False) &
    df["Series Name"].str.contains("urban|rural", case=False, na=False)
]

# ---------------------------
# 4️⃣ Identify year columns
# ---------------------------
year_cols = [col for col in df.columns if "[YR" in col]

# ---------------------------
# 5️⃣ Convert WIDE → LONG format
# ---------------------------
df_long = df.melt(
    id_vars=["Country Name", "Series Name"],
    value_vars=year_cols,
    var_name="Year",
    value_name="Value"
)

# ---------------------------
# 6️⃣ Clean Year and Value
# ---------------------------
df_long["Year"] = df_long["Year"].str.extract(r"(\d{4})").astype(int)
df_long["Value"] = pd.to_numeric(df_long["Value"], errors="coerce")

# ---------------------------
# 7️⃣ Keep ONLY years 1995–2025
# ---------------------------
df_long = df_long[(df_long["Year"] >= 1995) & (df_long["Year"] <= 2025)]

# ---------------------------
# 8️⃣ Create detailed Indicator labels
# ---------------------------
# Service Level: Basic Water / Safely Managed Water / Electricity
df_long["Service Level"] = np.where(
    df_long["Series Name"].str.contains("safely managed", case=False, na=False),
    "Safely Managed Water",
    np.where(
        df_long["Series Name"].str.contains("basic", case=False, na=False),
        "Basic Water",
        "Electricity"
    )
)

# Urban / Rural
df_long["Area"] = df_long["Series Name"].str.extract(
    r"(?i)(urban|rural)", expand=False
).str.title()

# Combine Service Level and Area
df_long["Indicator"] = df_long["Service Level"] + " - " + df_long["Area"]

# ---------------------------
# 9️⃣ Aggregate YEARLY values (in case multiple rows per year exist)
# ---------------------------
df_avg = df_long.groupby(
    ["Year", "Indicator"],
    observed=True
)["Value"].mean().reset_index()

# Sort by year for plotting
df_avg = df_avg.sort_values("Year")

# ---------------------------
# 🔟 Plot YEARLY line chart
# ---------------------------
fig = px.line(
    df_avg,
    x="Year",
    y="Value",
    color="Indicator",
    facet_col="Indicator",
    facet_col_wrap=2,
    facet_col_spacing=0.08,
    title="Access to Drinking Water & Electricity in Pakistan (1995–2025)",
    labels={
        "Value": "Access (% of population)",
        "Year": "Year"
    }
)

# Set y-axis scale 0–100
fig.update_yaxes(range=[0, 100])

# Show tick every year or every 5 years if crowded
fig.update_xaxes(dtick=1)  # one tick per year
fig.update_traces(line=dict(width=2))

# Show the interactive figure
fig.show()
