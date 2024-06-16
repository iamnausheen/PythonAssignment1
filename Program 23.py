conversion = input("Farenheit/F to Celcius/C or Celcius/C to Farenheit/F : ")
temperature = int(input("Enter temperature: "))

if (conversion.lower() == "celcius to farenheit" or conversion.lower() == "c to f"):
    result = (temperature*(9/5)) + 32
    print("Temperature from {} : {}".format(conversion, result))
elif (conversion.lower() == "farenheit to celcius" or "f to c"):
    result = (temperature - 32)*(5/9)
    print("Temperature from {} : {}".format(conversion, result))
else :
    print("INVALID")