# -*- coding: utf-8 -*-
# @File Name: CodeCraft-2019.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\CodeCraft-2019.py
# @Author: Ruige_Lee
# @Date:   2019-03-19 11:00:06
# @Last Modified by:   Ruige_Lee
# @Last Modified time: 2019-03-19 20:11:53
# @Email: 295054118@whut.edu.cn"


import logging
import sys
import json


car_path = '../config/car.txt'
road_path = '../config/road.txt'
cross_path = '../config/cross.txt'
answer_path = '../config/answer.txt'

global carData

global crossData
global finalAnswer


carData = []

crossData = []

finalAnswer = []






def load_data():
	global carData

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

	with open("./helpScript/network.json",'r') as crossFile:
		data = crossFile.read()
		crossData = json.loads(data)

	# print (crossData)




def answer_init():
	global finalAnswer
	finalAnswer = carData

	# 出发时间排序
	finalAnswer.sort(key=lambda x:x[4])
	# print (finalAnswer)




def find_roadLine(crossTree,lever,lastEleCnt):

	# 产生roadline

	roadLine = []

	idAim = lastEleCnt
	while(lever != 0):
		lever = lever - 1
		upEleCnt = 0;
		idCnt = 0

		print ("crossTree[lever]=",crossTree[lever])
		for ele in crossTree[lever]:
			for crossID in ele:
				if (idCnt == lastEleCnt):
					roadLine.insert(0,crossID)
					idAim = upEleCnt
					break

				idCnt = idCnt + 1;

			if (idAim == upEleCnt):
				break

			upEleCnt = upEleCnt + 1
			
	print ("roadLine=",roadLine)


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
	crossTree = crossData[startPos-1]

	eleCnt,lever = findEndPos(crossTree,endPos)

	find_roadLine(crossTree,lever,eleCnt)



	pass






def createAnswer():

	# [carID,startPos,endPos,maxSpeed,takeoffTime]
	# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]
	# [crossID,roadID1,roadID2,roadID3,roadID4]
	global finalAnswer

	answer = finalAnswer.copy()
	finalAnswer = []


	
	
	for data in answer:
		oneCar = [data[0],data[4]]
		print ( "Sort from ",data[1],"to",data[2] )


		roadLine = simpleShortestWay(data[1],data[2])

		# oneCar.extend(roadLine)
		
		# print ( "oneCar=",oneCar )

		# writeResult = "(" 
		# for data in oneCar:
		# 	writeResult = writeResult + str(data) + ','

		# writeResult = writeResult[:-1]+")\n"
				
		# answerFile.write(writeResult)
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
