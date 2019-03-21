# @File Name: ol_workingCard.py
# @File Path: K:\work\dark+PRJ\HWCC2019\SDK\CodeCraft-2019\src\ol_workingCard.py
# @Author: 29505
# @Date:   2019-03-21 23:33:11
# @Last Modified by:   29505
# @Last Modified time: 2019-03-22 00:03:19
# @Email: 295054118@whut.edu.cn

import sys

SCHEDULE_SILCE = 1000
ROAD_CNT = 200

	# [carID,startPos,endPos,maxSpeed,takeoffTime]
	# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]
	# [crossID,roadID1,roadID2,roadID3,roadID4]

class workingCard():

	def __init__(self):
		self.card = []
		self.roadData = []

		for i in range (0,SCHEDULE_SILCE):
			timeSlice = []
			for j in range (0,ROAD_CNT):
				timeSlice.append([0,0])
			self.card.append(timeSlice)

	def load_data(self,roadData):
		self.roadData = roadData

		# 用于得出新结果后刷新工作牌，需要maxSpeed,takeoffTime，roadLength,maxSpeed,chnNum,行驶方向
	def updateCard(self,onePreAnswer):

		schTime = onePreAnswer[]
		roadID = onePreAnswer[]

		while(1):
			self.card[schTime][roadId1][] ++
			if (lenght /speed > schTime):
				roadid++
			if (roadid overflow):
				break


		return 0


		# 用于评估路线时绕开拥堵路段
		# 可精确配平，也可以抽线为出发时刻后一段时间内的情况
	def queryCard(self):
		pass






