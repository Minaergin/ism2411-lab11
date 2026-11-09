
# ISM2411 Lab 11 - Customer Dictionary & Lookup
# Name: Mina Ergin

# Reflection Question 1:
# I would use .get() when looking up information that
# might not exist, such as a customer's phone number
# or email address. I would use bracket notation when
# the information is required and should always exist.
# My rule of thumb is to use .get() for optional fields
# and brackets for required fields.

# Reflection Question 2:
# Building a summary dictionary reminds me of using
# PivotTables in Excel to organize and total sales
# by categories such as region. Python can be more
# useful for large datasets because it can automate
# calculations and handle large amounts of data
# without manually updating spreadsheets.



# Exercise 1 - One Customer

print("\nExercise 1")

customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 1500
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2 - Update and Add

print("\nExercise 2")

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)



# Exercise 3 - Safe Lookup

print("\nExercise 3")

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")



# Exercise 4 - Iterate

print("\nExercise 4")

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only returns the keys.
# With .items(), the loop returns both keys and values.

for key in customer:
    print(key)



# Exercise 5 - Lookup Table

print("\nExercise 5")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)

purchase_price = 200
final_price = purchase_price * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")



# Exercise 6 - List of Dictionaries

print("\nExercise 6")

customers = [
    customer,
    {
        "name": "Bob",
        "tier": "silver",
        "ytd_spend": 800
    },
    {
        "name": "Charlie",
        "tier": "bronze",
        "ytd_spend": 300
    }
]

for person in customers:
    name = person["name"]
    tier = person["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(
        f"{name} - Tier: {tier}, "
        f"Discount: ${discount_amount:.2f}"
    )
