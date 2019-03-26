# -*- coding: utf-8 -*-
# @File Name: ol_workingCard.py
# @File Path: K:\work\dark+PRJ\HWCC2019\SDK\CodeCraft-2019\src\ol_workingCard.py
# @Author: Ruige_Lee
# @Date:   2019-03-22 09:32:33
# @Last Modified by:   29505
# @Last Modified time: 2019-03-24 19:49:01
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

SEARCHSLICE = 0
# [carID,startPos,endPos,maxSpeed,takeoffTime]
# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]
# [crossID,roadID1,roadID2,roadID3,roadID4]

class workingCard():

	def __init__(self):
		self.card = []
		self.roadData = []
		self.carData = []

		self.carID = 0
		self.startTimeSlice = 0
		self.roadList = []

		for i in range (0,SCHEDULE_SILCE):
			timeSlice = []
			for j in range (0,ROAD_CNT):
				timeSlice.append([0,0])
			self.card.append(timeSlice)

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

#____________________________________________________


		# 用于得出新结果后刷新工作牌，需要maxSpeed,takeoffTime，roadLength,maxSpeed,chnNum,行驶方向
	
	def updateCard(self):

		# print("self.carID=",self.carID)
		# print( "self.carData[self.find_carIndex(self.carID)=",self.carData[self.find_carIndex(self.carID) )
#____________________________________________________	
		carSpeed = self.carData[self.find_carIndex(self.carID)][3]
#____________________________________________________	
		schTime = self.startTimeSlice	

		for roadStruct in self.roadList:
			
			while(1):
				roadID = roadStruct[0]
				roadDir = roadStruct[1]

#____________________________________________________	
				roadLength = self.roadData[self.find_roadIndex(roadID)][1]
				roadSpeed = self.roadData[self.find_roadIndex(roadID)][2]
#____________________________________________________	

				maxSpeed = min(roadSpeed,carSpeed)

#____________________________________________________	
				self.card[schTime][self.find_roadIndex(roadID)][roadDir] = self.card[schTime][self.find_roadIndex(roadID)][roadDir] + 1
#____________________________________________________	

				# print( "schTime,roadID,roadDir=",schTime,roadID,roadDir  )
				# print (self.card[schTime][self.find_roadIndex(roadID)][roadDir])
				schTime = schTime + 1

				if ( roadLength // maxSpeed < schTime):
					# print ('break')
					break

		# print ("update finish")	

		return 0


		# 用于评估路线时绕开拥堵路段

		# 抽象为出发时刻后一段时间内的情况
	def queryCardOnce(self,roadID,roadDir):
		
		
		maxCarNum = 0;

#____________________________________________________	
		roadChnNum = self.roadData[self.find_roadIndex(roadID)][3]
#____________________________________________________	

		for slice in range (self.startTimeSlice,self.startTimeSlice + SEARCHSLICE):
#____________________________________________________	
			maxCarNum = max(maxCarNum,self.card[slice][self.find_roadIndex(roadID)][roadDir])
#____________________________________________________	


			# if ( roadChnNum > maxCarNum ):
		return roadChnNum - maxCarNum
			# else:



	# 可精确配平，也可以
	def queryCardPerious(self):
		pass		


	def wCard_init(self,roadData,carData):
		self.roadData = roadData
		self.carData = carData

	def wCard_reset(self,startTimeSlice,carID):
		self.startTimeSlice = startTimeSlice
		self.roadList = []

		self.carID = carID


	def wCard_pushOneRoad(self,RoadID,roadDir):
		self.roadList.append([RoadID,roadDir])
