class Car():
    """mock car"""
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+" "+str(self.make)+" "+str(self.model)
        return long_name.title()
    
    def read_odometer(self):
        print("This car has",str(self.odometer_reading),"miles on it.")

    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("Your can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles


class ECar(Car):
    """mock electric car"""
    def __init__(self, make, model, year,size=70):
        super().__init__(make, model, year)
        self.battery_size=size
        self.battery=Battery(size)

    def read_odometer(self):
        print("This electric car has",str(self.odometer_reading),"miles on it.")
        
    def describe_battery(self):
        print("This car has a",str(self.battery_size)+"-kWh battery.")


class Battery():
    """mock battery"""
    def __init__(self,size):
         self.battery_size=size
         
    def describe_battery(self):
        print("This car has a",str(self.battery_size)+"-kWh battery.")



    