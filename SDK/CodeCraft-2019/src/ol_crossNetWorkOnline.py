# -*- coding: utf-8 -*-
# @File Name: ol_crossNetWorkOnline.py
# @File Path: K:\work\dark+PRJ\HWCC2019\SDK\CodeCraft-2019\src\ol_crossNetWorkOnline.py
# @Author: Ruige_Lee
# @Date:   2019-03-19 11:00:06
# @Last Modified by:   29505
# @Last Modified time: 2019-03-21 00:15:03
# @Email: 295054118@whut.edu.cn"



import sys

crossCollection = []


class crossNetwork():

	def __init__(self):
		self.crossCollection = []
		self.crossList = []
		pass
	

	def checkroadVaild(self,startCross,roadId):
		global crossCollection
		result = -1
		# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]
		
		if ( roadId == -1 ):
			return result

		# 默认路就是5000开始的
		oneRoad = roadData[roadId-5000] 
		# print ("oneRoad=",oneRoad)
		if ( oneRoad[4] == startCross ):
			result = oneRoad[5]

		elif ( oneRoad[5] == startCross and oneRoad[6] == 1 ):
			result = oneRoad[4]
		else:
			pass

		for vaildCross in crossCollection:
			if (result == vaildCross[0]):
				print ( "checkroadVaild=Return" ,result)
				crossCollection.remove(vaildCross)
				return result


		# print ( "checkroadVaild=Return" ,-1)
		return -1



	def findNextCrossId(self,crossId):
		crossInfo = crossData[crossId-1]
		print ("crossInfo=",crossInfo)

	# 检查路标
		nextCross1 = checkroadVaild(crossInfo[0],crossInfo[1])
		nextCross2 = checkroadVaild(crossInfo[0],crossInfo[2])
		nextCross3 = checkroadVaild(crossInfo[0],crossInfo[3])
		nextCross4 = checkroadVaild(crossInfo[0],crossInfo[4])

		return nextCross1,nextCross2,nextCross3,nextCross4










	def createNetwork(self,carData,roadData,crossData,startCross,endCross):

		# [carID,startPos,endPos,maxSpeed,takeoffTime]
		# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]
		# [crossID,roadID1,roadID2,roadID3,roadID4]
		

		self.crossCollection = []
		self.crossCollection = crossData.copy()
		self.crossList = []

		# 载入起始点，使用格式，每层两级，一级表示层，一级对应上层的实体枝干
		self.crossList.append([[startCross]])

		# 集合中删除起始点
		del self.crossCollection[startCross-1]

		flagFound = 0
		while(1):
			OneCrossLever = []
			# 扫描上一个层，即总表的最后一个list
			lastLever = self.crossList[len(self.crossList)-1]
			for root in lastLever:
				# print ("root=",root)
				# 检查本层每个结点作为下一级的枝干
				for crossId in root:
					# print ("crossId=",crossId)

					# 调用API查找下一级对应的节点
					cross1,cross2,cross3,cross4 = self.findNextCrossId(crossId)
					# 本级为叶子，则下一级留空以防止错位
					leavesCheck = []

##################################################

## 价值函数排序可以在这里做，放在前面会先被for到

##################################################


					if ( cross1 != -1 ):
						leavesCheck.append(cross1)
					if ( cross2 != -1 ):	
						leavesCheck.append(cross2)
					if ( cross3 != -1 ):	
						leavesCheck.append(cross3)
					if ( cross4 != -1 ):	
						leavesCheck.append(cross4)
					
					if ( (cross1 == endCross) or (cross2 == endCross) or (cross3 == endCross) or (cross4 == endCross) ):
						flagFound = 1

					# 本路口级增加一个枝干组
					OneCrossLever.append(leavesCheck)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


			
			# print ( "路口未激活集合=",self.crossCollection )

			# 判定完成条件，这里为找到目标点
			if ( flagFound == 1 ):

				roadList.append(OneCrossLever)


				return roadList



			roadList.append(OneCrossLever)

		pass





		return simpleShortestWay(i))


		pass













