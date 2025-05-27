def dates_to_iso8601(date_list):
    """Converts a list of 'Month Day, Year' dates to ISO-8601 'YYYY-MM-DD' format."""
    month_map = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }
    result = []
    for date in date_list:
        date = date.strip().replace(",", "")
        parts = date.split()
        if len(parts) != 3:
            continue  # skip invalid dates
        month_str, day_str, year_str = parts
        month = month_map.get(month_str)
        day = day_str.zfill(2)
        result.append(f"{year_str}-{month}-{day}")
    return result

def sort_dates(date_list):
    """Sorts a list of 'Month Day, Year' dates chronologically (ignoring irrelevant whitespace)."""
    def to_iso(date):
        date = date.strip().replace(",", "")
        parts = date.split()
        if len(parts) != 3:
            return "9999-99-99"  # push invalids to the end
        month_map = {
            "January": "01", "February": "02", "March": "03", "April": "04",
            "May": "05", "June": "06", "July": "07", "August": "08",
            "September": "09", "October": "10", "November": "11", "December": "12"
        }
        month = month_map.get(parts[0])
        day = parts[1].zfill(2)
        year = parts[2]
        return f"{year}-{month}-{day}"

    sorted_pairs = sorted(date_list, key=lambda d: to_iso(d))
    return sorted_pairs
