def convert_tem(ask_tem,from_unit,to_unit):
    if from_unit=='celsius':
        if to_unit=='celsius':
            output=ask_tem
            return str(output)
        elif to_unit=='fahrenheit':
            output=(ask_tem*9/5)+32
            return str(output)
        elif to_unit=='kelvin':
            output=ask_tem+ 273.15
            return str(output)
        else:
            return "invaled input"
    elif from_unit=='fahrenheit':
        if to_unit=='celsius':
            output=(ask_tem-32)*5/9
            return str(output)
        elif to_unit=='fahrenheit':
            output=ask_tem
            return str(output)
        elif to_unit=='kelvin':
            output=(ask_tem-32)*5/9+273.15
            return str(output)
        else:
            return 'invaled input'
    elif from_unit=='kelvin':
        if to_unit=='celsius':
            output=ask_tem-273.15
            return str(output)
        elif to_unit=='fahrenheit':
            output=(ask_tem-273.15)*9/5+32
            return str(output)
        elif to_unit=='kelvin':
            output=ask_tem
            return str(output)
        else:
            return "invalied input"
    else:
        return "invaled input"