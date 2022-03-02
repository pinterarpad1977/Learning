import json
import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = json.loads(response.text)
# response.text contains json data - todos will be a list of dictionaries

# we want to compute which user completed the most todos.
# We create a dictionary to keep track
todos_by_user = {}
for todo in todos:
    if todo['completed']:
        try:
            todos_by_user[todo['userId']] += 1
        except KeyError:
            todos_by_user[todo['userId']] = 1
# *******************************************************
# ****** my solution cannot handle ties *******
# max_task=0
# top_user=''
# for k,v in todos_by_user.items():
#     if todos_by_user[k]>max_task:
#         max_task=v
#         top_user=k

sorted_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# This creates a list of tuples sorted descending by the values in the dict

max_complete = sorted_users[0][1]  # takes the 1st tuple 2nd element
top_users = []
for user, num_completed in sorted_users:
    if num_completed < max_complete:
        break
    else:
        top_users.append(str(user))

# filter the original json to show only the top users and their todos
# *********** My solution **************
top_list = []
for k in todos:
    if k['completed'] and k['userId'] == 5 or k['completed'] and k['userId'] == 10:
        top_list.append(k)
    else:
        continue

jsn = json.dumps(top_list, indent=4)


# ******* Real Python soultion **************
def keep(todo):
    """ This is to create a filter parameter"""
    is_complete = todo['completed']
    has_max_count = str(todo['userId']) in top_users
    return is_complete and has_max_count


with open('filtered_data.json', 'w') as data_file:
    filtered_todos = list(filter(keep, todos))
    # this creates a filter object which is converted to a list
    json.dump(filtered_todos, data_file, indent=2)



