F1 = ['Max Verstappen 33 Red Bull', 'Lewis Hamilton 44 Mercedes Yeet!', 'Valtteri Bottas 77 Mercedes',
      'Lando Norris 04 Mclaren', 'Sergio Perez 11 Red Bull', 'Charles Leclerc 16 Ferrari', 'Carlos Sainz 55 Ferrari',
      'Daniel Ricciardo 03 Mclaren', 'Pierre Gasly 10 AlphaTauri', 'Fernando Alonso 14 Alpine', 'Esteban Ocon 31 Alpine',
      'Sebastian Vettel 05 Aston Martin', 'Lance Stroll 18 Aston Martin', 'Yuki Sonoda 22 AlhaTauri',
      'George Russell 63 Williams', 'Nicholas latifi 06 Williams', 'Kimi Raikkonen 07 Alpha Romeo', 'Antonio Giovinazzi 07 Alpha Romeo'
      'Mick Schumacher 47 Haas', 'Nikita Mazepin 09 Haas']
"""
Sorted: 
F1 is a list 
Key=lambda we use lambda for calling anonymous function
key=lambda s: s.split(" ") This function takes a string s and divides it into each blank space. 
[1]: This is the index value of each string in the list and according to this index value the strings will sort in the list.
"""
f1 = sorted(F1, key=lambda s: s.split(" ")[1])
print('2021 F1 Drivers - Alphabetically')
print('================================')
for item in f1:
      print(item)

print('2021 F1 Drivers - Numerically')
print('================================')
f1_1 = sorted(F1, key=lambda s: s.split()[2])
for item in f1_1:
      print(item)
