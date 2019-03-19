# -*- coding: utf-8 -*-
# @File Name: crossNetWorkOffline.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\helpScript\crossNetWorkOffline.py
# @Author: Ruige_Lee
# @Date:   2019-03-19 11:00:06
# @Last Modified by:   Ruige_Lee
# @Last Modified time: 2019-03-19 17:40:36
# @Email: 295054118@whut.edu.cn"



import logging
import sys
import json

road_path = '../../config/road.txt'
cross_path = '../../config/cross.txt'


global roadData
global crossData

roadData = []
crossData = []


def load_data():

	global roadData
	global crossData


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

			roadData.append([roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool])
		# print (roadData)

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
			# print (doubleBool)

			crossData.append([crossID,roadID1,roadID2,roadID3,roadID4])
		# print (crossData)






crossCollection = []

def checkroadVaild(startCross,roadId):
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
			# print ( "checkroadVaild=Return" ,result)
			# del crossCollection[result-1]
			crossCollection.remove(vaildCross)
			return result


	# print ( "checkroadVaild=Return" ,-1)
	return -1



def findNextCrossId(crossId):
	crossInfo = crossData[crossId-1]
	# print ("crossInfo=",crossInfo)

# 检查路标
	nextCross1 = checkroadVaild(crossInfo[0],crossInfo[1])
	nextCross2 = checkroadVaild(crossInfo[0],crossInfo[2])
	nextCross3 = checkroadVaild(crossInfo[0],crossInfo[3])
	nextCross4 = checkroadVaild(crossInfo[0],crossInfo[4])

	return nextCross1,nextCross2,nextCross3,nextCross4





def simpleShortestWay(input):


	global crossCollection

	crossCollection = crossData.copy()
	roadList = []

	startPos = input

	roadList.append([[startPos]])
	del crossCollection[startPos-1]


	# print (roadList[0])
	while(1):
		OneCrossLever = []
		lastLever = roadList[len(roadList)-1]

		for root in lastLever:
			for crossId in root:
				# print ("crossId=",crossId)
				if ( crossId == -1 ):
					cross1,cross2,cross3,cross4 = -1,-1,-1,-1
				else:
					cross1,cross2,cross3,cross4 = findNextCrossId(crossId)

					leavesCheck = []

					if ( cross1 != -1 ):
						leavesCheck.append(cross1)
					if ( cross2 != -1 ):	
						leavesCheck.append(cross2)
					if ( cross3 != -1 ):	
						leavesCheck.append(cross3)
					if ( cross4 != -1 ):	
						leavesCheck.append(cross4)

			OneCrossLever.append(leavesCheck)


		
		# print ( "路口集合=",crossCollection )



		if ( len(crossCollection) == 0 ):

			roadList.append(OneCrossLever)


			return roadList



		roadList.append(OneCrossLever)

	pass





def createNetwork():

	# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]
	# [crossID,roadID1,roadID2,roadID3,roadID4]
	
	

	output = []

	



	for i in range(0,64):

		print ( "Sort i= ",i )


		output = (simpleShortestWay(i))

		with open( "./network"+str(i)+".json",'w') as networkFile:
			data = json.dumps(output)
			networkFile.write(data)




	pass






# 车辆出发时间排序
# 遍历车辆出发路口，A*寻找最短路径，作为结果


	
















if __name__ == "__main__":
	load_data()

	createNetwork()
