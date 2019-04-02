# -*- coding: utf-8 -*-
# @File Name: ol_fileSystem.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK_python\CodeCraft-2019\src\ol_fileSystem.py
# @Author: Ruige_Lee
# @Date:   2019-03-25 08:50:11
# @Last Modified by:   Ruige_Lee
# @Last Modified time: 2019-04-02 09:47:45
# @Email: 295054118@whut.edu.cn"

# @File Name: ol_fileSystem.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\ol_fileSystem.py
# @Author: Ruige_Lee
# @Date:   2019-03-21 08:31:20
# @Last Modified by:   29505
# @Last Modified time: 2019-03-24 22:37:31
# @Email: 295054118@whut.edu.cn
# @page: https://whutddk.github.io/

# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]
# [crossID,roadID1,roadID2,roadID3,roadID4]
# [carID,startPos,endPos,maxSpeed,takeoffTime,isPri,isPreSet]
# [preSetCarID,startTime,roadId1,roadId2........]



import sys

class fS():
	def __init__(self):
		self.carData = []
		self.roadData = []
		self.crossData = []
		self.presetAnswerData = []
		self.finalAnswer = []

	def load_data(self,car_path,road_path,cross_path,preset_answer_path):

		with open(road_path,'r') as roadFile:
			for data in roadFile.readlines():
				if data[0] == '#':
					continue

				string = data
				po = string.find(',')
				roadID = int(string[1:po])

				string = string[po+2:]
				po = string.find(',')
				roadLength = int(string[:po])

				string = string[po+2:]
				po = string.find(',')
				maxSpeed = int(string[:po])

				string = string[po+2:]
				po = string.find(',')
				chnNum = int(string[:po])

				string = string[po+2:]
				po = string.find(',')
				startID = int(string[:po])

				string = string[po+2:]
				po = string.find(',')
				endID = int(string[:po])

				string = string[po+2:]
				po = string.find(')')
				doubleBool = int(string[:po])
				# print (doubleBool)

				self.roadData.append([roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool])
			# print (self.roadData)

		with open(cross_path,'r') as crossFile:
			for data in crossFile.readlines():
				if data[0] == '#':
					continue

				string = data
				po = string.find(',')
				crossID = int(string[1:po])

				string = string[po+2:]
				po = string.find(',')
				roadID1 = int(string[:po])

				string = string[po+2:]
				po = string.find(',')
				roadID2 = int(string[:po])

				string = string[po+2:]
				po = string.find(',')
				roadID3 = int(string[:po])

				string = string[po+2:]
				po = string.find(')')
				roadID4 = int(string[:po])

				self.crossData.append([crossID,roadID1,roadID2,roadID3,roadID4])
			# print (self.crossData)

		with open(car_path,'r') as carFile:
			for data in carFile.readlines():
				if data[0] == '#':
					continue

				string = data
				po = string.find(',')
				carID = int(string[1:po])

				string = string[po+2:]
				po = string.find(',')
				startPos = int(string[:po])

				string = string[po+2:]
				po = string.find(',')
				endPos = int(string[:po])

				string = string[po+2:]
				po = string.find(',')
				maxSpeed = int(string[:po])

				string = string[po+2:]
				po = string.find(',')
				takeoffTime = int(string[:po])

				string = string[po+2:]
				po = string.find(',')
				isPri = int(string[:po])

				string = string[po+2:]
				po = string.find(')')
				isPreSet = int(string[:po])
				# print (takeoffTime)

				self.carData.append([carID,startPos,endPos,maxSpeed,takeoffTime,isPri,isPreSet])
			# print (self.carData)




	
	def save_answer(self,answer_path):
		with open( answer_path,'w') as answerFile:
			for oneCar in self.finalAnswer:
				writeResult = "(" 
				for data in oneCar:
					writeResult = writeResult + str(data) + ','
				writeResult = writeResult[:-1]+")\n"						
				answerFile.write(writeResult)

