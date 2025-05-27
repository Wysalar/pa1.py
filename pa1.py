def dates_to_iso8601(date_list):
    """Converts a list of dates in 'Month Day, Year' format to ISO-8601 'YYYY-MM-DD' format."""
    month_map = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }
    result = []
    for date in date_list:
        if not date or not isinstance(date, str):
            continue
        cleaned = date.strip().replace(",", "")
        parts = cleaned.split()
        if len(parts) != 3 or parts[0] not in month_map:
            continue  # skip invalid formats
        month_str, day_str, year_str = parts
        month = month_map[month_str]
        day = day_str.zfill(2)
        result.append(f"{year_str}-{month}-{day}")
    return result

def sort_dates(date_list):
    """Sorts a list of 'Month Day, Year' dates chronologically."""
    def to_iso(date):
        try:
            return dates_to_iso8601([date])[0]
        except IndexError:
            return "9999-99-99"  # invalid dates go last
    return sorted(date_list, key=to_iso)

