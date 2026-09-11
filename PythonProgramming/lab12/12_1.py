ask = int(input())
women_and_children = []
men = []
captain = None
if ask < 1 or ask > 100:
    print("Чет не то")
for i in range(ask):
    name, status = input().split()
    if status == "woman" or status == "child":
        women_and_children.append(name)
    elif status == "man":
        men.append(name)
    elif status == "captain":
        captain=name

escape_crew = women_and_children+men
if captain:
    escape_crew.append(captain)
print("\n".join(escape_crew))