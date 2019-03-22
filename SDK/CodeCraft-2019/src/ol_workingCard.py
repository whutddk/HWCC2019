# -*- coding: utf-8 -*-
# @File Name: ol_workingCard.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\ol_workingCard.py
# @Author: Ruige_Lee
# @Date:   2019-03-22 09:32:33
# @Last Modified by:   Ruige_Lee
# @Last Modified time: 2019-03-22 11:51:46
# @Email: 295054118@whut.edu.cn"

# @File Name: ol_workingCard.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\ol_workingCard.py
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

class workingCard(carData,roadData):

	def __init__(self):
		self.card = []
		self.roadData = []
		self.carData = []

		for i in range (0,SCHEDULE_SILCE):
			timeSlice = []
			for j in range (0,ROAD_CNT):
				timeSlice.append([0,0])
			self.card.append(timeSlice)

		self.roadData = roadData
		self.carData = carData


		# 用于得出新结果后刷新工作牌，需要maxSpeed,takeoffTime，roadLength,maxSpeed,chnNum,行驶方向
	
		# 强制onePreAnswer格式处理为（车，起飞时间，路，0/1，路，0/1.。。。）
	def updateCard(self,onePreAnswer):

		carID = onePreAnswer[0]
		carSpeed = self.carData[carID][3]
		schTime = onePreAnswer[1]		
		roadPointer = 2

		while( roadPointer < len(onePreAnswer) ):
			
			roadID = onePreAnswer[roadPointer]
			roadDir = onePreAnswer[roadPointer+1]
			roadLength = self.roadData[roadID-5000][1]
			roadSpeed = self.roadData[roadID-5000][2]

			maxSpeed = min(roadSpeed,carSpeed)

			self.card[schTime][roadID-5000][roadDir] = self.card[schTime][roadID][roadDir] + 1
			if ( roadLength // maxSpeed < schTime):
				roadPointer = roadPointer + 2

			schTime = schTime + 1

		return 0


		# 用于评估路线时绕开拥堵路段

		# 抽象为出发时刻后一段时间内的情况
	def queryCardOnce(self,startTimeSlice,roadID,roadDir):
		
		SEARCHSLICE = 30
		maxCarNum = 0;
		roadChnNum = self.roadData[roadID-5000][3]

		for slice in range (startTimeSlice,startTimeSlice + SEARCHSLICE):
			maxCarNum = max(maxCarNum,self.card[slice][roadID-5000][roadDir])

		return carNum,roadChnNum

	# 可精确配平，也可以
	def queryCardPerious(self):
		pass		



