
def convert_len(ask_len,to_unit,from_unit):
    if from_unit=='gram':
        if to_unit=='kilogram':
         output=ask_len/1000
         return str(output)
        elif to_unit=='gram':
           output=ask_len
           return str(output)
        elif to_unit=='pound':
           output=ask_len/453.59237 
           return str(output)
        elif to_unit=='milligram':
           output=ask_len*1000
           return str(output)
        elif to_unit=='ounce':
           output=ask_len/ 28.349523125
           return str(output)
        else:
           return "invalid input"
    elif from_unit=='kilogram':
       if to_unit=='kilogram':
          output=ask_len
          return str(output)
       elif to_unit=='gram':
          output=ask_len*1000
          return str(output)
       elif to_unit=='pound':
          output=ask_len*2.20462
          return str(output)
       elif to_unit=='milligram':
           output=ask_len*1000000
           return str(output)
       elif to_unit=='ounce':
           output=ask_len*35.2739619
           return str(output)
       else:
          return 'invalid input'
    elif from_unit=='pound':
       if to_unit=='kilogram':
          output=ask_len/2.20462
          return str(output)
       elif to_unit=='pound':
          output=ask_len
          return str(output)
       elif to_unit=='gram':
          output=ask_len*453.592
          return str(output)
       elif to_unit=='milligram':
           output=ask_len*453592.37
           return str(output)
       elif to_unit=='ounce':
           output=ask_len*16
           return str(output)
       else:
          return "invaled input"
       
    elif from_unit=='milligram':
       if to_unit=='kilogram':
          output=ask_len/1000000
          return str(output)
       elif to_unit=='pound':
          output=ask_len/453592.37
          return str(output)
       elif to_unit=='gram':
          output=ask_len/1000
          return str(output)
       elif to_unit=='milligram':
           output=ask_len
           return str(output)
       elif to_unit=='ounce':
           output=ask_len*0.0000352739619
           return str(output)
       else:
        return "invalid input"
        
    elif from_unit=="ounce":
       if to_unit=='kilogram':
          output=ask_len*0.028349523125
          return str(output)
       elif to_unit=='pound':
          output=ask_len* 0.0625
          return str(output)
       elif to_unit=='gram':
          output=ask_len*28.349523125
          return str(output)
       elif to_unit=='milligram':
           output=ask_len* 28349.523125
           return str(output)
       elif to_unit=='ounce':
           output=ask_len
           return str(output)
    else:
       return "invalid input"
          

    
    
