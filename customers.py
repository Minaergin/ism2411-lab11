
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
