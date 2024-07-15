# import random library
import random

# defining mostly empty variobuls
temperatures = []
good_days_count = 0
days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
good_days_list = []
above_avg = []

# adding to good day list/count
for i in range(7):
	temperatures.append(random.randint(26, 40))

	if temperatures[i] % 2 == 0:
		good_days_count += 1

		# makes it add to the list of good days the day of the week based on the [i] = index
		good_days_list.append(days_of_the_week[i])

#hi and low
highest_temp = max(temperatures)
HI = temperatures.index(highest_temp)
highest_temp_day = days_of_the_week[HI]

lowest_temp = min(temperatures)
LI = temperatures.index(lowest_temp)
lowest_temp_day = days_of_the_week[LI]

# average temp
AVG = sum(temperatures)/len(temperatures)
for k in range(7):
	if temperatures[k] > AVG:
		ABV_AVG = days_of_the_week[k]
		above_avg.append(ABV_AVG)


# final report
print("Final Report: \n")
print("the temperatures this week are: \n")
for d in range(7):
	temp=temperatures[d]
	day=days_of_the_week[d]
	print("on", day, "it was:", temp, "degress\n")

print("the amount of good days for shelly is: ", good_days_count, "\n")
print("the list of good days: ", good_days_list, "\n")

print("the lowest temp is: ", lowest_temp)
print("the day with the lowest temp is: ", lowest_temp_day)
print("the highest temp is: ", highest_temp)
print("the day with the highest temp is: ", highest_temp_day,"\n")

print("the average temperature this week is: ",int(AVG))
print("the days with temperatures above average are: ", above_avg)
