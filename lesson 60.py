# dictionary comprehension = create dictionaries using an exprression
#                            can replace for loops and certain lambda function
#
#dictionary = {key : expression for (key,value) in iterable}
#dictionary = {key : expression for (key,value) in iterable if conditional}
#dictionary = {key : (if/else) for (key,value) in iterable}
#dictionary = {key : function(value) for (key,value) in iterable}
#----------------------------------------------------------------------------------------------------------------------

cities_in_F = {'New York':32, 'Boston': 75, 'Los Angeles':100, 'Chicago': 50}

cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

#----------------------------------------------------------------------------------------------------------------------

weather = {'New York': "snowing", 'Boston':"sunny",'Los Angeles':"sunny",'Los Angeles': "sunny", 'Chicago':"cloudy"}

sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}

print(sunny_weather)

#----------------------------------------------------------------------------------------------------------------------
cities = {'New York':32, 'Boston': 75, 'Los Angeles':100, 'Chicago': 50}

desc_cities = {key : ("Warm" if  value >=40 else "cold") for (key,value) in cities.items()}
print(desc_cities)

#----------------------------------------------------------------------------------------------------------------------
def check_temp(value):
    if value >= 70:
          return "Hot"
    elif 69 >= value >=40:
          return "Warm"
    else:
          return "Cold"

cities_4 = {'New York':32, 'Boston': 75, 'Los Angeles':100, 'Chicago': 50}

desc_cities_4 = {key : check_temp(value) for (key,value) in cities_4.items()}
print(desc_cities_4)

