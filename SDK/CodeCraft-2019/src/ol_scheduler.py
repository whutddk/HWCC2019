# -*- coding: utf-8 -*-
# @File Name: ol_scheduler.py
# @File Path: K:\work\dark+PRJ\HWCC2019\SDK\CodeCraft-2019\src\ol_scheduler.py
# @Author: Ruige_Lee
# @Date:   2019-03-21 20:25:35
# @Last Modified by:   29505
# @Last Modified time: 2019-03-24 20:48:15
# @Email: 295054118@whut.edu.cn"

# [carID,startPos,endPos,maxSpeed,takeoffTime]

import sys


# 调度条件 本身起飞时间 、最高速度-》（规划）-》路程

# 调度函数：关键构造非线性函数来压缩时间，当前主要矛盾集中在起飞时间上，而不是运行时间

class scheduler():
	def __init__(self):
		self.carData = []
		self.roadData = []
		self.crossData = []
		self.targetList = []
		self.preAnswer = []
		self.takeoffPlace = []

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


# [carID,startPos,endPos,maxSpeed,takeoffTime]


# 不同起点车同时排
	def diff_startCross(self):

		# 根据cross来创建同出发列表
		for cross in self.crossData:
			self.takeoffPlace.append([])

		for car in self.targetList:
			startCrossID = car[1]
			self.takeoffPlace[ self.find_crossIndex(startCrossID) ].append(car)

		# print("self.takeoffPlace=",self.takeoffPlace)

		self.targetList = []

		while(len(self.takeoffPlace) > 0):
			for group in self.takeoffPlace:
				if ( len(group) == 0 ):
					self.takeoffPlace.remove(group)
					continue
				self.targetList.append(group[0])
				group.remove(group[0])
		# print(self.targetList)






	def pre_scheduler(self,carData,roadData,crossData):
		self.carData = carData
		self.roadData = roadData
		self.crossData = crossData


		self.targetList = self.carData.copy()
		# 出发时间排序
		self.targetList.sort(key=lambda x:x[4]) 
		
		#self.diff_startCross()
		# 高速先排路线
		self.targetList.sort(key=lambda x:x[3],reverse=True)
	

		

		additionalTime = 0
		
		takeoffset = 150
		maxtime = 1000

		for ans in range(0,len(self.targetList)):
			if ( additionalTime < takeoffset ):
				pass
			#elif ( (additionalTime-takeoffset)//20 > maxtime ):
				#self.targetList[ans][4] = maxtime
			elif ( self.targetList[ans][4] < (additionalTime-takeoffset)//25 ):
				self.targetList[ans][4] = (additionalTime-takeoffset)//25
			else:
				pass
			
			additionalTime = additionalTime + 1 



	
	def fin_scheduler(self,preAnswer):


		self.preAnswer = preAnswer

		# 多岔路后行
		# self.preAnswer.sort(key = lambda i:len(i)) 

		# for ans in self.preAnswer:
		# 	print (ans)

		return self.preAnswer

	
	
