# -*- coding: utf-8 -*-
# @File Name: ol_crossNetWorkOnline.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\ol_crossNetWorkOnline.py
# @Author: Ruige_Lee
# @Date:   2019-03-25 08:50:11
# @Last Modified by:   Ruige_Lee
# @Last Modified time: 2019-03-25 11:30:22
# @Email: 295054118@whut.edu.cn"

# @File Name: ol_crossNetWorkOnline.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\ol_crossNetWorkOnline.py
# @Author: Ruige_Lee
# @Date:   2019-03-19 11:00:06
# @Last Modified by:   29505
# @Last Modified time: 2019-03-25 00:01:32
# @Email: 295054118@whut.edu.cn
# @page: https://whutddk.github.io/

# 整体流程定义

# (获得最高速度，要计算极差，防止有漏)

# 出发时间排序(sch)
# 速度排序(sch)
#[ 起点排序](sch)
# 直到未调度车辆数归零
# 取1个剩余未调度车辆 
	# 生长三叉树直到完全长满
		# [每长一个结点，检查未调度表中是否有该起点车辆，（允许限制条件，速度太小就不考虑）且其终点为树根（先不查枝干），有则加入本“拍”“起点节”调度，从未调度表中删除]
		# 每长一个结点，检查未调度表中是否有起点为树根，终点为该点的车辆，有则加入本“拍”“起点节”调度，从未调度表中删除
	# 遍历小节进行排序，速度相同一起写入出发时间，（不受道路限速影响），严格限制不同速度出发时间不同，防止慢速车号小先跑了



import sys
import ol_roadValueRisk



class crossNetwork():

	def __init__(self):
		self.carData = []
		self.roadData = []
		self.crossData = []
		self.crossTreeGroup = []

		self.crossLineGroup = []
		self.crossCollection = []


		self.RDV = ol_roadValueRisk.roadValue()


		pass


#____________________________________________________	
	def find_crossIndex(self,crossID):

		index = 0

		for index in range(0,len(self.crossData)):
			if (self.crossData[index][0] == crossID):
				return index

		print ("findCrossIndex Fail!")
		while(1):
			pass

	def find_roadIndex(self,roadID):

		index = 0
		for index in range(0,len(self.roadData)):
			if (self.roadData[index][0] == roadID):
				return index

		print ("findRoadIndex Fail!")
		while(1):
			pass

	def find_carIndex(self,carID):

		index = 0
		for index in range(0,len(self.carData)):
			if (self.carData[index][0] == carID):
				return index

		print ("findCarIndex Fail!")
		while(1):
			pass
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	def fw_checkroadVV(self,startCross,roadId):
		nextCross = -1
		# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]
		
		if ( roadId == -1 ):
			return nextCross,0
			
		oneRoad = self.roadData[self.find_roadIndex(roadId)] 

		# print ("oneRoad=",oneRoad)
		if ( oneRoad[4] == startCross ):		
			nextCross = oneRoad[5]
		elif ( oneRoad[5] == startCross and oneRoad[6] == 1 ):			
			nextCross = oneRoad[4]
		else:
			pass

		for vaildCross in self.crossCollection:
			if ( nextCross == vaildCross[0] ):
				# print ( "checkroadVaild=Return" ,nextCross)
				self.crossCollection.remove(vaildCross)

#####################################################################
	#如果这条路是有效的，在这里调用子函数计算这条路的价值，然后一起返回,
	#可以参考的参数：道路的最高速，当前车的最高速，道路长度，车道数
	
				roadValue = self.RDV.RD_Value(oneRoad[1],oneRoad[2],oneRoad[3])
				
#####################################################################

				return nextCross,roadValue
		# print ( "checkroadVaild=Return" ,-1)
		return -1,0



# 生成树同时把该起点的corssLine进行全局编排，放入一组
	def fw_createCrossTree(self,crossID):
		self.crossCollection = self.crossData.copy()
		crossTree = []
		crossTree.append([[crossID]])

		# delete start cross
		for vaildCross in self.crossCollection:
			if ( vaildCross[0] == crossID ):
				# print ( "checkroadVaild=Return" ,nextCross)
				self.crossCollection.remove(vaildCross)
				break

		while(1):
			OneCrossLever = []
			lastLever = crossTree[len(crossTree)-1]

			for root in lastLever:
				for crossId in root:
					crossInfo = self.crossData[self.find_crossIndex(crossId)]
					# print ("crossInfo=",crossInfo)

					# 检查路标
					cross1Temp,value1 = self.fw_checkroadVV(crossInfo[0],crossInfo[1])
					cross2Temp,value2 = self.fw_checkroadVV(crossInfo[0],crossInfo[2])
					cross3Temp,value3 = self.fw_checkroadVV(crossInfo[0],crossInfo[3])
					cross4Temp,value4 = self.fw_checkroadVV(crossInfo[0],crossInfo[4])

					# 本级为叶子，则下一级留空以防止错位
					leavesCheck = []

##################################################

## 价值函数排序可以在这里做，本级cross已经确定，下级cross的价值可以从前面return 回来，下级cross放在前面会先被for到

					SortListTemp = [[cross1Temp,value1],[cross2Temp,value2],[cross3Temp,value3],[cross4Temp,value4]]
					# print( "SortListTemp=B",SortListTemp )
					SortListTemp.sort(key=lambda x:x[1],reverse=True)
					# print( "SortListTemp=A",SortListTemp )

					cross1 = SortListTemp[0][0]
					cross2 = SortListTemp[1][0]
					cross3 = SortListTemp[2][0]
					cross4 = SortListTemp[3][0]

##################################################
				
					if ( cross1 != -1 ):
						leavesCheck.append(cross1)
					if ( cross2 != -1 ):	
						leavesCheck.append(cross2)
					if ( cross3 != -1 ):	
						leavesCheck.append(cross3)
					if ( cross4 != -1 ):	
						leavesCheck.append(cross4)
					

					# if ( (cross1 == self.endCross) or (cross2 == self.endCross) or (cross3 == self.endCross) or (cross4 == self.endCross) ):
					# 	flagFound = 1

					# 本路口级增加一个枝干组
					OneCrossLever.append(leavesCheck)
				
				# print ( "路口未激活集合=",self.crossCollection )	
			# print ( "路口集合=",crossCollection )

			crossTree.append(OneCrossLever)

			if ( len(self.crossCollection) == 0 ):
				return crossTree

		pass			



	def bw_SearchOneLever(self,lever,lastEleCnt):
		pass


	def bw_SortCross(self):
		pass


	def cross2road(self):
		pass




	def createNetwork(self):

	# 产生树表，每棵树级越少越先
		for cross in self.crossData:
			crossID = cross[0]
			crossTree = self.fw_createCrossTree(crossID)
			self.crossTreeGroup.append(crossTree)


		for tree in self.crossTreeGroup:
			print ( "tree len=",len(tree) )







	def crossNetwork_init(self,carData,roadData,crossData):
		self.carData = carData
		self.roadData = roadData
		self.crossData = crossData