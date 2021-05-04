"""
File: weather_master.py
Name: 林坤毅 Jordan
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -100
# This number controls when "Weather Master 4.0" will end.


def main():
	"""
	This program will will give a weather report containing highest, lowest, average temperatures and total days below
	16 degrees Celsius.
	1. It will check if user has entered EXIT first.
		If enter EXIT, this program will end.
		If enter a temperature other than EXIT, it will keep running.
	2. User will enter the second temperature, and this program will check that number is EXIT or not
		If enter EXIT, this program will show the weather report containing only one data.
		If enter a temperature other than EXIT, it will keep running.
	3. User will enter the third temperature, and this program will check that number is EXIT or not
		If enter EXIT, this program will show the weather report containing two data.
		If enter a temperature other than EXIT, it will keep storing data and go to while loop until user enter EXIT.
	"""

	print('stanCode \"Weather Master 4.0\"!')
	temperature = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)?'))

	if temperature == EXIT:
		print('No temperatures were entered.')

	else:
		temperature2 = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)?'))
		# The second temperature was entered.
		if temperature2 == EXIT:
			# The second temperature is EXIT, so the following will only print the information for temperature one.
			print('Highest temperature = ' + str(temperature))
			print('Lowest temperature = ' + str(temperature))
			print('Average = ' + str(float(temperature)))
			if temperature < 16:
				print('1 cold day(s)')
			else:
				print('0 cold day(s)')

		else:
			# The second temperature is not EXIT.

			if temperature > temperature2:
				maximum = temperature
				minimum = temperature2
			elif temperature < temperature2:
				maximum = temperature2
				minimum = temperature
			else:
				maximum = temperature2
				minimum = temperature2
			# Compare two temperatures and assign maximum and minimum to them.

			n = 2
			# Total days that have been entered.
			total = temperature + temperature2
			# The sum of the first two temperature.
			if temperature > 16 and temperature2 > 16:
				colddays = 0
			elif temperature > 16 and temperature2 == 16:
				colddays = 0
			elif temperature > 16 and temperature2 < 16:
				colddays = 1

			elif temperature == 16 and temperature2 > 16:
				colddays = 0
			elif temperature == 16 and temperature2 == 16:
				colddays = 0
			elif temperature == 16 and temperature2 < 16:
				colddays = 1

			elif temperature < 16 and temperature2 == 16:
				colddays = 1
			elif temperature < 16 and temperature2 > 16:
				colddays = 1
			else:
				colddays = 2
				# temperature < 16 and temperature2 < 16
			# Low temperature alarm.
			# There are three conditions for each temperature, so there are 9 conditions in total (3x3).

			while True:
				temperature3 = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)?'))
				if temperature3 == EXIT:
					print('Highest temperature = ' + str(maximum))
					print('Lowest temperature = ' + str(minimum))
					print('Average = ' + str(float(total/n)))
					print(str(colddays) + ' cold day(s)')
					break
				# The third temperature was EXIT, this program will compare first two temperatures.

				else:
					# The third temperature was not EXIT, so it will keep comparing the temperature user enter.

					n += 1
					# Total days will add one day, if enter this 'else' part.

					if temperature3 > maximum:
						maximum = temperature3
						# Maximum is reassigned.
						# Minimum value is unchanged.
					elif temperature3 < minimum:
						minimum = temperature3
						# Minimum is reassigned.
						# Maximum value is unchanged.
					else:
						pass
					# Reassign the highest and lowest temperatures.

					if temperature3 < 16:
						colddays += 1
					# Reassign the colddays if the temperature is lower than 16

					total += temperature3
					# Reassign total temperature if the temperature user entered is not EXIT.


				###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
