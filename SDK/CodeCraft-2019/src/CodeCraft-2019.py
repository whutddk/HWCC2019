# @File Name: CodeCraft-2019.py
# @File Path: K:\work\dark+PRJ\HWCC2019\SDK\CodeCraft-2019\src\CodeCraft-2019.py
# @Author: 29505
# @Date:   2019-03-17 23:16:45
# @Last Modified by:   29505
# @Last Modified time: 2019-03-18 00:07:29
# @Email: 295054118@whut.edu.cn

import logging
import sys
import re

car_path = '../config/car.txt'
road_path = '../config/road.txt'
cross_path = '../config/cross.txt'
answer_path = '../config/answer.txt'


carData = []
roadData = []
crossData = []

finalAnswer = []







logging.basicConfig(level=logging.DEBUG,
                    filename='../../logs/CodeCraft-2019.log',
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a')



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
			carID = string[1:po]

			string = string[po+2:]
			po = string.find(',')
			startPos = string[:po]

			string = string[po+2:]
			po = string.find(',')
			endPos = string[:po]

			string = string[po+2:]
			po = string.find(',')
			maxSpeed = string[:po]

			string = string[po+2:]
			po = string.find(')')
			takeoffTime = string[:po]
			# print (takeoffTime)

			carData.append([carID,startPos,endPos,maxSpeed,takeoffTime])
		# print (carData)



	with open(road_path,'r') as roadFile:
		for data in roadFile.readlines():
			if data[0] == '#':
				continue

			string = data
			po = string.find(',')
			roadID = string[1:po]

			string = string[po+2:]
			po = string.find(',')
			roadLength = string[:po]

			string = string[po+2:]
			po = string.find(',')
			maxSpeed = string[:po]

			string = string[po+2:]
			po = string.find(',')
			chnNum = string[:po]

			string = string[po+2:]
			po = string.find(',')
			startID = string[:po]

			string = string[po+2:]
			po = string.find(',')
			endID = string[:po]

			string = string[po+2:]
			po = string.find(')')
			doubleBool = string[:po]
			# print (doubleBool)

			roadData.append([roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool])
		# print (roadData)

	with open(cross_path,'r') as crossFile:
		for data in crossFile.readlines():
			if data[0] == '#':
				continue

			string = data
			po = string.find(',')
			crossID = string[1:po]

			string = string[po+2:]
			po = string.find(',')
			roadID1 = string[:po]

			string = string[po+2:]
			po = string.find(',')
			roadID2 = string[:po]

			string = string[po+2:]
			po = string.find(',')
			roadID3 = string[:po]

			string = string[po+2:]
			po = string.find(')')
			roadID4 = string[:po]
			# print (doubleBool)

			crossData.append([crossID,roadID1,roadID2,roadID3,roadID4])
		print (crossData)


def save_result():
	global finalAnswer

	pass
	# data = json.dumps(trueTable)
	# with open( answer_path,'w') as ttFile:
	# 	ttFile.write(data)





























# def main():
#     if len(sys.argv) != 5:
#         logging.info('please input args: car_path, road_path, cross_path, answerPath')
#         exit(1)

#     car_path = sys.argv[1]
#     road_path = sys.argv[2]
#     cross_path = sys.argv[3]
#     answer_path = sys.argv[4]

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



