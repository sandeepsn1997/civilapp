import math
import itertools



w1_=1 #wieght
w2_=5
Py_=0.5 # duration of project activity phase y in months
D_ = 0.1 #duration of temporary facility


y=1 # phase numberw1_
m=2 #number of phases
n=11 #number of facility


facility_name = ["site office","labour shed","security shed","site canteen","Toilets","watertank","Batching plant","Warehouse","QC lab","Power house","Parking"]

format=[("name","fijy1","tijy1","Rikl1","Pijy1","Sy1","uijy1")]

fijy1 = [2,3,1,3,2,0]#trip frequency
fijy2 = [4,3,2,1,1]#trip frequency
tijy1 = [0,0,0,100,500,0] #transportaion cost
tijy2 = [0,0,100,0,0] #transportaion cost
Rikl1 = [500,120,200,0,0,80] #relocation cost
Rikl2 = [0,0,150,0,0] #relocation cost
Pijy1 = [80,90,0,0,0,0] # penalty
Pijy2 = [0,0,200,100,0] # penalty

Sy1 = [0.03,0.03,0.03,0.0998,0.065,0.0328] # installation time for temprory facility
Sy2 = [0.03,0.065,0.03,0.03,0.03] # installation time temprory facility
uijy1 = [0,0,0,0,0,0] # time taken for transportation of material
uijy2 = [0.00045,0.0000913,0.00034,0.00022,0.00018] # time taken for transportation of material

#Ci= 283750#setup cost1
Ci= 204230#setup cost2


#ekl=[112,112,112,112,112,112,112,112,112,112,112,112] # distance from the facility to the site
#site 1: draw
#sitePosition =[(50,255),(95,255),(150,225),(190,255),(220,255),(275,255),(320,255),(50,160),(95,160),(150,160),(190,160),(220,160),(275,160),(320,160),(50,120),(95,120),(150,120),(190,120),(220,120),(275,120),(320,120),(50,20),(95,20),(150,20),(190,20),(220,20),(275,20),(320,20)]
#emptySlotPosition1=[(-40,275),(-40,135),(-35,30),(2,170),( 2,130),(6,10)]
#emptySlotPosition2=[(370,265),(380,200),(380,140),( 380,75),(370,25)]
#site 2: draw1
sitePosition =[(50,255),(95,255),(150,255),(275,255),(320,255),(50,160),(95,160),(150,160),(320,160),(370,160),(50,120),(95,120),(150,120),(320,120),(370,120),(50,20),(95,20),(150,20),(320,20),(370,20)]
emptySlotPosition1=[(-40,275),(-40,135),(-35,30),(205,255),(195,165),(230,155)]
emptySlotPosition2=[(375,265),(200,112),(245,115),(245,15),( 200,25)]


def findObjectiveFunction(distance,facility_data):
  f1f = facility_data[1] * facility_data[2] * distance * Py_ + Ci + facility_data[3] + facility_data[4]
  f2f = facility_data[5] + facility_data[1] * facility_data[6] * distance * Py_ + D_
  return f1f,f2f

def calculateDistance(x1,y1,x2,y2):
   x=x1-x2
   y=y1-y2
   return math.sqrt(x*x + y*y)

def totalObjectionValueForPlacement(facilities_data):
  totalObjectionValue1=0
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



def main(important_facility_data,less_important_facility_data,D,P):
  global Py_
  Py_=P
  global D_
  D_=D
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
