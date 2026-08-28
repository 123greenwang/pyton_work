def describe_pet(animal_type,pet_name='poter'):
    "显示宠物信息"
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")
describe_pet('hamster','harry')
describe_pet(animal_type='dog')
