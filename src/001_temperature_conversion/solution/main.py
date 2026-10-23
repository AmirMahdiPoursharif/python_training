from .convertor import to_celsius, to_fahrenheit

def main():
    print("Hello welcome to temperature conversion app")
    print("we can convert Temperature to Fahrenheit or Celsius ")

    # دریافت ورودی های مورد نیاز از کاربر
    temperature : int = int(input("Enter Temperature: "))

    unit : int = int(input("please enter your temperature unit [Celsius/Fahrenheit] 1 / 2: "))

    # بررسی واحد ورودی کاربر و انجام عملیات متناسب روی آن

    match unit:
        case 1:
            return to_fahrenheit(temperature)
        case 2:
            return to_celsius(temperature)
        case _:
            # مقاومت در مقابل وارد کردن ورودی نامعتبر
            return "please enter a valid unit"

    # راه حل دیگر

    # if unit == 1:
    #     return to_fahrenheit(temperature)
    # elif unit == 2:
    #     return to_celsius(temperature)
    # else:
    #     return "please enter a valid unit"


if __name__ == "__main__":
    print(main())