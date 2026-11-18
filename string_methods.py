# String Methods Practice

name = "  priya sharma  "

print("Original:", name)
print("Upper:", name.upper())
print("Lower:", name.lower())
print("Strip:", name.strip())
print("Title:", name.strip().title())
print("Capitalize:", name.strip().capitalize())
print("Replace:", name.strip().replace("sharma", "patel"))
print("Split:", name.strip().split())
print("Join:", "-".join(["priya", "sharma"]))
print("Find 'sharma':", name.find("sharma"))
print("Count 'a':", name.count("a"))
print("Starts with priya?", name.strip().startswith("priya"))
print("Ends with ma?", name.strip().endswith("ma"))
print("Length:", len(name.strip()))