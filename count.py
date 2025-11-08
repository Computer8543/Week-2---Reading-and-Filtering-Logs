import csv
filename = "firewall_logs_2021_2023.csv"
deny_count = 0
accept_count = 0

print("Processing file:", filename)

with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    for line in csvreader:
        if line[7] == "DENY":
            deny_count += 1
        elif line[7] == "ACCEPT":
            accept_count += 1

print(f"Total DENY entries: {deny_count}")
print(f"Total ACCEPT entries: {accept_count}")