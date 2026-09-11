
with open(r'C:\file4.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()


participants = []
for line in lines:
    parts = line.strip().split()
    name = ' '.join(parts[:-1])
    score = int(parts[-1])
    participants.append((name, score))


max_score = max(p[1] for p in participants)


prize_score = max(p[1] for p in participants if p[1] < max_score)


for name, score in participants:
    if score == prize_score:
        print(f"Призер: {name}, баллы: {score}")
        break
