test = [5, 1, 3, 8, 12, 10]

max_value = 0

for value in test:
    if max_value < value:
        max_value = value

print(f"Max : {max_value}")
assert max_value == 12

# - build dictionary like this [{"hero_name" : "Axe", "attack_dmg": 150}, {"hero_name" : "Sniper", "attack_dmg": 150}]
# by reading csv - use For loop
# - sorted dictionary by attach_dmg (Reverse - ကြီးစဥ် ငယ်လိုက်)
# - get the first item
