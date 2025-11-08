import csv
filename = "firewall_logs_2021_2023.csv"
deny_count = 0
allow_count = 0

print("Processing file:", filename)

with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    for line in csvreader:
        if "DENY" in line:
            deny_count += 1
        elif "ALLOW" in line:
            allow_count += 1

print(f"Total DENY entries: {deny_count}")
print(f"Total ALLOW entries: {allow_count}")