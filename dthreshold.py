
import math
import random

class dthreshold:

	def thresh_calc(pmed:int, crdr:int ):
		a = 1/(pmed*crdr)
		thresh = a*pmed**2
		return thresh

	def random_thresh_calc(thresh, pmed):
		d = 0.02*pmed
		drand = random.random() * d
		r_thresh = (thresh-(drand-pmed/70)) if random.randint(0,1) == 0 else (thresh + drand)
		return r_thresh

	def client_decision(pmed:int, crdr:int, player_price) -> bool:
		thresh = dthreshold.thresh_calc(pmed, crdr)
		r_thresh = dthreshold.random_thresh_calc(thresh, pmed)
		a = 1/(pmed*crdr)
		d = 0.02*pmed
		max_price = math.sqrt((r_thresh)/a)
		return (max_price >= player_price, max_price)
