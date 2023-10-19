my_string: str = '''Hello
World!'''
print(my_string)
name:str = "Umair khan "
fname:str = "Muhammad Sadiq"
education:str = "Bscs"
age : int = 25
card : str = "Piaic Student Card \nStudent Name: " + name  +  "\nage" + str(age)

print(card)
print(3 + \
      2 + \
        1)

card2 : str = """ 
piaic student card
student name: {}
full name : {}
education : {}
student age:  {}
""".format(name,fname,education,age)
print(card2)

card3:str = f"""
Name: {name}
Full Name: {fname}
education: {education}
age: {age}
"""
print(card3)

card4:str = """
name : {a}
fullname: {b}
education: {c}
age: {d}
""".format(a=name,b=fname,c=education,d=age)
print(card4)