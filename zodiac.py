from datetime import datetime

# List of zodiac signs with their date ranges (month, day)
ZODIAC_DATES = [
    ("Capricorn", (12, 22), (1, 19)),
    ("Aquarius", (1, 20), (2, 18)),
    ("Pisces", (2, 19), (3, 20)),
    ("Aries", (3, 21), (4, 19)),
    ("Taurus", (4, 20), (5, 20)),
    ("Gemini", (5, 21), (6, 20)),
    ("Cancer", (6, 21), (7, 22)),
    ("Leo", (7, 23), (8, 22)),
    ("Virgo", (8, 23), (9, 22)),
    ("Libra", (9, 23), (10, 22)),
    ("Scorpio", (10, 23), (11, 21)),
    ("Sagittarius", (11, 22), (12, 21)),
]

def infer_zodiac_sign(birth_date: str) -> str:
    """
    Determine zodiac sign based on birth date.
    Expects birth_date as 'YYYY-MM-DD'.
    Returns zodiac sign as string.
    """
    dt = datetime.strptime(birth_date, "%Y-%m-%d")
    month, day = dt.month, dt.day

    # Loop through zodiac date ranges to find matching sign
    for zodiac, (start_month, start_day), (end_month, end_day) in ZODIAC_DATES:
        # Handle Capricorn which overlaps year end and start
        if start_month == 12 and end_month == 1:
            if (month == 12 and day >= start_day) or (month == 1 and day <= end_day):
                return zodiac
        else:
            # Normal case: check if birth date falls within range
            if (month == start_month and day >= start_day) or \
               (month == end_month and day <= end_day) or \
               (start_month < month < end_month):
                return zodiac
    return "Unknown"
