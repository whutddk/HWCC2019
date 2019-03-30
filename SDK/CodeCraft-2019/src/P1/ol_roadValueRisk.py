# -*- coding: utf-8 -*-
# @File Name: ol_roadValueRisk.py
# @File Path: M:\MAS2\dark_PRJ\HWCC2019\SDK\CodeCraft-2019\src\ol_roadValueRisk.py
# @Author: Ruige_Lee
# @Date:   2019-03-21 16:15:16
# @Last Modified by:   Ruige_Lee
# @Last Modified time: 2019-03-25 11:18:25
# @Email: 295054118@whut.edu.cn"




import sys

# [roadID,roadLength,maxSpeed,chnNum,startID,endID,doubleBool]


class roadValue():

	def __init__(self):
		self.value = 0

		pass


	def RD_Value(self,rdLength,rdSpeed,rdChnNum):
		# 默认长度是速度2~5倍
		self.value = 0

		self.value = rdSpeed*(0) - (rdLength*0) + (rdChnNum*1)

		return self.value



