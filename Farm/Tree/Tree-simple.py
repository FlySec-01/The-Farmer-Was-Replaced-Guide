clear()
while True:
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
			if (get_pos_x() + get_pos_y()) % 2 == 1:
				plant(Entities.Tree)
			move(North)
		move(East)
