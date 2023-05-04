import json



with open('cities.json') as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    print("Type:", type(data))
 
    # Print the data of dictionary
    print("\nPeople1:", data['people1'])
    print("\nPeople2:", data['people2'])



# with open('cities.json') as f:
	# print(type(f))
	# data = loads(f)
	# print(data)



