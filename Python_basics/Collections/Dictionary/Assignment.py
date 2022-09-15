import json

airlines = ["India", "Pakistan", "Brazil", "Australia",
            "US", "India", "Pakistan", "Pakistan", "Brazil",
            "Australia", "US", "India"]

unique_countries = []

airlines_count = {}

for country in airlines:
    if country not in unique_countries:
        unique_countries.append(country)

# unique countries
# print(unique_countries)

for country in unique_countries:
    airlines_count[country] = 0

# print(json.dumps(airlines_count, indent=4))

for country in airlines:
    airlines_count[country] += 1


print(json.dumps(airlines_count, indent=4))

