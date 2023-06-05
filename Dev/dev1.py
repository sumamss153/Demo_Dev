import datetime
mynow = datetime.datetime.now()
mynumber = 15
mytext = "Sumam"
myfloat = 15.3
print("The date and time is", mynow, mynumber, mytext, myfloat)
print(type(mynumber), type(mytext), type(myfloat))

montemp = [9.1,8.8,7.5,9.1] #list
list_ranges = list(range(1,10,2))
print(montemp, list_ranges)

mysum = sum(montemp) #function dir(__builtins__)
mylen = len(montemp) 
mymean = mysum / mylen
print(mysum, mylen, mymean, montemp.count(9.1)) #method dir(list) & help(list.count)

student_grades = {"Jack": 9.1, "Jill": 8.8, "Tom": 7.5, "Jerry": 9.1} #dictionary

print(student_grades.values(), sum(student_grades.values()) / len(student_grades)) #calculate mean

montemp2 = (1,2,3) #tuple
print(montemp2)

print(montemp.index(9.1))
print(montemp.index(9.1,2))

print(montemp[1], montemp[1:3], montemp[:2], montemp[3:], montemp[-1], montemp[-3:], montemp[-3:-1]) #slices
print(student_grades["Tom"])

#user defined function
def mean(value):
    print("user defined function", type(value))
    if type(value) == dict: #isinstance(value, dict)
        the_mean = sum(value.values()) / len(value)
    elif isinstance(value, list):
        the_mean = sum(value) / len(value)   
    else:
        the_mean = value
    return the_mean

print(mean([1,2,5])) #calling the function
print(mean(student_grades))
print(mean(10))
print(type(mean), type(sum))

def weather_condition(temperature):
    if temperature > 25:
        return "It's Hot"
    elif 25 >= temperature >= 15:
        return "It's Warm"
    else:
        return "It's Cold"

user_input = float(10) #user input capture

print(weather_condition(user_input))

user_input = 'SSS'
message = "Hello %s!" % user_input
print(message)
when = "today"
message = f"Hello {user_input}. What's up {when}?" #Python 3.6+
print(message)

for temperature in montemp:
    print(round(temperature))
    print("Done!")

for letter in 'hello':
    print(letter.title())
