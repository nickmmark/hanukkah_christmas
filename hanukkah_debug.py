# convert GregorianDate to Python's date object before adding timedelta
def debug_small_range_fixed(start_hebrew_year, end_hebrew_year):
    debug_results = []
    for hebrew_year in range(start_hebrew_year, end_hebrew_year + 1):
        try:
            hanukkah_eve = get_hanukkah_eve_gregorian(hebrew_year)
            hanukkah_eve_date = date(hanukkah_eve.year, hanukkah_eve.month, hanukkah_eve.day)
            christmas = date(hanukkah_eve.year, 12, 25)
            hanukkah_days = [hanukkah_eve_date + timedelta(days=i) for i in range(8)]
            overlap = christmas in hanukkah_days
            debug_results.append({
                "Hebrew Year": hebrew_year,
                "Gregorian Year": hanukkah_eve.year,
                "Hanukkah Eve": hanukkah_eve_date,
                "Hanukkah Days": hanukkah_days,
                "Christmas Overlap": overlap
            })
        except Exception as e:
            debug_results.append({
                "Hebrew Year": hebrew_year,
                "Error": str(e)
            })
    return debug_results

# Test and debug for Hebrew years 5785 to 5795
# The years 2024 and 2030 (5785 and 5791) should have overlap
debug_results_fixed = debug_small_range_fixed(5785, 5795)
debug_results_fixed
