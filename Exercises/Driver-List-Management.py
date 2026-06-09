"""
Driver List Management

A simple Python program that simulates a racing leaderboard while
demonstrating common list operations such as updating, adding,
removing, moving, and displaying elements.
"""

# Starting grid
drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George", "Lando"]

print("🏁 Starting Grid")
print(drivers)

# Correct a misspelled driver's name
drivers[2] = "Valtteri"

# Add a late arrival to the race
drivers.append("Esteban")

# Add another group of competitors
additional_drivers = ["Blue", "Elton", "Colt"]
drivers.extend(additional_drivers)

# Remove Colt after a crash
drivers.pop()

# Remove the race leader after an incident
drivers.pop(0)

# Move the new leader to the back of the pack
leader = drivers.pop(0)
drivers.append(leader)

# Remove Blue from the race
drivers.remove("Blue")

# Elton makes a charge through the field
drivers.remove("Elton")
drivers.insert(2, "Elton")

# Create the podium
podium = drivers[:3]

print("\n🥇 Podium Finishers")
for position, driver in enumerate(podium, start=1):
    print(f"{position}. {driver}")

print("\n📊 Final Leaderboard")
for position, driver in enumerate(drivers, start=1):
    print(f"{position}. {driver}")
