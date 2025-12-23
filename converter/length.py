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
        elif to_unit=='Centimeter':
            output=ask_met*100
            return str(output)
        elif to_unit=='Millimeter':
            output=ask_met*1000
            return str(output)
        elif to_unit=='Inch':
            output=ask_met/0.0254
            return str(output)
        elif to_unit=='Foot':
            output=ask_met/0.3048
            return str(output)
        elif to_unit=='Yard':
            output=ask_met/0.9144
            return str(output)
        else:
           return "invalid input"
        
    elif from_unit=='Kilometer':
        if to_unit=='Meter':
            output=ask_met*1000
            return str(output)
        elif to_unit=='Kilometer':
            output=ask_met
            return str(output)
        elif to_unit=='Mile':
            output=ask_met/1.609344
            return str(output)
        elif to_unit=='Centimeter':
            output=ask_met*100000
            return str(output)
        elif to_unit=='Millimeter':
            output=ask_met*1000000
            return str(output)
        elif to_unit=='Inch':
            output=ask_met/0.0000254
            return str(output)
        elif to_unit=='Foot':
            output=ask_met/0.0003048
            return str(output)
        elif to_unit=='Yard':
            output=ask_met/0.0009144
            return str(output)
        else:
           return "invalid input"
        
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
        elif to_unit=='Centimeter':
            output=ask_met*160934.4
            return str(output)
        elif to_unit=='Millimeter':
            output=ask_met*1,609344
            return str(output)
        elif to_unit=='Inch':
            output=ask_met*63,360
            return str(output)
        elif to_unit=='Foot':
            output=ask_met*5,280
            return str(output)
        elif to_unit=='Yard':
            output=ask_met*1,760
            return str(output)
        else:
           return "invalid input"
        
    elif from_unit=='Centimeter':
         if to_unit=='Meter':
            output=ask_met/100
            return str(output)
         elif to_unit=='Kilometer':
            output=ask_met/100000
            return str(output)
         elif to_unit=='Mile':
            output=ask_met/160934.4
            return str(output)
         elif to_unit=='Centimeter':
            output=ask_met
            return str(output)
         elif to_unit=='Millimeter':
            output=ask_met*10
            return str(output)
         elif to_unit=='Inch':
            output=ask_met/2.54
            return str(output)
         elif to_unit=='Foot':
            output=ask_met/30.48
            return str(output)
         elif to_unit=='Yard':
            output=ask_met/91.44
            return str(output)
         else:
           return "invalid input"
         
    elif from_unit=='Millimeter':
         if to_unit=='Meter':
            output=ask_met/1000
            return str(output)
         elif to_unit=='Kilometer':
            output=ask_met/1000000
            return str(output)
         elif to_unit=='Mile':
            output=ask_met/1,609344
            return str(output)
         elif to_unit=='Centimeter':
            output=ask_met/10
            return str(output)
         elif to_unit=='Millimeter':
            output=ask_met
            return str(output)
         elif to_unit=='Inch':
            output=ask_met/25.4
            return str(output)
         elif to_unit=='Foot':
            output=ask_met/304.8
            return str(output)
         elif to_unit=='Yard':
            output=ask_met/914.4
            return str(output)
         else:
            return "invalid input"
         
    elif from_unit=='Inch':
         if to_unit=='Meter':
            output=ask_met*0.0254
            return str(output)
         elif to_unit=='Kilometer':
            output=ask_met*0.0000254
            return str(output)
         elif to_unit=='Mile':
            output=ask_met/63360
            return str(output)
         elif to_unit=='Centimeter':
            output=ask_met*2.54
            return str(output)
         elif to_unit=='Millimeter':
            output=ask_met*25.4
            return str(output)
         elif to_unit=='Inch':
            output=ask_met
            return str(output)
         elif to_unit=='Foot':
            output=ask_met/12
            return str(output)
         elif to_unit=='Yard':
            output=ask_met/36
            return str(output)
         else:
             return "invalid input"

         
    elif from_unit=='Foot':
         if to_unit=='Meter':
            output=ask_met*0.3048
            return str(output)
         elif to_unit=='Kilometer':
            output=ask_met*0.0003048
            return str(output)
         elif to_unit=='Mile':
            output=ask_met/5280
            return str(output)
         elif to_unit=='Centimeter':
            output=ask_met*30.48
            return str(output)
         elif to_unit=='Millimeter':
            output=ask_met*304.8
            return str(output)
         elif to_unit=='Inch':
            output=ask_met/12
            return str(output)
         elif to_unit=='Foot':
            output=ask_met
            return str(output)
         elif to_unit=='Yard':
            output=ask_met/3
            return str(output)
         else:
             return "invalid input"
         

    elif from_unit=='Yard':
         if to_unit=='Meter':
            output=ask_met*0.9144
            return str(output)
         elif to_unit=='Kilometer':
            output=ask_met*0.0009144
            return str(output)
         elif to_unit=='Mile':
            output=ask_met/1760
            return str(output)
         elif to_unit=='Centimeter':
            output=ask_met*91.44
            return str(output)
         elif to_unit=='Millimeter':
            output=ask_met*914.4
            return str(output)
         elif to_unit=='Inch':
            output=ask_met/36
            return str(output)
         elif to_unit=='Foot':
            output=ask_met/3
            return str(output)
         elif to_unit=='Yard':
            output=ask_met
            return str(output)
         else:
            return "invalid input"

         
        

    
        

        
        

    
         
        

    
        

    