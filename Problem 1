def dates_to_iso8601(dates_list):
    months = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }
    iso_dates = []
    for date in dates_list:
        parts = date.replace(",", "").split()
        month = months[parts[0]]
        day = parts[1].zfill(2)
        year = parts[2]
        iso_dates.append(f"{year}-{month}-{day}")
    return iso_dates
def sort_dates(dates_list):
    iso_dates = dates_to_iso8601(dates_list)
    combined = list(zip(iso_dates, dates_list))
    combined.sort()
    return [original for _, original in combined]
