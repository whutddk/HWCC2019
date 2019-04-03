# -*- coding: utf-8 -*-
# @File Name: ol_crossNetWorkOnline.py
# @File Path: K:\work\dark+PRJ\HWCC2019\SDK_python\CodeCraft-2019\src\ol_crossNetWorkOnline.py
# @Author: Ruige_Lee
# @Date:   2019-03-25 08:50:11
# @Last Modified by:   29505
# @Last Modified time: 2019-04-03 23:39:19
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
		self.presetAnswerData = []



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

		print ("find CrossIndex Fail!")
		while(1):
			pass

	def find_roadIndex(self,roadID):

		index = 0
		for index in range(0,len(self.roadData)):
			if (self.roadData[index][0] == roadID):
				return index

		print ("find RoadIndex Fail!")
		while(1):
			pass

	def find_carIndex(self,carID):

		index = 0
		for index in range(0,len(self.carData)):
			if (self.carData[index][0] == carID):
				return index

		print ("find CarIndex Fail!")
		while(1):
			pass

	def find_persetAnswerIndex(self,carID):

		index = 0
		for index in range(0,len(self.presetAnswerData)):
			if (self.presetAnswerData[index][0] == carID):
				return index

		print ("find presetAnswerIndex Fail!")
		while(1):
			pass
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def bw_SearchOneLever(self,crossTree,lever,lastEleCnt):
		upEleCnt = 0;
		idCnt = 0
		for ele in crossTree[lever]:
			# print ("ele=",ele)
			for crossID in ele:

				if (idCnt == lastEleCnt):
					# print ("upEleCnt=",upEleCnt)
					return upEleCnt,crossID
				idCnt = idCnt + 1;
			upEleCnt = upEleCnt + 1

		print ("error")
		while(1):
			pass


	def bw_SortCross(self,crossTree,eleCnt_i):

		lever = len(crossTree)
		crossLine = []
		# 最后一层多少元件，决定上层的枝干编号
		# print ("lastLever=",self.crossTree[len(self.crossTree)-1])
		eleCnt = eleCnt_i
		# print ("eleCnt=",eleCnt)

		# 产生crossline
		lever = lever - 1
		while(lever != 0):
			lever = lever - 1
			# print ("crossTree[lever]=",crossTree[lever])
			eleCnt,upCrossID = self.bw_SearchOneLever(crossTree,lever,eleCnt)
			crossLine.insert(0,upCrossID)

		return crossLine







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


# [carID,startPos,endPos,maxSpeed,takeoffTime]
# 生成树同时把该起点的corssLine进行全局编排，放入一组
	def fw_createCrossTree(self,crossID):

		oneCrossLineGroup = []
		# 同一起点的车
		oneCrossCarGroup = []

		for car in self.carData:
			if ( car[1] == crossID ):
				oneCrossCarGroup.append(car)



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

			for eleCnt in range(0,len(lastLever)):
				for crossId in lastLever[eleCnt]:
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
					

					# 提前生成该起点车的cross路线
					for car in oneCrossCarGroup:
						endCross = car[2]
						if ( ( car[6] == 0 ) and ((cross1 == endCross) or (cross2 == endCross) or (cross3 == endCross) or (cross4 == endCross)) ):
							crossLine = self.bw_SortCross(crossTree,eleCnt)
							crossLine.append( crossId )
							crossLine.append( endCross )

							# 先带入最高速度为第一项，起飞时间为第二项，方便后排序
							carSch = [car[3],car[0],car[4]]
							carSch.extend(crossLine)

							oneCrossLineGroup.append(carSch)

					# 本路口级增加一个枝干组
					OneCrossLever.append(leavesCheck)
				
				# print ( "路口未激活集合=",self.crossCollection )	
			# print ( "路口集合=",crossCollection )

			crossTree.append(OneCrossLever)

			if ( len(self.crossCollection) == 0 ):
				self.crossLineGroup.append(oneCrossLineGroup)
				return crossTree

		pass			





	def cross2road(self,crossLine):
		# print("crossLine=",crossLine)
		roadLine = [crossLine[0],crossLine[1]]
		index = len(crossLine)
		for i in range (2,index-1):
			# print ( crossLine[i],crossLine[i+1] )
			startCrossTemp = self.crossData[self.find_crossIndex(crossLine[i])]
			endCrossTemp = self.crossData[self.find_crossIndex(crossLine[i+1])]

			if ( (startCrossTemp[1] == endCrossTemp[1] or startCrossTemp[1] == endCrossTemp[2] or startCrossTemp[1] == endCrossTemp[3] or startCrossTemp[1] == endCrossTemp[4]) and (startCrossTemp[1] != -1) ):
				RoadID = startCrossTemp[1]
			elif ( (startCrossTemp[2] == endCrossTemp[1] or startCrossTemp[2] == endCrossTemp[2] or startCrossTemp[2] == endCrossTemp[3] or startCrossTemp[2] == endCrossTemp[4]) and (startCrossTemp[2] != -1)):
				RoadID = startCrossTemp[2]
			elif ( (startCrossTemp[3] == endCrossTemp[1] or startCrossTemp[3] == endCrossTemp[2] or startCrossTemp[3] == endCrossTemp[3] or startCrossTemp[3] == endCrossTemp[4]) and (startCrossTemp[3] != -1)):
				RoadID = startCrossTemp[3]
			elif ( (startCrossTemp[4] == endCrossTemp[1] or startCrossTemp[4] == endCrossTemp[2] or startCrossTemp[4] == endCrossTemp[3] or startCrossTemp[4] == endCrossTemp[4]) and (startCrossTemp[4] != -1)):
				RoadID = startCrossTemp[4]

			# print("warning",startCross,endCross)
			roadLine.append( RoadID )

		# print ("roadLine=",roadLine)
		return roadLine




	def createNetwork(self):

		self.crossLineGroup = []
	# 产生树表，每棵树级越少越先
		for cross in self.crossData:
			crossID = cross[0]
			crossTree = self.fw_createCrossTree(crossID)
			self.crossTreeGroup.append(crossTree)


################################################################################
		
		# 重新按高速先行进行排序测试
		crossLine = []
		for oneCrossLineGroup in self.crossLineGroup:
			for car in oneCrossLineGroup:
				crossLine.append(car)

		# 先出发在前
		crossLine.sort(key=lambda x:x[2])
		# 高速在前
		crossLine.sort(key=lambda x:x[0],reverse=True)


		offset = 0
		additionalTime = 2
		
		for ans in range(0,len(crossLine)):
			schTime = additionalTime//1 + offset
			if ( crossLine[ans][2] < schTime ):
				crossLine[ans][2] = schTime
			# additionalTime = additionalTime + 5
			

			if ( schTime < 755 ):
				additionalTime = additionalTime + 5
				 
			else:			
				additionalTime = additionalTime + 3 






		for i in range(0,len(crossLine)):
			crossLine[i].remove(crossLine[i][0])
			# print ( crossLine[i] )
		


################################################################################
		

		roadLine = []
		for car in crossLine:
			roadLine.append(self.cross2road(car))
			# print ( roadLine[i] )


		return roadLine


	def crossNetwork_init(self,carData,roadData,crossData,presetAnswerData):
		self.carData = carData
		self.roadData = roadData
		self.crossData = crossData
		self.presetAnswerData = presetAnswerData



