# -*- coding: utf-8 -*-
# @File Name: CodeCraft-2019.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\CodeCraft-2019.py
# @Author: Ruige_Lee
# @Date:   2019-03-19 11:00:06
# @Last Modified by:   Ruige_Lee
# @Last Modified time: 2019-03-19 21:09:19
# @Email: 295054118@whut.edu.cn"


import logging
import sys
import json


car_path = '../config/car.txt'
road_path = '../config/road.txt'
cross_path = '../config/cross.txt'
answer_path = '../config/answer.txt'

global carData
global crossNetworkData
global crossData
global finalAnswer


carData = []

crossData = []

finalAnswer = []






def load_data():
	global carData
	global crossNetworkData
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

	with open("./helpScript/crossNetwork.json",'r') as crossNetworkFile:
		data = crossNetworkFile.read()
		crossNetworkData = json.loads(data)

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




def find_roadLine(crossTree,lever,lastEleCnt):

	# 产生roadline
	flag_break = 0
	roadLine = []

	idAim = lastEleCnt
	while(lever != 0):
		lever = lever - 1

		upEleCnt = 0;
		idCnt = 0

		# print ("crossTree[lever]=",crossTree[lever])
		for ele in crossTree[lever]:
			# print ("ele=",ele)
			for crossID in ele:

				if (idCnt == lastEleCnt):
					roadLine.insert(0,crossID)
					idAim = upEleCnt
					flag_break = 1
					break

				idCnt = idCnt + 1;

			if (flag_break == 1):
				flag_break = 0
				break

			upEleCnt = upEleCnt + 1

		lastEleCnt = upEleCnt


	return roadLine


def findEndPos(crossTree,endPos):

	lever = len(crossTree)
	aimID = endPos

	# 找endPos
	while(lever != 0):
		lever = lever - 1
		eleCnt = 0;
		for ele in crossTree[lever]:
			
			for crossID in ele:
				if (crossID == endPos):
					return eleCnt,lever

			eleCnt = eleCnt + 1




def simpleShortestWay(startPos,endPos):

	# 加载对应树
	crossTree = crossNetworkData[startPos-1]

	eleCnt,lever = findEndPos(crossTree,endPos)

	roadline = find_roadLine(crossTree,lever,eleCnt)

	roadline.append(endPos)

	return roadline




def cross2road(crossLine):

	# print("crossLine=",crossLine)
	roadLine = []
	index = len(crossLine)
	for i in range (0,index-1):
		# print ( crossLine[i],crossLine[i+1] )
		startCross = crossData[crossLine[i]-1]
		endCross = crossData[crossLine[i+1]-1]

		if ( (startCross[1] == endCross[1] or startCross[1] == endCross[2] or startCross[1] == endCross[3] or startCross[1] == endCross[4]) and (startCross[1] != -1) ):
			roadLine.append( startCross[1] )
		elif ( (startCross[2] == endCross[1] or startCross[2] == endCross[2] or startCross[2] == endCross[3] or startCross[2] == endCross[4]) and (startCross[2] != -1)):
			roadLine.append( startCross[2] )
		elif ( (startCross[3] == endCross[1] or startCross[3] == endCross[2] or startCross[3] == endCross[3] or startCross[3] == endCross[4]) and (startCross[3] != -1)):
			roadLine.append( startCross[3] )
		elif ( (startCross[4] == endCross[1] or startCross[4] == endCross[2] or startCross[4] == endCross[3] or startCross[4] == endCross[4]) and (startCross[4] != -1)):
			roadLine.append( startCross[4] )
		# else:
		# print("warning",startCross,endCross)


	# print ("roadLine=",roadLine)
	return roadLine





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
			# print ( "Sort from ",data[1],"to",data[2] )


			crossLine = simpleShortestWay(data[1],data[2])

			roadLine = cross2road(crossLine)

			oneCar.extend(roadLine)
			
			# print ( "oneCar=",oneCar )

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
	# main()
	load_data()
	answer_init()

	createAnswer()
