# --------------
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry', 'Corinna Cortes']
new_class=class_1+class_2
print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
for x in courses.values():
    print(x)
total=0
for x in courses.values():
    total=total+x
print(total)
percentage=(total/500)*100
print(percentage)
mathematics={
    'Geoffrey Hinton':78,
    'Andrew Ng':95,
    'Sebastian Raschka':65,
    'Yoshua Bengio':50,
    'Hilary Mason':70,
    'Carla Gentry':66,
    'Corinna Cortes':75}
topper=max(mathematics,key=mathematics.get)
print(topper)
x=topper.split(" ")
first_name=x[0]
last_name=x[1]
print(first_name)
print(last_name)
full_name=last_name+" "+first_name
certificate_name=full_name.upper()
print(certificate_name)



