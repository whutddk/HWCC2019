# -*- coding: utf-8 -*-
# @File Name: ol_preProduce.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK_python\CodeCraft-2019\src\ol_preProduce.py
# @Author: Ruige_Lee
# @Date:   2019-04-03 09:50:38
# @Last Modified by:   Ruige_Lee
# @Last Modified time: 2019-04-03 10:07:39
# @Email: 295054118@whut.edu.cn"

# @File Name: ol_preProduce.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK_python\CodeCraft-2019\src\ol_preProduce.py
# @Author: 29505
# @Date:   2019-04-02 23:13:28
# @Last Modified by:   29505
# @Last Modified time: 2019-04-02 23:54:16
# @Email: 295054118@whut.edu.cn
# @page: https://whutddk.github.io/




import sys


class preProduce():

	def __init__(self):
		pass


	def dealData(self,carData,roadData,crossData,presetAnswerData):

		# 分析车的总数量，优先车，普通车，预置车的数量（有重合）
		# 分析道路数量，
		# 分析岔道数量

		# 需要获得预置车的出发时间，以及密度
# [carID,startPos,endPos,maxSpeed,takeoffTime,isPri,isPreSet]
# [preSetCarID,startTime,roadId1,roadId2........]

		# print ( "totalCarNum = ",len(carData) )


		# preSetSpeed = []
		# speed16 = 0
		# speed4 = 0
		# # print ("presetAnswerData=",presetAnswerData)
		# for car in carData:
		# 	if ( car[3] == 16 and car[6] == 1 ):
		# 		speed16 = speed16 + 1

		# 	if ( car[3] == 4 and car[6] == 1 ):
		# 		speed4 = speed4 + 1
		# 	# if  startTime in preSetTakeoffTime:
		# 	# 	pass
		# 	# else:
		# 	# 	preSetTakeoffTime.append(startTime)

		# print ( "speed16=",speed16 )
		# print ( "speed4=",speed4 )

		# print( "preSetTakeoffTime=",preSetTakeoffTime )
		# print( "preSetCarNum = ",len(presetAnswerData) )



