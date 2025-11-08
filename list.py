import csv

filename = "firewall_logs_2021_2023.csv"
IP_POSITION = 1  # Assuming the IP address is in the second column (index 1)

# Set up list limit for unique IPs
LIST_LIMIT = 5

# Initialize
deny_count = 0

# Create a set to hold unique IP addresses
ip_set = set()

# Create a dictionary to hold DENY counts per IP address
ip_deny_count_dictionary = {ip_set: deny_count for ip_set in ip_set}

# Process the file
print("Processing file:", filename)
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    for line in csvreader:
        if "DENY" in line:
            if line[IP_POSITION] not in ip_set:
                ip_set.add(line[IP_POSITION])
                deny_count = 1
                ip_deny_count_dictionary[line[IP_POSITION]] = deny_count
            else:
                ip_deny_count_dictionary[line[IP_POSITION]] += 1

# Sort the dictionary by most to least DENY counts
ip_deny_count_dictionary = dict(sorted(ip_deny_count_dictionary.items(), key=lambda item: item[1], reverse=True))

# Output the results
print(f"Top {LIST_LIMIT} IP addresses with most DENY entries:")

# set up counter
count = 0

# Loop through the dictionary and print the top IPs
for ip, deny_count in ip_deny_count_dictionary.items():
    if count < LIST_LIMIT:
        print(f"IP Address: {ip} - DENY Count: {deny_count}")
        count += 1
    else:
        break