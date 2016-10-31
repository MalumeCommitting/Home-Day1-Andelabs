def data_type(_arg_):

	if type(_arg_) == str:
		return len(_arg_)

	if type(_arg_) == None:
		return 'no value'

	elif type(_arg_) == bool:
		return _arg_
		
	elif type(_arg_) == int:
		if _arg_ < 100:
			return 'less than 100'
			
		elif _arg_ == 100:
			return 'equal to 100'
			
		else:
			return 'more than 100'
			
	elif type(_arg_) == list:
		if len(_arg_) < 3:
			return None
		else:
			return _arg_[2]

print (data_type(_arg_ = False))