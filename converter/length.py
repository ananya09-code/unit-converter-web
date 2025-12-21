def convert_met(ask_met,from_unit,to_unit):
    if from_unit=='Meter':
        if to_unit=='Meter':
            output=ask_met
            return str(output)
        elif to_unit=='Kilometer':
            output=ask_met/1000
            return str(output)
        elif to_unit=='Mile':
            output=ask_met/1609.344
            return str(output)
        else:
            return "invaid input"
    elif from_unit=='Kilometer':
        if to_unit=='Meter':
            output=ask_met*1000
            return str(output)
        elif to_unit=='Kilometer':
            output=ask_met
            return str(output)
        elif to_unit=='Mile':
            output=ask_met*0.621371
            return str(output)
        else:
            return "invialed input"
    elif from_unit=='Mile':
        if to_unit=='Meter':
            output=ask_met*1609.344
            return str(output)
        elif to_unit=='Kilometer':
            output=ask_met*1.609344
            return str(output)
        elif to_unit=='Mile':
            output=ask_met
            return str(output)
    else:
        return "invaled input"
    