def checkio(number):
	line = "";
	if number % 3 == 0 and number % 5 == 0:
		return "Fizz Buzz";
	if number % 3 == 0:
		line += "Fizz";
	if number % 5 == 0:
		line += "Buzz";

	if line == '':
		line = str(number);
		return line;
	else:
		return line;
