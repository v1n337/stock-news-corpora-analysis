from datetime import datetime

bloomberg_date = "2006-10-20T20:16:16Z"
reuters_date = "Fri Oct 20, 2006 6:15pm EDT"

date3 = datetime.strptime(bloomberg_date, "%Y-%m-%dT%H:%M:%SZ")
print(date3)

date4 = datetime.strptime(reuters_date, '%a %b %d, %Y %I:%M%p %Z')
print(date4)
