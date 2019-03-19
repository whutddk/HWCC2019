# -*- coding: utf-8 -*-
# @File Name: CodeCraft-2019.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\CodeCraft-2019.py
# @Author: Ruige_Lee
# @Date:   2019-03-19 11:00:06
# @Last Modified by:   Ruige_Lee
# @Last Modified time: 2019-03-19 15:51:11
# @Email: 295054118@whut.edu.cn"

# @File Name: CodeCraft-2019.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\CodeCraft-2019.py
# @Author: 29505
# @Date:   2019-03-17 23:16:45
# @Last Modified by:   29505
# @Last Modified time: 2019-03-19 00:05:15
# @Email: 295054118@whut.edu.cn

import logging
import sys
import re

car_path = '../config/car.txt'
road_path = '../config/road.txt'
cross_path = '../config/cross.txt'
answer_path = '../config/answer.txt'

global carData
global roadData
global crossData
global finalAnswer
carData = []
roadData = []
crossData = []

finalAnswer = []






def load_data():
	global carData
	global roadData
	global crossData

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
			po = string.find(')')
			takeoffTime = int(string[:po])
			# print (takeoffTime)

			carData.append([carID,startPos,endPos,maxSpeed,takeoffTime])
		# print (carData)



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


def answer_init():
	global finalAnswer
	finalAnswer = carData

	# 出发时间排序
	finalAnswer.sort(key=lambda x:x[4])
	# print (finalAnswer)





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





def simpleShortestWay(startPos,endPos):
	global crossCollection
	crossCollection = crossData.copy()
	roadList = []

	roadList.append([startPos])
	del crossCollection[startPos-1]


	# print (roadList[0])
	while(1):
		OneCrossLever = []
		for crossId in roadList[len(roadList)-1]:
			# print ("crossId=",crossId)
			if ( crossId == -1 ):
				cross1,cross2,cross3,cross4 = -1,-1,-1,-1
			else:
				cross1,cross2,cross3,cross4 = findNextCrossId(crossId)
				# if ( cross1 != -1):
				# 	del crossCollection[cross1-1]
				# if ( cross2 != -1):
				# 	del crossCollection[cross2-1]
				# if ( cross3 != -1):
				# 	del crossCollection[cross3-1]
				# if ( cross4 != -1):
				# 	del crossCollection[cross4-1]

			OneCrossLever.append(cross1)
			OneCrossLever.append(cross2)
			OneCrossLever.append(cross3)
			OneCrossLever.append(cross4)


		
		# print ( "路口集合=",crossCollection )
		crossCnt = 0
		for cross in OneCrossLever:
			if ( cross == endPos):
				# print ("done!",crossCnt)
				roadLine = []
				lever = len(roadList)
				# print ( "len of roadList",lever)
				# print ("endPos=",OneCrossLever[crossCnt])
				roadLine.insert(0,OneCrossLever[crossCnt])

				while( lever != 0 ):
					lever = lever -1 
					searchLever = roadList[lever]
					crossCnt = crossCnt // 4
					# print ("-1Pos=",searchLever[crossCnt])
					roadLine.insert(0,searchLever[crossCnt])
				# print ("roadLine=",roadLine)
				# while(1):
				# 	pass

				return roadLine

			crossCnt = crossCnt + 1

		roadList.append(OneCrossLever)

	pass





def createAnswer():

	# [carID,startPos,endPos,maxSpeed,takeoffTime]
	# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]
	# [crossID,roadID1,roadID2,roadID3,roadID4]
	global finalAnswer

	answer = finalAnswer.copy()
	finalAnswer = []


	with open( answer_path,'w') as answerFile:
	
		for data in answer:
			oneCar = [data[0],data[4]]
			print ( "Sort from ",data[1],"to",data[2] )
			roadLine = simpleShortestWay(data[1],data[2])

			oneCar.extend(roadLine)
			
			print ( "oneCar=",oneCar )

			writeResult = "(" 
			for data in oneCar:
				writeResult = writeResult + str(data) + ','

			writeResult = writeResult[:-1]+")\n"
					
			answerFile.write(writeResult)
			# 	
			# 	
			# while(1):
			# 	pass


	pass






# 车辆出发时间排序
# 遍历车辆出发路口，A*寻找最短路径，作为结果


	

















def main():
	global car_path
	global road_path
	global cross_path
	global answer_path



	car_path = sys.argv[1]
	road_path = sys.argv[2]
	cross_path = sys.argv[3]
	answer_path = sys.argv[4]

#     logging.info("car_path is %s" % (car_path))
#     logging.info("road_path is %s" % (road_path))
#     logging.info("cross_path is %s" % (cross_path))
#     logging.info("answer_path is %s" % (answer_path))

# to read input file
# process
# to write output file


if __name__ == "__main__":
	main()
	load_data()
	answer_init()

	createAnswer()
