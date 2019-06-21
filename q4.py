import copy


a = [1, 2, 3]
a_fake = a
b = copy.copy(a)
c = a * 1

a_fake.append(4)

print(a)
print(a_fake)
print(b)
print(c)
print(id(a))
print(id(a_fake))
print(id(b))
print(id(c))