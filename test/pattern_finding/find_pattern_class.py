#klasse zum finden von pattern
class Pattern:
	
	coords = []
	possible_pattern = []
	
	AllPatterns = [] #fütter array mit patterns
	# mögliches array AllPatterns[0] =
	#0 0 0
	#1 1 1
	#0 0 0
	varianz = 0.2
	FirstX = 0
	FirstY = 0
	FirstZ = 0
	
	def __init__(self,coords):
		self.coords = coords
		self.FirstX = coords[0](1)
		self.FirstY = coords[0](2)
		self.FirstZ = coords[0](3)
		
		
	#erstelle mögliches pattern
	#drittel das coord array, da immer nur ein drittel verglichen wird
	#von
	#0 0 0
	#1 1 1
	#0 0 0
	#wird zunächst nur die erste SPALTE erstellt, dann die zweite, ...
	def createPossiblePattern(self):		
		length = len(self.coords)
		dr_len = int(length/3)
		
		firstArr = self.coords[0:dr_len]
		secondArr = self.coords[dr_len+1:dr_len*2]
		thirdArr = self.coords[dr_len*2+1:dr_len*3-1]
		
		self.SetPattern(firstArr)
		self.SetPattern(secondArr)
		self.SetPattern(thirdArr)	
	
	#hier wird das pattern erstellt	
	def SetPattern(self, array):		
		xArr = 0
		yArr = 0
		zArr = 0
		
		xLast = 0
		
		for tupel in array:
			#schau nur an, was sich am meisten geändert hat
			xArr += tupel(1) # > 0 ? links rum  <0 rechts rum
			yArr += tupel(2)
			zArr += tupel(3)
		
		#erstelle sowohl pos als auf neg werte
		#somit egal ob coord neg/pos waren ?!
		deltaX_neg = self.FirstX - xArr
		deltaX_pos = self.FirstX + xArr
		deltaY_neg = self.FirstY - yArr
		deltaY_pos = self.FirstY + yArr
		detlaZ_neg = self.FirstZ - zArr
		detlaZ_pos = self.FirstZ + zArr
		
		#prüfe ob pos/neg wert gräßer/kleiner als varianz ist
		#wenn ja -> setze 1 im möglichen pattern
		#-1 für hoch/runter links/rechts vor/zurück fehlt noch
		#erstmal so testen :P
		if deltaX_pos > self.varianz or deltaX_neg < self.varianz:
			self.possible_pattern[0][0] = 1
		else:
			self.possible_pattern[0][0] = 0
		if deltaY_pos > self.varianz or deltaY_neg < self.varianz:
			self.possible_pattern[1][0] = 1
		else:
			self.possible_pattern[1][0] = 0
		if deltaZ_pos > self.varianz or detlaZ_neg < self.varianz:
			self.possible_pattern[2][0] = 1
		else:
			self.possible_pattern[2][0] = 0	
		
	#eigentliche methode, die aufgerufen wird
	#rückgabewerte fehlen noch
	def findPattern(self):
		self.createPossiblePattern()
		found = false;
		for arr in self.AllPatterns:
			if (arr==self.possible_pattern).all():
				found = true
				
		if found == false:
			print "error"
		else:
			print "pattern found"