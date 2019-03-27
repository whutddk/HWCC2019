# -*- coding: utf-8 -*-
# @File Name: ol_scheduler.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\ol_scheduler.py
# @Author: Ruige_Lee
# @Date:   2019-03-25 08:50:11
# @Last Modified by:   Ruige_Lee
# @Last Modified time: 2019-03-27 10:01:52
# @Email: 295054118@whut.edu.cn"

# @File Name: ol_scheduler.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\ol_scheduler.py
# @Author: Ruige_Lee
# @Date:   2019-03-21 20:25:35
# @Last Modified by:   29505
# @Last Modified time: 2019-03-24 22:37:11
# @Email: 295054118@whut.edu.cn
# @page: https://whutddk.github.io/






import sys



class scheduler():
	def __init__(self):
		self.carData = []
		self.roadData = []
		self.crossData = []
		self.preSort = []



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



	def pre_scheduler(self,carData,roadData,crossData):
		self.carData = carData
		self.roadData = roadData
		self.crossData = crossData

		self.preSort = self.carData.copy()
		# 出发时间排序
		self.preSort.sort(key=lambda x:x[4]) 

		# 高速先排路线
		self.preSort.sort(key=lambda x:x[3],reverse=True)

		return self.preSort





	
	def fin_scheduler(self,preAnswer):
		answer = preAnswer
		additionalTime = 0		
		takeoffset = 0
		for ans in range(0,len(answer)):
			if ( additionalTime < takeoffset ):
				pass
			elif ( answer[ans][1] < (additionalTime-takeoffset)//25 ):
				answer[ans][1] = (additionalTime-takeoffset)//25
			else:
				pass
			
			additionalTime = additionalTime + 1 
		

		# print (answer)
		return answer
