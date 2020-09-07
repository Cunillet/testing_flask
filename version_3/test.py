def greetings(name, times):
	try:
		if (times > 0):
			for x in range(times):
				print('Hello {}'.format(name))
		else:
			raise
	except:
		print('error, number of times need to be positive')

if __name__ == '__main__':
	greetings('Oriol', -1)