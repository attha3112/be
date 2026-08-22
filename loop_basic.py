users = [
    {'nama' : 'budi', 'role' : 'admin'},
    {'nama' : 'siti', 'role' : 'user'},
    {'nama' : 'leo', 'role' : 'user'},
    {'nama' : 'kevin', 'role' : 'admin'}
]

user_biasa = []

for u in users:
    if u['role'] == 'admin':
        user_biasa.append(u)

print(user_biasa)