
import math
import random
#The formulas used below were made in desmos:
#https://www.desmos.com/calculator/tngpylcgmn
class dthreshold:
	#Calculates the decision threshold based on the quadratic function (y = ax^2) where thresh = y, 
	#"a" is a calculated value based on the "pmed" (medium price) and coeficient "crdr" (resources, dificulty, rarity)
	def thresh_calc(pmed:int, crdr:int ): 
		a = 1/(pmed*crdr)
		thresh = a*pmed**2
		return thresh
	
	#Returns a random threshold for the client decision based on the calculated threshold and an interval "d" which is a function of pmed
	def random_thresh_calc(thresh, pmed):
		#The value 0.02 was adjusted to obtain better results 
		d = 0.02*pmed
		#Random value between 0 and 1 multiplied by "d"
		drand = random.random() * d
		#Chooses a random number from an interval between thresh - (drand - pmed/70) and thresh + drand
		#The left part of the if statement will reflect the max_price below pmed
		#The right part of the if statement will reflect the max_price above pmed
		#The pmed/70 was used to better limit the max_price below pmed 
		r_thresh = (thresh-(drand-pmed/70)) if random.randint(0,1) == 0 else (thresh + drand)
		return r_thresh

	#Returns client decision to buy or not to buy based on the random threshold obtained and the respective max_price by using the reverse of the quadratic function 
	def client_decision(pmed:int, crdr:int, player_price) -> bool:
		#Obtains the initial threshold value
		thresh = dthreshold.thresh_calc(pmed, crdr)
		#Obtains the random threshold value
		r_thresh = dthreshold.random_thresh_calc(thresh, pmed)
		a = 1/(pmed*crdr)
		d = 0.02*pmed
		#Calculates max_price using the reverse quadratic function (x = sqrt(y/a)) 
		max_price = math.sqrt((r_thresh)/a)
		#Returns true or false, and the max price
		return (max_price >= player_price, max_price)
