class Car:
    '模拟汽车'
    def __init__(self,make,model,year):
        '初始化'
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        '返回规范信息'
        long_name=f'{self.year} {self.make} {self.model}'
        return long_name.title()
    def read_odometer(self):
        "行驶里程消息"
        print(f'this car has {self.odometer_reading} mile on it')
my_new_car=Car('md','a4','2026')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23
my_new_car.read_odometer()
