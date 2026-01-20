# Generate 1000 random votes for 4 parties A, B, C, and D
# Find and print the results (%) of each party and the Winner.
import random

votes = []
parties = ['A', 'B', 'C', 'D']

for i in range(1000):
    votes.append(random.choice(parties))


results = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0
}

for party in parties:
    results[party] = votes.count(party)

max = 0
max_party = None
for party in results:
    r = results[party] * 100 / 1000
    print(f"{party}: {r}%")
    if r > max:
        max = r
        max_party = party

print(f"WINNER: {max_party}")


