# @File Name: ol_crossNetWorkOnline.py
# @File Path: K:\work\dark+PRJ\HWCC2019\SDK\CodeCraft-2019\src\ol_crossNetWorkOnline.py
# @Author: Ruige_Lee
# @Date:   2019-03-19 11:00:06
# @Last Modified by:   29505
# @Last Modified time: 2019-03-25 00:01:32
# @Email: 295054118@whut.edu.cn
# @page: https://whutddk.github.io/

# 整体流程定义

# 获得最高速度，要计算极差，防止有漏

# 出发时间排序
# 速度排序
# 起点排序
# 直到未调度车辆数归零
# 取1个剩余未调度车辆 
	# 生长三叉树直到完全长满
		# 每长一个结点，检查未调度表中是否有该起点车辆，（允许限制条件，速度太小就不考虑）且其终点为树根（先不查枝干），有则加入本“拍”“起点节”调度，从未调度表中删除
		# 每长一个结点，检查未调度表中是否有起点为树根，终点为该点的车辆，有则加入本“拍”“起点节”调度，从未调度表中删除
	# 遍历小节进行排序，速度相同一起写入出发时间，（不受道路限速影响），严格限制不同速度出发时间不同，防止慢速车号小先跑了



import sys
import ol_roadValueRisk
import ol_workingCard


class crossNetwork():

	def __init__(self):
		

		pass




