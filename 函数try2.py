def get_formatted_name(first_name,last_name,middle_name=''):
    "返回标准模式的姓名"
    if middle_name:
        full_name=f'{first_name} {middle_name} {last_name}'
    else:
        full_name=f'{first_name} {last_name}'
    return full_name

def build_person(first_name,last_name,age=None):
    "返回一个字典，包括一个人的信息"
    
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person

musician=get_formatted_name('jimi','hendrix')
print(musician)
m2=get_formatted_name('john','hooker','lee')
print(m2)
m3=build_person('jimi','hendrix',age=27)
print(m3)
