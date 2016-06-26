#__author__ = 'mjwei'

from enum import Enum
import os
import operator
import random

class Category(Enum):
	Face ='face'
	CatFace ='face'
	MonkeyFace = 'face'
	Transport = 'transport'
	Symbol = 'symbol'
	Animal = 'animal'

class Emoji(Enum):
	Grin = ('\U0001F601', Category.Face.name, ['happy','joy','grad'])
	Tear = ('\U0001F602', Category.Face.name, ['happy','joy','grad'])
	Smile = ('\U0001F603', Category.Face.name, ['happy','joy','grad','smiling'])
	Mouth = ('\U0001F604', Category.Face.name, ['happy','joy','grad','smiling'])
	Sweat = ('\U0001F605', Category.Face.name, ['happy','joy','grad','smiling'])
	XD = ('\U0001F606', Category.Face.name, ['happy','joy','grad','smiling'])
	Wink = ('\U0001F609', Category.Face.name, ['happy','joy','grad','smiling'])
	Savor = ('\U0001F60B', Category.Face.name, ['happy','joy','grad','smiling'])
	Relieve = ('\U0001F60C', Category.Face.name, ['none'])
	HeartShaped = ('\U0001F60D', Category.Face.name, ['love','happy','joy','grad','smiling'])
	Smirk = ('\U0001F60F', Category.Face.name, ['none'])
	Unamused = ('\U0001F612', Category.Face.name, ['none'])
	ColdSweat = ('\U0001F613', Category.Face.name, ['none'])
	Pensive = ('\U0001F614', Category.Face.name, ['none'])
	Confound = ('\U0001F616', Category.Face.name, ['confuse','puzzle'])
	Kiss = ('\U0001F618', Category.Face.name, ['none'])
	Tongue = ('\U0001F61C',Category.Face.name, ['wink','stuck-out'])
	ClosedEyes = ('\U0001F61D', Category.Face.name, ['none'])
	Disappoint = ('\U0001F61E', Category.Face.name, ['none'])
	Angry = ('\U0001F620', Category.Face.name, ['none'])
	Pout = ('\U0001F621', Category.Face.name, ['none'])
	SadCry = ('\U0001F622', Category.Face.name, ['none'])
	Worry = ('\U0001F623', Category.Face.name, ['worried','persevere','persevering'])
	Triumph = ('\U0001F624', Category.Face.name, ['none'])
	Relieved = ('\U0001F625', Category.Face.name, ['disappoint'])
	Fear = ('\U0001F628', Category.Face.name, ['none'])
	Weary = ('\U0001F629', Category.Face.name, ['none'])
	Sleep = ('\U0001F62A', Category.Face.name, ['none'])
	Tired = ('\U0001F62B', Category.Face.name, ['none'])
	LoudCry = ('\U0001F62D', Category.Face.name, ['none'])
	Scream = ('\U0001F631', Category.Face.name, ['fear','shock','scare'])
	Astonished = ('\U0001F632', Category.Face.name, ['shock'])
	Flushed = ('\U0001F633', Category.Face.name, ['blush'])
	Dizzy = ('\U0001F635', Category.Face.name, ['none'])
	MedicalMask = ('\U0001F637', Category.Face.name, ['ill','sick'])
	GrinCat = ('\U0001F638', Category.CatFace.name, ['happy','joy','grad'])
	TearCat = ('\U0001F639', Category.CatFace.name, ['happy','joy','grad'])
	SmileCat = ('\U0001F63A', Category.CatFace.name, ['happy','joy','grad','smiling'])
	HeartShapedCat = ('\U0001F63B', Category.CatFace.name, ['love','happy','joy','grad','smiling'])
	WrySmileCat = ('\U0001F63C', Category.CatFace.name, ['none'])
	KissCat = ('\U0001F63D', Category.CatFace.name, ['none'])
	PoutCat = ('\U0001F63E', Category.CatFace.name, ['none'])
	SadCryCat = ('\U0001F63F', Category.CatFace.name, ['none'])	
	NoGoodGesture = ('\U0001F645', Category.Face.name, ['object','deny'])
	OkGesture = ('\U0001F646', Category.Face.name, ['agree','yes'])
	Bowing = ('\U0001F647', Category.Face.name, ['kneel'])
	SeeNoEvilMonkey = ('\U0001F648', Category.MonkeyFace.name, ['none'])
	HearNoEvilMonkey = ('\U0001F649', Category.MonkeyFace.name, ['none'])
	SpeakNoEvilMonkey = ('\U0001F64A', Category.MonkeyFace.name, ['none'])
	RaiseOneHand = ('\U0001F64B', Category.Face.name, ['raising'])
	RaiseBothHand = ('\U0001F64C', Category.Face.name, ['raising'])
	Frown = ('\U0001F64D', Category.Face.name, ['none'])
	FoldedHands = ('\U0001F64F', Category.Face.name, ['none'])
	Rocket = ('\U0001F680', Category.Transport.name, ['none'])
	RailwayCar = ('\U0001F683', Category.Transport.name, ['none'])
	HighSpeed = ('\U0001F684', Category.Transport.name, ['train'])
	HighSpeedBullet = ('\U0001F685', Category.Transport.name, ['train'])
	Metro = ('\U0001F687', Category.Transport.name, ['none'])
	Station = ('\U0001F689', Category.Transport.name, ['none'])
	Bus = ('\U0001F68C', Category.Transport.name, ['none'])
	BusStop = ('\U0001F68F', Category.Transport.name, ['none'])
	Ambulance = ('\U0001F691', Category.Transport.name, ['none'])
	FireEngine = ('\U0001F692', Category.Transport.name, ['none'])
	PoliceCar = ('\U0001F693', Category.Transport.name, ['none'])
	Taxi = ('\U0001F695', Category.Transport.name, ['none'])
	Automobile = ('\U0001F697', Category.Transport.name, ['car'])
	RecreationalVehicle = ('\U0001F699', Category.Transport.name, ['none'])
	DeliveryTruck = ('\U0001F69A', Category.Transport.name, ['none'])
	Ship = ('\U0001F6A2', Category.Transport.name, ['none'])
	Speedboat = ('\U0001F6A4', Category.Transport.name, ['none'])
	TrafficLight = ('\U0001F6A5', Category.Transport.name, ['horizontal'])
	ConstructionSign = ('\U0001F6A7', Category.Transport.name, ['none'])
	RevolvingLight = ('\U0001F6A8', Category.Transport.name, ['none'])
	TriangularFlag = ('\U0001F6A9', Category.Transport.name, ['on post'])
	Door = ('\U0001F6AA', Category.Transport.name, ['none'])
	NoEntry = ('\U0001F6AB', Category.Symbol.name, ['none'])
	SmokingSymbol = ('\U0001F6AC', Category.Symbol.name, ['sign'])
	NoSmokingSymbol = ('\U0001F6AD', Category.Symbol.name, ['sign'])
	Bicycle = ('\U0001F6B2', Category.Transport.name, ['sign'])
	Pedestrian = ('\U0001F6B6', Category.Transport.name, ['sign'])
	MenSymbol = ('\U0001F6B9', Category.Symbol.name, ['sign'])
	WomenSymbol = ('\U0001F6BA', Category.Symbol.name, ['sign'])
	Restroom = ('\U0001F6BB', Category.Symbol.name, ['bathroom'])
	BabySymbol = ('\U0001F6BC', Category.Symbol.name, ['sign'])
	Toilet = ('\U0001F6BD', Category.Symbol.name, ['bathroom','restroom'])
	WaterCloset = ('\U0001F6BE', Category.Symbol.name, ['wc'])
	Bath = ('\U0001F6C0', Category.Symbol.name, ['sign'])
	Rat = ('\U0001F400', Category.Animal.name, ['none'])
	Mouse = ('\U0001F401', Category.Animal.name, ['none'])
	Ox = ('\U0001F402', Category.Animal.name, ['none'])
	WaterBuffalo = ('\U0001F403', Category.Animal.name, ['none'])
	Cow = ('\U0001F404', Category.Animal.name, ['none'])
	Tiger = ('\U0001F405', Category.Animal.name, ['none'])
	Leopard = ('\U0001F406', Category.Animal.name, ['none'])
	Rabbit = ('\U0001F407', Category.Animal.name, ['none'])
	Cat = ('\U0001F408', Category.Animal.name, ['none'])
	Dragon = ('\U0001F409', Category.Animal.name, ['none'])
	Crocodile = ('\U0001F40A', Category.Animal.name, ['none'])
	Whale = ('\U0001F40B', Category.Animal.name, ['none'])
	Ram = ('\U0001F40F', Category.Animal.name, ['none'])
	Goat = ('\U0001F410', Category.Animal.name, ['none'])
	Rooster = ('\U0001F413', Category.Animal.name, ['none'])
	Dog = ('\U0001F415', Category.Animal.name, ['none'])
	Pig = ('\U0001F416', Category.Animal.name, ['none'])
	Camel = ('\U0001F42A', Category.Animal.name, ['none'])


def to_emoji(enter):

	flag = False
	for emoji in Emoji:
		#find the corresponding word at Emoji.name
		if(enter.lower().find(emoji.name.lower()) >= 0 or emoji.name.lower().find(enter.lower()) >= 0):
			flag = True
			print((emoji.value)[0])
			break

		#find the corresponding word at Emoji.value[2] which is extra description
		emotion_tup = emoji.value
		for description in emotion_tup[2]:
			if(enter.lower().find(description) >= 0 or description.find(enter.lower()) >=0):
				flag = True
				print((emoji.value)[0])
				break

		if flag:
			break
	
	if flag is not True:
		#random select from the emoji list with same category
		emoji_list = searchCategory(enter)
		if(len(emoji_list)>0):
			flag =True
			print(random.choice(emoji_list))

	#if no corresponding emoji can be found
	if flag is not True:
		print('\U0001F631')

#find the corresponding word at category name
def searchCategory(enter):

	emoji_list = []
	for emoji in Emoji:
		category=(emoji.value)[1]
		if(category.lower().find(enter.lower()) >=0):
			emoji_list.append((emoji.value)[0])

	return emoji_list	
									

while True:
	enter = input("Please enter here :")
	if enter=='':
		break
	to_emoji(enter.lower())



