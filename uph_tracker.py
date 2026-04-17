associates = [
{"id": "A123", "uph": 85, "volume": 300, "idle": 15},
{"id": "B456", "uph": 72, "volume": 250, "idle": 30},
{"id": "C789", "uph": 95, "volume": 400, "idle": 10},
]

def performance_score(a):
return a["uph"] - (a["idle"] * 0.5)

def performance_flag(score):
if score >= 85:
return "Top Performer"
elif score >= 70:
return "Meets Expectations"
else:
return "Needs Coaching"

for a in associates:
score = performance_score(a)
status = performance_flag(score)
print(f"ID: {a['id']} | Score: {score} | Status: {status}")
