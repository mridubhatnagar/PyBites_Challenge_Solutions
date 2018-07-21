import sys

class HouseInventory(object):

	def __init__(self, house_structure):

		self.house_structure = house_structure
        

	def get_format_output(self):
		"""
		Format the output.
		Based on contents in 
		dictionary
		"""
		for room, item_list in self.house_structure.items():

			print("Room: {}".format(room))

			for item, element in item_list.items():

				print(item + ':' + ' ' + element)

			print("======================================")


	def __len__(self):

		return len(self.house_structure)


	def __getitem__(self, key):

	    for k,v in self.house_structure[key].items():
	        print(k,v)


class HouseInventoryCost:

	def get_total_item_cost(self, **kwargs):

		total_cost = 0

		for key, value in kwargs.items():
			for cost in value.values():
				total_cost = total_cost + int(cost)

		return total_cost


def main():

	global data_dictionary

	room_list = str(input("Enter room names seprated by comma")).split(",")

	for room in room_list:

		item_dictionary = dict()

		item_list = str(input("Enter list of item name present in {}".format(room))).split(",")

		for item in item_list:

			item_cost = str(input("For item name {} present in room {} enter the item cost".format(item, room)))

			item_dictionary[item] = item_cost

		data_dictionary[room] = item_dictionary

		print("=============================================================================")


if __name__ == '__main__':

	
	print("HOUSE INVENTORY TRACKER")

	data_dictionary = dict()

	while True:

		choice = int(input("Press 1: to start listing rooms and items for 1st time\nPress 2: Wish to add details about more rooms?. Add room. Add items and cost\nPress 3: To exit\n"))

		if choice == 1:
			main()

		elif choice == 2:

			new_room_details = dict()

			room_name = input("Wish to add more rooms? Enter the room name").split(",")

			for room in room_name:

				new_item_details = dict()

				if room not in data_dictionary.keys():
					items_list = input("Mention items present in the {}".format(room)).split(",")

					for item in items_list:
						item_cost = input("Enter cost for {}".format(item))

						new_item_details[item] = item_cost

				data_dictionary[room] = new_item_details
		elif choice == 3:
			break


		house = HouseInventory(data_dictionary)
		house.get_format_output()
		print(len(house))

		room_list = [room for room in data_dictionary.keys()]

		s = ','.join(room_list)
		print(s)

		housecost = HouseInventoryCost()
		print(housecost.get_total_item_cost(**data_dictionary))

		room = input("Out of above mentioned room, enter room name you wish to list?")
		if room in data_dictionary.keys():
			house[room]
		else:
			print("Invalid Room")




			




	
