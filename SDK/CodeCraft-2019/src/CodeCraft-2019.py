# -*- coding: utf-8 -*-
# @File Name: CodeCraft-2019.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\CodeCraft-2019.py
# @Author: Ruige_Lee
# @Date:   2019-03-19 11:00:06
# @Last Modified by:   Ruige_Lee
# @Last Modified time: 2019-03-21 20:59:35
# @Email: 295054118@whut.edu.cn"


import logging
import sys
import json
import ol_fileSystem 
import ol_crossNetWorkOnline
import ol_scheduler
# car_path = '../config/car.txt'
# road_path = '../config/road.txt'
# cross_path = '../config/cross.txt'
# answer_path = '../config/answer.txt'

fS = ol_fileSystem.fS() 
CNW = ol_crossNetWorkOnline.crossNetwork()
sch = ol_scheduler.scheduler()


logging.basicConfig(level=logging.DEBUG,
                    filename='../logs/CodeCraft-2019.log',
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a')









def cross2road(crossLine):

	# print("crossLine=",crossLine)
	roadLine = []
	index = len(crossLine)
	for i in range (0,index-1):
		# print ( crossLine[i],crossLine[i+1] )
		startCross = fS.crossData[crossLine[i]-1]
		endCross = fS.crossData[crossLine[i+1]-1]

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


	preAnswer = []

	for data in sch.targetList:
		
		oneCar = [data[0],data[4]]

		crossLine = CNW.createNetwork(fS.carData,fS.roadData,fS.crossData,data[1],data[2])
		roadLine = cross2road(crossLine)

		oneCar.extend(roadLine)
		
		# print ( "oneCar=",oneCar )

		preAnswer.append(oneCar)

	fS.finalAnswer = sch.fin_scheduler(preAnswer)


def main():

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

########################################
	# fileSystem init



	fS.load_data(road_path,cross_path,car_path)


	sch.pre_scheduler(fS.carData,fS.roadData,fS.crossData)

	createAnswer()



	fS.save_answer(answer_path)

##########################################




if __name__ == "__main__":
	main()

