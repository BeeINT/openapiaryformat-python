from beeint import Apiary

a = Apiary("My First Hive")
print a.name
a.name = "test"
print a.name



b = Apiary(enable_history=True)
b.name = "The New Name"
b.dumps()
print b