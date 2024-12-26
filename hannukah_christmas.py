# Calculate overlap percentage for the next 1,000 Hebrew years using fixed logic
def calculate_hanukkah_christmas_overlap_percentage_fixed(start_hebrew_year, num_years):
    overlaps = 0

    for hebrew_year in range(start_hebrew_year, start_hebrew_year + num_years):
        try:
            hanukkah_eve = get_hanukkah_eve_gregorian(hebrew_year)
            hanukkah_eve_date = date(hanukkah_eve.year, hanukkah_eve.month, hanukkah_eve.day)
            christmas = date(hanukkah_eve.year, 12, 25)
            hanukkah_days = [hanukkah_eve_date + timedelta(days=i) for i in range(8)]
            if christmas in hanukkah_days:
                overlaps += 1
        except Exception:
            continue

    # Calculate overlap percentage
    overlap_percentage = (overlaps / num_years) * 100
    return overlap_percentage, overlaps, num_years

# Run the calculation for the next 1,000 Hebrew years starting from 5785
overlap_percentage_fixed, overlaps_fixed, total_years_fixed = calculate_hanukkah_christmas_overlap_percentage_fixed(5785, 1000)

# Display the results
overlap_percentage_fixed, overlaps_fixed, total_years_fixed
