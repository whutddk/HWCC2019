# -*- coding: utf-8 -*-
# @File Name: ol_crossNetWorkOnline.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\ol_crossNetWorkOnline.py
# @Author: Ruige_Lee
# @Date:   2019-03-19 11:00:06
# @Last Modified by:   Ruige_Lee
# @Last Modified time: 2019-03-23 16:57:46
# @Email: 295054118@whut.edu.cn"



import sys
import ol_roadValueRisk
import ol_workingCard


class crossNetwork():

	def __init__(self):
		self.carData = []
		self.roadData = []
		self.crossData = []

		self.crossCollection = []
		self.crossTree = []

		self.carID = []
		self.startCross = 1
		self.endCross = 1
		self.takeoffTime = []
		self.roadLine = []


		self.RDV = ol_roadValueRisk.roadValue()
		self.wCard = ol_workingCard.workingCard()

		pass
	

	def fw_checkroadVV(self,startCross,roadId,preDir):
		retDir = 0
		nextCross = -1
		# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]
		
		if ( roadId == -1 ):
			return nextCross,0,retDir

		# 默认路就是5000开始的
		oneRoad = self.roadData[roadId-5000] 
		# print ("oneRoad=",oneRoad)
		if ( oneRoad[4] == startCross ):		
			nextCross = oneRoad[5]
			roadDir = 0

		elif ( oneRoad[5] == startCross and oneRoad[6] == 1 ):			
			nextCross = oneRoad[4]
			roadDir = 1
		else:
			pass

		for vaildCross in self.crossCollection:
			if ( nextCross == vaildCross[0] ):
				# print ( "checkroadVaild=Return" ,nextCross)
				self.crossCollection.remove(vaildCross)

#####################################################################
	#如果这条路是有效的，在这里调用子函数计算这条路的价值，然后一起返回,
	#可以参考的参数：道路的最高速，当前车的最高速，道路长度，车道数
	
				# roadValue = self.wCard.queryCardOnce(roadId,roadDir)
				# roadValue = self.RDV.RD_Value(oneRoad[1],oneRoad[2],oneRoad[3])
				
				# [crossID,roadID1,roadID2,roadID3,roadID4]
				if ( roadId == self.crossData[startCross-1][1]  ):
					retDir = 1
				elif ( roadId == self.crossData[startCross-1][2]  ):
					retDir = 2
				elif ( roadId == self.crossData[startCross-1][3]  ):
					retDir = 3
				elif ( roadId == self.crossData[startCross-1][4]  ):
					retDir = 4
				else:
					print ("error!")
					while(1):
						pass
				# 直行
				if ( retDir == preDir ):
					roadValue = 4
				elif ( (preDir == 1 and retDir == 4) or (preDir == 2 and retDir == 1) or (preDir == 3 and retDir == 2) or (preDir == 4 and retDir == 3)):
					roadValue = 3
				elif ( (preDir == 1 and retDir == 4) or (preDir == 2 and retDir == 1) or (preDir == 3 and retDir == 2) or (preDir == 4 and retDir == 3)):
					roadValue = 2
				else:
					roadValue = 0
#####################################################################


				return nextCross,roadValue,retDir


		# print ( "checkroadVaild=Return" ,-1)
		return -1,0,retDir




	def fw_createcrossTree(self):

		# 载入起始点，使用格式，每层两级，一级表示层，一级对应上层的实体枝干
		self.crossTree.append([[[self.startCross,0]]])

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
					crossInfo = self.crossData[crossId[0]-1]
					# print ("crossInfo=",crossInfo)

					# 检查路标
					cross1Temp,value1,preDir1 = self.fw_checkroadVV(crossInfo[0],crossInfo[1],crossId[1])
					cross2Temp,value2,preDir2 = self.fw_checkroadVV(crossInfo[0],crossInfo[2],crossId[1])
					cross3Temp,value3,preDir3 = self.fw_checkroadVV(crossInfo[0],crossInfo[3],crossId[1])
					cross4Temp,value4,preDir4 = self.fw_checkroadVV(crossInfo[0],crossInfo[4],crossId[1])

					# 本级为叶子，则下一级留空以防止错位
					leavesCheck = []

##################################################

## 价值函数排序可以在这里做，本级cross已经确定，下级cross的价值可以从前面return 回来，下级cross放在前面会先被for到
#
					SortListTemp = [[cross1Temp,value1,preDir1],[cross2Temp,value2,preDir2],[cross3Temp,value3,preDir3],[cross4Temp,value4,preDir4]]
					# print( "SortListTemp=B",SortListTemp )
					SortListTemp.sort(key=lambda x:x[1],reverse=True)
					# print( "SortListTemp=A",SortListTemp )


					cross1 = [ SortListTemp[0][0], SortListTemp[0][2]]
					cross2 = [ SortListTemp[1][0], SortListTemp[1][2]]
					cross3 = [ SortListTemp[2][0], SortListTemp[2][2]]
					cross4 = [ SortListTemp[3][0], SortListTemp[3][2]]

##################################################
					



					if ( cross1[0] != -1 ):
						leavesCheck.append(cross1)
					if ( cross2[0] != -1 ):	
						leavesCheck.append(cross2)
					if ( cross3[0] != -1 ):	
						leavesCheck.append(cross3)
					if ( cross4[0] != -1 ):	
						leavesCheck.append(cross4)
					
					if ( (cross1[0] == self.endCross) or (cross2[0] == self.endCross) or (cross3[0] == self.endCross) or (cross4[0] == self.endCross) ):
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
					self.crossLine.insert(0,crossID[0])
					# print ("upEleCnt=",upEleCnt)
					return upEleCnt
				idCnt = idCnt + 1;
			upEleCnt = upEleCnt + 1

		print ("error")
		while(1):
			pass



	def bw_SortCross(self):

		# 一共有多少层
		# print ("self.crossTree=",self.crossTree)
		lever = len(self.crossTree)

		# 最后一层多少元件，决定上层的枝干编号
		# print ("lastLever=",self.crossTree[len(self.crossTree)-1])
		eleCnt = len(self.crossTree[len(self.crossTree)-1])-1
		# print ("eleCnt=",eleCnt)

		# 产生crossline
		lever = lever - 1
		while(lever != 0):
			lever = lever - 1
			# print ("self.crossTree[lever]=",self.crossTree[lever])
			eleCnt = self.bw_SearchOneLever(lever,eleCnt)

		self.crossLine.append(self.endCross)

		return


	def cross2road(self):

		# print("crossLine=",crossLine)
		self.roadLine = []
		index = len(self.crossLine)
		for i in range (0,index-1):
			# print ( crossLine[i],crossLine[i+1] )
			startCrossTemp = self.crossData[self.crossLine[i]-1]
			endCrossTemp = self.crossData[self.crossLine[i+1]-1]

			if ( (startCrossTemp[1] == endCrossTemp[1] or startCrossTemp[1] == endCrossTemp[2] or startCrossTemp[1] == endCrossTemp[3] or startCrossTemp[1] == endCrossTemp[4]) and (startCrossTemp[1] != -1) ):
				RoadID = startCrossTemp[1]
			elif ( (startCrossTemp[2] == endCrossTemp[1] or startCrossTemp[2] == endCrossTemp[2] or startCrossTemp[2] == endCrossTemp[3] or startCrossTemp[2] == endCrossTemp[4]) and (startCrossTemp[2] != -1)):
				RoadID = startCrossTemp[2]
			elif ( (startCrossTemp[3] == endCrossTemp[1] or startCrossTemp[3] == endCrossTemp[2] or startCrossTemp[3] == endCrossTemp[3] or startCrossTemp[3] == endCrossTemp[4]) and (startCrossTemp[3] != -1)):
				RoadID = startCrossTemp[3]
			elif ( (startCrossTemp[4] == endCrossTemp[1] or startCrossTemp[4] == endCrossTemp[2] or startCrossTemp[4] == endCrossTemp[3] or startCrossTemp[4] == endCrossTemp[4]) and (startCrossTemp[4] != -1)):
				RoadID = startCrossTemp[4]

			# print("warning",startCross,endCross)
			self.roadLine.append( RoadID )

#######################################

# 外挂式加载道路工作卡
			# 岔道ID == 
			if ( self.crossLine[i] == self.roadData[RoadID-5000][4] ):
				roadDir = 0
			else:
				roadDir = 1

			self.wCard.wCard_pushOneRoad( RoadID,roadDir )

#######################################


		# print ("roadLine=",roadLine)
		return 




	def createNetwork(self,oneCar):

		# [carID,startPos,endPos,maxSpeed,takeoffTime]
		# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]
		# [crossID,roadID1,roadID2,roadID3,roadID4]



		self.carID = oneCar[0]		
		self.startCross = oneCar[1]
		self.endCross = oneCar[2]
		self.takeoffTime = oneCar[4]

		self.crossCollection = []
		self.crossCollection = self.crossData.copy()
		self.crossTree = []
		self.crossLine = []
		self.roadLine = []

		# print( "CMW.carID=",self.carID )
		self.wCard.wCard_reset(self.takeoffTime,self.carID)




		# print ("sort from",self.startCross,'to',self.endCross)
		self.fw_createcrossTree()
		self.bw_SortCross()
		# print ("crossLine=",self.crossLine)
		self.cross2road()


		self.wCard.updateCard()


		return self.roadLine


	def crossNetwork_init(self,carData,roadData,crossData):
		self.carData = carData
		self.roadData = roadData
		self.crossData = crossData


		self.wCard.wCard_init(self.roadData,self.carData)
		pass







