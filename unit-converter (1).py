def get_conversion_factors():
    return {
        'length': {
            'm to km': 0.001,
            'km to m': 1000,
            'feet to meters': 0.3048,
            'meters to feet': 3.28084,
            'inches to cm': 2.54,
            'cm to inches': 0.393701
        },
        'weight': {
            'kg to lbs': 2.20462,
            'lbs to kg': 0.453592,
            'g to oz': 0.035274,
            'oz to g': 28.3495
        },
        'temperature': {
            'C to F': lambda x: (x * 9/5) + 32,
            'F to C': lambda x: (x - 32) * 5/9
        }
    }

def show_available_conversions(conversions):
    print("\nAvailable conversions:")
    for category, units in conversions.items():
        print(f"\n{category.capitalize()}:")
        for conversion in units.keys():
            print(f"  - {conversion}")

def get_user_input(conversions):
    show_available_conversions(conversions)
    
    while True:
        category = input("\nEnter category (length/weight/temperature): ").lower()
        if category in conversions:
            break
        print("Invalid category. Please try again.")

    print(f"\nAvailable conversions for {category}:")
    for conversion in conversions[category].keys():
        print(f"- {conversion}")

    while True:
        conversion_type = input("\nEnter conversion type (e.g., 'm to km'): ")
        if conversion_type in conversions[category]:
            break
        print("Invalid conversion type. Please try again.")

    while True:
        try:
            value = float(input("Enter value to convert: "))
            return category, conversion_type, value
        except ValueError:
            print("Please enter a valid number.")

def convert_value(category, conversion_type, value, conversions):
    conversion_factor = conversions[category][conversion_type]
    if isinstance(conversion_factor, float):
        return value * conversion_factor
    else:  # For temperature conversions that use lambda functions
        return conversion_factor(value)

def main():
    print("Welcome to Unit Converter!")
    conversions = get_conversion_factors()
    
    while True:
        category, conversion_type, value = get_user_input(conversions)
        result = convert_value(category, conversion_type, value, conversions)
        
        print(f"\nResult: {value} {conversion_type.split(' to ')[0]} = {result:.2f} {conversion_type.split(' to ')[1]}")
        
        if input("\nWould you like to do another conversion? (yes/no): ").lower() != 'yes':
            break
    
    print("Thank you for using Unit Converter!")

if __name__ == "__main__":
    main()
