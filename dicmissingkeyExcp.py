country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}


print (country_code.get('India','Not Found'))
print (country_code.get('Japan','Not Found'))



country_code.setdefault('Japan', 'Not Present') 
 
print(country_code['Japan'])
