q = [
    "Q:1) Who is the father of cell?",
    "Q:2) At which place can you find edible food?",
    "Q:3) What is the % of carbon in mild steel?",
    "Q:4) Who is the current president of India?",
    "Q:5) In which compound's terms is hardness of water measured?"
]

options = [
    ["a) Robert Hooke", "b) Plancks", "c) Albert Einstein", "d) None of these"],
    ["a) Yardley", "b) Mc Donalds", "c) Louis Vuitton", "d) None of these"],
    ["a) 15-30%", "b) 1.5-3%", "c) 0.15-0.3%", "d) None of these"],
    ["a) Droupadi Murmu", "b) Ram Nath Kovind", "c) Pranab Mukherjee", "d) None of these"],
    ["a) MgCO3", "b) CaSO4", "c) MgSO4", "d) CaCO3"]
]

answers = ["a", "b", "c", "a", "d"]

score = 0

for i in range(5):
    print("\n" + q[i])
    for opt in options[i]:
        print(opt)
    user = input("Your answer (a/b/c/d): ").strip().lower()
    if user == answers[i]:
        print("Correct! ✓")
        score += 1
    else:
        print(f"Wrong! Correct answer was: {answers[i]}")

print(f"\nYour score: {score}/5")
