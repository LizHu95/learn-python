from car import ECar

tesla=ECar('tesla','model s',2016,90)
print(tesla.get_descriptive_name())
tesla.read_odometer()
tesla.update_odometer(150)
tesla.read_odometer()
tesla.update_odometer(50)
tesla.read_odometer()
tesla.increment_odometer(50)
tesla.read_odometer()
tesla.describe_battery()
tesla.battery.describe_battery()