# -*- coding: utf-8 -*-
# @File Name: CodeCraft-2019.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK_python\CodeCraft-2019\src\CodeCraft-2019.py
# @Author: Ruige_Lee
# @Date:   2019-04-02 09:43:48
# @Last Modified by:   Ruige_Lee
# @Last Modified time: 2019-04-02 10:30:32
# @Email: 295054118@whut.edu.cn"

# @File Name: CodeCraft-2019.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK_python\CodeCraft-2019\src\CodeCraft-2019.py
# @Author: 29505
# @Date:   2019-04-01 23:19:28
# @Last Modified by:   29505
# @Last Modified time: 2019-04-01 23:45:57
# @Email: 295054118@whut.edu.cn
# @page: https://whutddk.github.io/

# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]
# [crossID,roadID1,roadID2,roadID3,roadID4]
# [carID,startPos,endPos,maxSpeed,takeoffTime,isPri,isPreSet]
# [preSetCarID,startTime,roadId1,roadId2........]

import logging
import sys

import ol_fileSystem 
import ol_crossNetWorkOnline

fS = ol_fileSystem.fS() 
CNW = ol_crossNetWorkOnline.crossNetwork()



logging.basicConfig(level=logging.DEBUG,
					filename='../logs/CodeCraft-2019.log',
					format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
					datefmt='%Y-%m-%d %H:%M:%S',
					filemode='a')


def main():
	if len(sys.argv) != 6:
		logging.info('please input args: car_path, road_path, cross_path, answerPath')
		exit(1)

	car_path = sys.argv[1]
	road_path = sys.argv[2]
	cross_path = sys.argv[3]
	preset_answer_path = sys.argv[4]
	answer_path = sys.argv[5]

	logging.info("car_path is %s" % (car_path))
	logging.info("road_path is %s" % (road_path))
	logging.info("cross_path is %s" % (cross_path))
	logging.info("preset_answer_path is %s" % (preset_answer_path))
	logging.info("answer_path is %s" % (answer_path))

# to read input file
# process
# to write output file


########################################
	# fileSystem init
	fS.load_data(car_path,road_path,cross_path,preset_answer_path)

	CNW.crossNetwork_init(fS.carData,fS.roadData,fS.crossData,fS.presetAnswerData)

	# roadLine = CNW.createNetwork()

	# fS.finalAnswer = roadLine
	# print (roadLine)
	# fS.save_answer(answer_path)
##########################################





if __name__ == "__main__":
	main()