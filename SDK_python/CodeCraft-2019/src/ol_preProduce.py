# @File Name: ol_preProduce.py
# @File Path: K:\work\dark+PRJ\HWCC2019\SDK_python\CodeCraft-2019\src\ol_preProduce.py
# @Author: 29505
# @Date:   2019-04-02 23:13:28
# @Last Modified by:   29505
# @Last Modified time: 2019-04-02 23:47:46
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

		preSetTakeoffTime = []
		# print (presetAnswerData)
		for car in presetAnswerData:
			startTime = car[1]
			if  startTime in preSetTakeoffTime:
				pass
			else:
				preSetTakeoffTime.append(startTime)
		# print( "preSetTakeoffTime=",preSetTakeoffTime )



