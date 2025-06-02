from server import get_today_date
from datetime import datetime
import pytz # Make sure pytz is available for the test script
import os

# Get the timezone from the TZ environment variable, default to UTC if not set
tz_name = os.environ.get('TZ', 'UTC')
try:
    expected_tz = pytz.timezone(tz_name)
except pytz.exceptions.UnknownTimeZoneError:
    print(f"Error: Unknown timezone specified in TZ environment variable: {tz_name}")
    exit(1)

expected_date = datetime.now(expected_tz).strftime("%m/%d")
actual_date = get_today_date() # This should now use the TZ environment variable

print(f"TZ={tz_name}, Expected={expected_date}, Actual={actual_date}")

if expected_date == actual_date:
    print("Test PASSED")
else:
    print("Test FAILED")
    exit(1) # Exit with error code if test fails
