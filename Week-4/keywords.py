'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>
def welcome_message(user_name=None,place=None,):
    if user_name != None:
        user_name = "," + user_name + ","

    if place != None:
        place = "to "+ place
    return("Hello "+ user_name + " and welcome "+ place)

# Create a function called list_average()
# without using any libraries to do the maths for you 
# (the point of this exercise is to practice interacting 
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list

def list_average(the_list,avg_type="mean"):
    if avg_type == "mode":
        ordered_list = set(the_list)
        for number in ordered_list:
            the_list.count(number)
        return("list_mode")
        
    elif avg_type == "median":
        sorted_list = sorted(the_list)
        return(the_list[int(len(sorted_list)/2)])
    
    elif avg_type == "mean":
        list_mean=((sum(the_list))/len(the_list))
        return(list_mean)

