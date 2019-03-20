# -*- coding: utf-8 -*-
# @File Name: crossNetWorkOnline.py
# @File Path: K:\work\dark+PRJ\HWCC2019\SDK\CodeCraft-2019\src\crossNetWorkOnline.py
# @Author: Ruige_Lee
# @Date:   2019-03-19 11:00:06
# @Last Modified by:   29505
# @Last Modified time: 2019-03-20 23:30:12
# @Email: 295054118@whut.edu.cn"



import sys


road_path = '../../config/road.txt'
cross_path = '../../config/cross.txt'


global roadData
global crossData

roadData = []
crossData = []



class crossNetwork():

	






	crossCollection = []

	def checkroadVaild(self,startCross,roadId):
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
				print ( "checkroadVaild=Return" ,result)
				crossCollection.remove(vaildCross)
				return result


		# print ( "checkroadVaild=Return" ,-1)
		return -1



	def findNextCrossId(self,crossId):
		crossInfo = crossData[crossId-1]
		print ("crossInfo=",crossInfo)

	# 检查路标
		nextCross1 = checkroadVaild(crossInfo[0],crossInfo[1])
		nextCross2 = checkroadVaild(crossInfo[0],crossInfo[2])
		nextCross3 = checkroadVaild(crossInfo[0],crossInfo[3])
		nextCross4 = checkroadVaild(crossInfo[0],crossInfo[4])

		return nextCross1,nextCross2,nextCross3,nextCross4





	def simpleShortestWay(self,input):


		global crossCollection

		crossCollection = crossData.copy()
		roadList = []

		startPos = input

		roadList.append([[startPos]])
		del crossCollection[startPos-1]


		# print (roadList[0])
		while(1):
			OneCrossLever = []
			lastLever = roadList[len(roadList)-1]

			for root in lastLever:
				print ("root=",root)
				for crossId in root:
					print ("crossId=",crossId)
					# print ("crossId=",crossId)
					if ( crossId == -1 ):
						cross1,cross2,cross3,cross4 = -1,-1,-1,-1
					else:
						cross1,cross2,cross3,cross4 = findNextCrossId(crossId)

						leavesCheck = []

						if ( cross1 != -1 ):
							leavesCheck.append(cross1)
						if ( cross2 != -1 ):	
							leavesCheck.append(cross2)
						if ( cross3 != -1 ):	
							leavesCheck.append(cross3)
						if ( cross4 != -1 ):	
							leavesCheck.append(cross4)

						
						OneCrossLever.append(leavesCheck)


			
			# print ( "路口集合=",crossCollection )



			if ( len(crossCollection) == 0 ):

				roadList.append(OneCrossLever)


				return roadList



			roadList.append(OneCrossLever)

		pass





	def createNetwork(self):

		# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]
		# [crossID,roadID1,roadID2,roadID3,roadID4]
		
		

		output = []

		



		for i in range(1,65):

			print ( "Sort i= ",i )


			output.append(simpleShortestWay(i))

		with open( "./crossNetwork.json",'w') as networkFile:
			data = json.dumps(output)
			networkFile.write(data)




		pass













