
def dates_to_iso8601(date_list):
    """Converts a list of dates in 'Month Day, Year' format to ISO-8601 'YYYY-MM-DD' format."""
    month_map = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }
    result = []
    for date in date_list:
        parts = date.replace(",", "").split()
        month = month_map[parts[0]]
        day = parts[1].zfill(2)
        year = parts[2]
        result.append(f"{year}-{month}-{day}")
    return result

def sort_dates(date_list):
    """Sorts a list of 'Month Day, Year' dates chronologically."""
    iso_dates = dates_to_iso8601(date_list)
    sorted_pairs = sorted(zip(iso_dates, date_list))
    return [original for _, original in sorted_pairs]
