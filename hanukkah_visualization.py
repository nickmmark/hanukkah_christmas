import matplotlib.pyplot as plt

# Generate corrected data starting with Gregorian year 2024
visualization_data_corrected = []
for hebrew_year in range(5785, 5785 + 1000):
    try:
        hanukkah_eve = get_hanukkah_eve_gregorian(hebrew_year)
        hanukkah_eve_date = date(hanukkah_eve.year, hanukkah_eve.month, hanukkah_eve.day)
        christmas = date(hanukkah_eve.year, 12, 25)
        hanukkah_days = [hanukkah_eve_date + timedelta(days=i) for i in range(8)]
        overlap = christmas in hanukkah_days
        visualization_data_corrected.append({
            "Hebrew Year": hebrew_year,
            "Gregorian Year": hanukkah_eve.year,
            "Overlap": overlap
        })
    except Exception:
        continue

# Filter to start from Gregorian year 2024
visualization_data_2024 = [entry for entry in visualization_data_corrected if entry["Gregorian Year"] >= 2024]

# Create the visualization
fig, ax = plt.subplots(figsize=(20, 15))
for idx, entry in enumerate(visualization_data_2024):
    x = idx % 50  # Columns
    y = -(idx // 50)  # Rows
    color = 'blue' if entry["Overlap"] else 'red'
    ax.add_patch(plt.Rectangle((x, y), 1, 1, color=color))
    ax.text(x + 0.5, y + 0.5, str(entry["Gregorian Year"]), color="white", ha='center', va='center', fontsize=8)

# Set limits and labels
ax.set_xlim(0, 50)
ax.set_ylim(-len(visualization_data_2024) // 50 - 1, 0)
ax.set_aspect('equal')
ax.axis('off')
plt.title("Hanukkah and Christmas Overlaps (Starting from 2024)", fontsize=16, pad=20)
plt.show()
