# (Google) Count unique email address

# Take-aways
# 1) string.split('delimiter'), return a list, can assign each item in output list to variable
# 2) string.replace("target delimiter", "replace with"), return a string
# 3) set(), add(hashable), len(set) = num. unique elements

# Best solution
def numUniqueEmailsBest(emails):
    addresses = set()
    for email in emails:
        local, domain = email.split("@")
        local = local.split("+")[0].replace(".", "")
        addresses.add(local + "@" + domain)
    return len(addresses)

# My solution
def numUniqueEmails(emails):
    # Keep track of local and domain names
    localNames, domainNames = set(), set()
    flags = [".", "+"]
    numUnique = 0

    # Split the string by flags
    for email in emails:
        # Get local and domain names by @
        parts = email.split("@")
        local, domain = parts[0], parts[1]
        # Extract substring before first +
        plus_split = local.split(flags[1])
        if plus_split:
            local = plus_split[0]
        # Join each 'space' with ''
        dot_split = local.split(flags[0])
        if dot_split:
            local = "".join(dot_split)
        # Increment if current email local OR domain is unique
        if (local not in localNames) or (domain not in domainNames):
            numUnique += 1
            localNames.add(local)
            domainNames.add(domain)
    return numUnique