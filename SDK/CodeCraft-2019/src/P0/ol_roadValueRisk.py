# -*- coding: utf-8 -*-
# @File Name: ol_roadValueRisk.py
# @File Path: /home/whutddk/下载/HWCC2019/SDK/CodeCraft-2019/src/ol_roadValueRisk.py
# @Author: Ruige_Lee
# @Date:   2019-03-21 16:15:16
# @Last Modified by:   whutddkUbuntu16
# @Last Modified time: 2019-03-30 10:30:17
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

		self.value = rdSpeed*(0) - (rdLength*1) + (rdChnNum*0)

		return self.value



