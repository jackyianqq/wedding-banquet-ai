import pandas as pd
import json

# Load Excel file
df = pd.read_excel("venues.xlsx")

# Convert DataFrame to JSON
venues_json = df.to_dict(orient="records")

# Save as JSON
with open("data/venues.json", "w", encoding="utf-8") as f:
    json.dump(venues_json, f, ensure_ascii=False, indent=2)

print("✅ Converted venues.xlsx to data/venues.json")
