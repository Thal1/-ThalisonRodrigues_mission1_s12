from MeasurementConverter import MeasurementConverter
from conversou_medidas import conversou_medidas

print('''
[1]. Centimeters to Meters
[2]. Meters to Centimeters
[3]. Celsius to Fahrenheit
[4]. Fahrenheit to Celsius
''')

choice = input('Choose an option: ')
value = float(input('Type a value: '))

if choice == '1':
    result = MeasurementConverter.centimeters_to_meters(value)
elif choice == '2':
    result = MeasurementConverter.meters_to_centimeters(value)
elif choice == '3':
    result = conversou_medidas.celsius_to_fahrenheit(value)
else:
    result = conversou_medidas.fahrenheit_to_celsius(value)
    
print('Result:', result)