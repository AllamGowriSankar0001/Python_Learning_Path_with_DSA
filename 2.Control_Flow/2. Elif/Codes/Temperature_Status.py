
# Write a program using elif to display temperature status:
# Above 40 → Very Hot
# 30–40 → Hot
# 20–29 → Warm
# 10–19 → Cool
# Below 10 → Cold
temperature = float(input("Enter the temperature: "))

if temperature > 40:
    print("Very Hot")
elif 30 <= temperature <= 40:
    print("Hot")
elif 20 <= temperature <= 29:
    print("Warm")
elif 10 <= temperature <= 19:
    print("Cool")
else:
    print("Cold")
