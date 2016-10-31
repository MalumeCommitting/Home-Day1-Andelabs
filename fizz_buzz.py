def fizz_buzz(data):
  
   if data % 3 == 0 and data % 5 == 0:
    return 'FizzBuzz'

   elif data % 3 == 0:
    return 'Fizz'
  
   elif data % 5 == 0:
    return 'Buzz'
  
   else:
     return data
