#深度优先算法


#获取当前可以移动的方向
def GetCanMove():
	global visited
	startX,startY = get_pos_x(),get_pos_y()
	result = []
	Directions = {
		North:(0,1),
		East:(1,0),
		South:(0,-1),
		West:(-1,0)}
	for i in Directions:
		if can_move(i):
			moveX,moveY = Directions[i][0] +startX,Directions[i][1] +startY
			result.append((i,(moveX,moveY)))
	return result       


# 深度搜索算法
def DeepFirstSearch():
	global task #当前任务状态（是否已经采集宝箱）
	global visited #保存已经走过的位置

	#获取当前位置并保存
	start = (get_pos_x(),get_pos_y())
	visited.add(start)

	#判断当前位置是否是宝箱
	if start == measure():
		harvest()
		task = True
		return
	
	#获取当前可以移动的方向
	for i in GetCanMove():
		#只去移动没有走过的位置
		if i[1] not in visited:
			#移动并进行下一轮探索
			move(i[0])
			# till() 可用于观察路径
			DeepFirstSearch(i[0])
			if task:
				return
			move_back(i[0])
#回溯方法用于
def move_back(d):
	back = {
		North:South,
		East:West,
		South:North,
		West:East
	}
	move(back[d])


task = False
visited = set()



#重复生成迷宫
while True:
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
		DeepFirstSearch(None)
		task = False
		visited = set()
