travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(Country,Visits,Cities):
    travel_log.append({"country":Country,"visits":Visits,"cities":Cities})

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
