person={'name':'zhangsan','age':18}
print(person.get('name'))
print(person['age'])
person['gender']='male'
print(person['gender'])
del person['age']
print(person)
print(person.get('age'))  # This will return None since 'age' has been deleted  None
print(person.get('age', 'Age not found'))  # This will return 'Age not found' since 'age' has been deleted  

