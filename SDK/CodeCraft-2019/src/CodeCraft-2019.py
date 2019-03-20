# -*- coding: utf-8 -*-
# @File Name: CodeCraft-2019.py
# @File Path: K:\work\dark+PRJ\HWCC2019\SDK\CodeCraft-2019\src\CodeCraft-2019.py
# @Author: Ruige_Lee
# @Date:   2019-03-19 11:00:06
# @Last Modified by:   29505
# @Last Modified time: 2019-03-20 23:34:51
# @Email: 295054118@whut.edu.cn"


import logging
import sys
import json


# car_path = '../config/car.txt'
# road_path = '../config/road.txt'
# cross_path = '../config/cross.txt'
# answer_path = '../config/answer.txt'

global carData
global crossNetworkData
global crossData
global finalAnswer

global answer_path
global car_path
global road_path
global cross_path



carData = []

crossData = []

finalAnswer = []





logging.basicConfig(level=logging.DEBUG,
                    filename='../logs/CodeCraft-2019.log',
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a')





















def load_data():
	global carData
	global crossNetworkData
	global crossData
	global answer_path
	global car_path
	global road_path
	global cross_path


	
	# print (crossData)




def answer_init():
	global finalAnswer
	finalAnswer = carData

	# 出发时间排序
	finalAnswer.sort(key=lambda x:x[3])
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
	global answer_path
	global car_path
	global road_path
	global cross_path

	answer = finalAnswer.copy()
	finalAnswer = []


	
		

		additionalTime = 0
		for data in answer:
			if ( data[4] < additionalTime//16 ):
				oneCar = [data[0],additionalTime//16]
			else:
				oneCar = [data[0],data[4]]
			# print ( "Sort from ",data[1],"to",data[2] )


			crossLine = simpleShortestWay(data[1],data[2])

			roadLine = cross2road(crossLine)

			oneCar.extend(roadLine)
			
			# print ( "oneCar=",oneCar )

			

			additionalTime = additionalTime + 1 
		# 	
		# 	
		# while(1):
		# 	pass


	pass






# 车辆出发时间排序
# 遍历车辆出发路口，A*寻找最短路径，作为结果


	
















def main():
	global answer_path
	global car_path
	global road_path
	global cross_path


	if len(sys.argv) != 5:
		logging.info('please input args: car_path, road_path, cross_path, answerPath')
		exit(1)

	car_path = sys.argv[1]
	road_path = sys.argv[2]
	cross_path = sys.argv[3]
	answer_path = sys.argv[4]

	logging.info("car_path is %s" % (car_path))
	logging.info("road_path is %s" % (road_path))
	logging.info("cross_path is %s" % (cross_path))
	logging.info("answer_path is %s" % (answer_path))


	load_data()
	answer_init()

	createAnswer()


if __name__ == "__main__":
	main()

