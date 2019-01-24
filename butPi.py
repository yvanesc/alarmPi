#!/usr/bin/bash
import git
import sys, os

def croi():
	print("X")
def rect():
	print("Rect")
def tria():
	print("triangle")
def rond():
	print("O") 
def low():
	print ("LOW")
	g = git.Git('/home/pi/alarmPi')
	g.pull('origin','master')
	# restart python soft to update change
	os.execl('/home/pi/stopRunMe.sh', '')
def high():
	print("HIGH")