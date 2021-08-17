import math
import itertools


w1_=1 #wieght
w2_=5
Py_=14 # duration of project in months
D_ = 14 #total duration of temporary facility


y=1 # phase numeber
m=2 #nuber of phases
n=11 #numer of facility


facility_name = ["site office","labour shed","security shed","site canteen","Toilets","watertank","Batching plant","Warehouse","QC lab","Power house","Parking"]

format=[("name","fijy1","tijy1","Rikl1","Pijy1","Sy1","uijy1")]

fijy1 = [10,5,5,10,10,10]#trip frequency
fijy2 = [5,5,2,1,3]#trip frequency
tijy1 = [0,0,0,100,500,0] #transportaion cost
tijy2 = [0,0,100,0,0] #transportaion cost
Rikl1 = [500,10000,200,20000,10000,5000] #relocation cost
Rikl2 = [10000,200,5000,1000,200] #relocation cost
Pijy1 = [500,500,0,1000,1000,500] # penalty
Pijy2 = [0,0,200,1000,0] # penalty
Sy1 = [0,0,0,2,7,0] # material delay in days
Sy2 = [0,0,1,0,0] # material delay in days
uijy1 = [0,0,0,2,1,0] # transportation delay in hrs
uijy2 = [0,0,2,0,0] # transportation delay in hrs


Ci= 3309960#site logistic cost
da = 1 # duration required for completion of each activity

#ekl=[112,112,112,112,112,112,112,112,112,112,112,112] # distance from the facility to the site

sitePosition =[(30, 120),(55, 120),(80, 120),(105, 120),(130, 120),(155, 120),(180, 120),(30, 75),(55, 75),(80, 75),(105, 75),( 130, 75),(155, 75),(180, 75),(30, 45),(55, 45),(80, 45),( 105, 45),(130, 45),( 155, 45),( 180, 45),(15, 0),(30, 0),(55, 0),(80, 0),(105, 0),( 130, 0),( 155, 0),(180, 0)]

emptySlotPosition1=[( -5, 130),(-5, 85),(-5, 65),(215, 125),( 215, 95),(215, 65)]
emptySlotPosition2=[( -5, 45),(-5, 25),(-5, 5),(215, 35),( 215, 5)]


def findObjectiveFunction(distance,facility_data):
  f1f = facility_data[1] * facility_data[2] * distance * Py_ + Ci + facility_data[3] + facility_data[4]
  f2f = da + facility_data[5] + facility_data[1] * facility_data[6] * distance * Py_ + D_
  return f1f,f2f

def calculateDistance(x1,y1,x2,y2):
   x=x1-x2
   y=y1-y2
   return math.sqrt(x*x + y*y)

def totalObjectionValueForPlacement(facilities_data):
  totalObjectionValue1 = 0
  totalObjectionValue2 = 0
  count=0
  for eachFacility in facilities_data:
    for eachsite in sitePosition:
      distance = calculateDistance(eachsite[0],eachsite[1],emptySlotPosition1[count][0],emptySlotPosition1[count][1])
      f1,f2=findObjectiveFunction(distance, eachFacility)
      totalObjectionValue1+= f1
      totalObjectionValue2 += f2
    count+=1
  return totalObjectionValue1,totalObjectionValue2

def swapPositions(list, pos1, pos2):
  list[pos1], list[pos2] = list[pos2], list[pos1]
  return list

def getAllPossiblePlacements(myList):
  return list(itertools.permutations(myList,len(myList)))



def main(important_facility_data,less_important_facility_data):
  min = 0
  bestImportantPlacement = []
  bestCost1 = 0
  bestTime1 = 0
  for eachPossiblePlacement in getAllPossiblePlacements(important_facility_data):
    totalObjectionValue1, totalObjectionValue2, = totalObjectionValueForPlacement(eachPossiblePlacement)
    # print("each iteration objection value(important)",totalObjectionValue)
    if (min == 0):
      min = totalObjectionValue1 + totalObjectionValue2
      bestImportantPlacement = eachPossiblePlacement
      bestCost1 = totalObjectionValue1
      bestTime1 = totalObjectionValue2
    if (totalObjectionValue1 + totalObjectionValue2 < min):
      min = totalObjectionValue1 + totalObjectionValue2
      bestCost1 = totalObjectionValue1
      bestTime1 = totalObjectionValue2
      bestImportantPlacement = eachPossiblePlacement

  min = 0
  bestCost2 = 0
  bestTime2 = 0
  bestLessImportantPlacement = []
  for eachPossiblePlacement in getAllPossiblePlacements(less_important_facility_data):
    totalObjectionValue1, totalObjectionValue2 = totalObjectionValueForPlacement(eachPossiblePlacement)
    # print("each iteration objection value(less important)",totalObjectionValue)
    if (min == 0):
      min = totalObjectionValue1 + totalObjectionValue2
      bestCost1 = totalObjectionValue1
      bestTime1 = totalObjectionValue2
      bestLessImportantPlacement = eachPossiblePlacement
    if (totalObjectionValue1 + totalObjectionValue2 < min):
      min = totalObjectionValue1 + totalObjectionValue2
      bestCost1 = totalObjectionValue1
      bestTime1 = totalObjectionValue2
      bestLessImportantPlacement = eachPossiblePlacement

  return bestCost1+ bestCost2 , bestTime1 + bestTime2 , bestImportantPlacement , bestLessImportantPlacement

