from collection import deque
def bread_first_search(graph, item, target):
	search_queue = deuqe()
	search_queue += graph[item]
	searched = []
	while search_queue:
		#  pops the item from the queue 
		curr_item = search_queue.popleft()
		# if the item is not already searched
		if curr_item not in searched:
			# if the item equals the target
			if curr_item == target:
				print(curr_item + "  matches the target value.\n")
				return True
			else:
				# adding the item's connection to the search list
				search_queue += graph[curr_item]
				# put the item in already searched list
				searched.add(curr_item)
	return False

university_body = {students: ["freshman","sophomore"], teaches: ["professors","teaching_assistants"], sophomore: ["henchhing", "zaykha", "kalesh", "mahia"]}
breadth_first_search(university_body, "students", "henchhing")

 
		
