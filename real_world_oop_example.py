class Car(object):
  
  def __init__(self, name = 'General', model = 'GM', type_of_car = None, speed = 0):
    self.name = name
    self.model = model
    self.type_of_car = type_of_car
    self.speed = speed
    
    
    if self.name in ['Porshe', 'Koenigsegg']:
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4
    
    if self.type_of_car == 'trailer':
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4
      
  def is_saloon(self):
    if self.type_of_car is not 'trailer':
    	self.type_of_car == 'saloon'
    	return True
    return False
  
  def drive(self, moving_speed):
    if moving_speed == 3:
      self.speed = 1000
    elif moving_speed == 7:
      self.speed = 77
    
    return self
