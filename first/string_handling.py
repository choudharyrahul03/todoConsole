# string handling in python

"""
this is python
string handling
demo
"""
s1 ="python is very powerful language"
print(s1)
print(type(s1))
print(s1[2]) # third char of string
print(s1[3:])
print(s1[3:6])
print(s1[:3])

s2 ="python"
print(s2)
print(s2[1:3])
print(s2[-2])
print(s2[-1])
print(s2[:2])
print(s2[-2:])
print(s1[::-1])
print(s1[::-2])
print(s1[::2])
print(s1+s1)
print(s1*3)
print(s1.capitalize())
print(s1.istitle())
print(s1.title())
print(s1.upper())
print(s1.count("p"))
print(s1.endswith("age"))
print(s1.startswith("p"))
print(s1.startswith("x"))
############################

s3 = "    this is python lab      "
print(s3)
print(s3.lstrip())
print(s3.rstrip())
print(s3.strip())
print(len(s1))
print(len(s2))
print(len(s3))