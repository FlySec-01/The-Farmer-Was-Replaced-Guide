

#复位无人机
def Reset():
	x,y = get_pos_xy()
	size = get_world_size()
	DirectionX,DirectionY = GetDirection(0,0)

	#移动
	while not (get_pos_x()== 0):
		move(DirectionX)
	while not (get_pos_y()== 0):
		move(DirectionY)	
		

# 获取移动方向
def GetDirection(dx,dy):
	x,y = get_pos_xy()
	DirectionX,DirectionY = None,None
	if x-dx < 0:
		DirectionX = East
	else:
		DirectionX = West
	if y-dy < 0:
		DirectionY = North
	else:
		DirectionY = South
	return DirectionX,DirectionY


def get_pos_xy():
	return get_pos_x(),get_pos_y()

#移动到目标位置
def moveToPos(dx,dy):
	x,y = get_pos_xy()
	DirectionX,DirectionY = GetDirection(dx,dy)
	while not (get_pos_x()== dx):
		move(DirectionX)
	while not (get_pos_y()== dy):
		move(DirectionY)
  
  
