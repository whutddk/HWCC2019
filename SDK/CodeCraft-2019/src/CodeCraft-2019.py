# -*- coding: utf-8 -*-
# @File Name: CodeCraft-2019.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\CodeCraft-2019.py
# @Author: Ruige_Lee
# @Date:   2019-03-25 08:50:11
# @Last Modified by:   Ruige_Lee
# @Last Modified time: 2019-03-25 12:06:40
# @Email: 295054118@whut.edu.cn"

# @File Name: CodeCraft-2019.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\CodeCraft-2019.py
# @Author: Ruige_Lee
# @Date:   2019-03-19 11:00:06
# @Last Modified by:   29505
# @Last Modified time: 2019-03-24 22:36:28
# @Email: 295054118@whut.edu.cn
# @page: https://whutddk.github.io/


# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]
# [crossID,roadID1,roadID2,roadID3,roadID4]
# [carID,startPos,endPos,maxSpeed,takeoffTime]

import logging
import sys

import ol_fileSystem 
import ol_crossNetWorkOnline
import ol_scheduler


fS = ol_fileSystem.fS() 
CNW = ol_crossNetWorkOnline.crossNetwork()
sch = ol_scheduler.scheduler()


logging.basicConfig(level=logging.DEBUG,
                    filename='../logs/CodeCraft-2019.log',
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a')







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

	CNW.crossNetwork_init(fS.carData,fS.roadData,fS.crossData)

	CNW.createNetwork()

##########################################




if __name__ == "__main__":
	main()

