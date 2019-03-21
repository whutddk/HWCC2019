# -*- coding: utf-8 -*-
# @File Name: ol_crossNetWorkOnline.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\ol_crossNetWorkOnline.py
# @Author: Ruige_Lee
# @Date:   2019-03-19 11:00:06
# @Last Modified by:   Ruige_Lee
# @Last Modified time: 2019-03-21 15:46:11
# @Email: 295054118@whut.edu.cn"



import sys

crossCollection = []


class crossNetwork():

	def __init__(self):
		self.crossCollection = []
		self.crossTree = []
		self.carData = []
		self.roadData = []
		self.crossData = []
		self.startCross = 1
		self.endCross = 1
		pass
	

	def fw_checkroadVV(self,startCross,roadId):
		result = -1
		# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]
		
		if ( roadId == -1 ):
			return result

		# 默认路就是5000开始的
		oneRoad = self.roadData[roadId-5000] 
		# print ("oneRoad=",oneRoad)
		if ( oneRoad[4] == startCross ):		
			result = oneRoad[5]


		elif ( oneRoad[5] == startCross and oneRoad[6] == 1 ):			
			result = oneRoad[4]
		else:
			pass

		for vaildCross in self.crossCollection:
			if ( result == vaildCross[0] ):
				# print ( "checkroadVaild=Return" ,result)
				self.crossCollection.remove(vaildCross)

#####################################################################
	#如果这条路是有效的，在这里调用子函数计算这条路的价值，然后一起返回


#####################################################################


				return result


		# print ( "checkroadVaild=Return" ,-1)
		return -1




	def fw_createcrossTree(self):

		# 载入起始点，使用格式，每层两级，一级表示层，一级对应上层的实体枝干
		self.crossTree.append([[self.startCross]])

		# 集合中删除起始点
		del self.crossCollection[self.startCross-1]

		flagFound = 0
		while(1):
			OneCrossLever = []
			# 扫描上一个层，即总表的最后一个list
			lastLever = self.crossTree[len(self.crossTree)-1]
			for root in lastLever:
				# print ("root=",root)
				# 检查本层每个结点作为下一级的枝干
				for crossId in root:
					# print ("crossId=",crossId)

					# 调用查找下一级对应的节点


					# 默认cross索引是从1开始的
					crossInfo = self.crossData[crossId-1]
					# print ("crossInfo=",crossInfo)

					# 检查路标
					cross1 = self.fw_checkroadVV(crossInfo[0],crossInfo[1])
					cross2 = self.fw_checkroadVV(crossInfo[0],crossInfo[2])
					cross3 = self.fw_checkroadVV(crossInfo[0],crossInfo[3])
					cross4 = self.fw_checkroadVV(crossInfo[0],crossInfo[4])

					# 本级为叶子，则下一级留空以防止错位
					leavesCheck = []

##################################################

## 价值函数排序可以在这里做，本级cross已经确定，下级cross的价值可以从前面return 回来，下级cross放在前面会先被for到

##################################################


					if ( cross1 != -1 ):
						leavesCheck.append(cross1)
					if ( cross2 != -1 ):	
						leavesCheck.append(cross2)
					if ( cross3 != -1 ):	
						leavesCheck.append(cross3)
					if ( cross4 != -1 ):	
						leavesCheck.append(cross4)
					
					if ( (cross1 == self.endCross) or (cross2 == self.endCross) or (cross3 == self.endCross) or (cross4 == self.endCross) ):
						flagFound = 1

					# 本路口级增加一个枝干组
					OneCrossLever.append(leavesCheck)
			
			# print ( "路口未激活集合=",self.crossCollection )

			# 判定完成条件，这里为找到目标点
					if ( flagFound == 1 ):

						self.crossTree.append(OneCrossLever)

						# 结束crossTree的生成
						return 

			self.crossTree.append(OneCrossLever)

		pass


####################################


	def bw_SearchOneLever(self,lever,lastEleCnt):
		upEleCnt = 0;
		idCnt = 0
		for ele in self.crossTree[lever]:
			# print ("ele=",ele)
			for crossID in ele:

				if (idCnt == lastEleCnt):
					self.crossLine.insert(0,crossID)
					print ("upEleCnt=",upEleCnt)
					return upEleCnt
				idCnt = idCnt + 1;
			upEleCnt = upEleCnt + 1


	def bw_SortCross(self):

		# 一共有多少层
		# print ("self.crossTree=",self.crossTree)
		lever = len(self.crossTree)

		# 最后一层多少元件，决定上层的枝干编号
		# print ("lastLever=",self.crossTree[len(self.crossTree)-1])
		eleCnt = len(self.crossTree[len(self.crossTree)-1])
		# print ("eleCnt=",eleCnt)

		# 产生crossline

		while(lever != 0):
			lever = lever - 1
			# print ("self.crossTree[lever]=",self.crossTree[lever])
			eleCnt = self.bw_SearchOneLever(lever,eleCnt)

		self.crossLine.append(self.endCross)

		return



	def createNetwork(self,carData,roadData,crossData,startCross,endCross):

		# [carID,startPos,endPos,maxSpeed,takeoffTime]
		# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]
		# [crossID,roadID1,roadID2,roadID3,roadID4]

		self.carData = carData
		self.roadData = roadData
		self.crossData = crossData
		self.startCross = startCross
		self.endCross = endCross

		self.crossCollection = []
		self.crossCollection = self.crossData.copy()
		self.crossTree = []
		self.crossLine = []

		# print ("forward")
		print ("sort from",self.startCross,'to',self.endCross)
		self.fw_createcrossTree()
		# print ("backward")
		self.bw_SortCross()

		print ("crossLine=",self.crossLine)

		return self.crossLine










