
def convert_len(ask_len,to_unit,from_unit):
    if from_unit=='gram':
        if to_unit=='kilogram':
         output=ask_len/1000
         return str(output)
        elif to_unit=='gram':
           output=ask_len
           return str(output)
        elif to_unit=='pound':
           output=ask_len/453.592
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
          output=ask_len/0.453592
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
       else:
          return "invaled input"
    else:
       return "invalid input"
          

    
    
