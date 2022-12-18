import math

class continued_fraction():
	def __init__(self, int_part=0, numerators=None, denominators=None):
		self.int_part = int_part

		# we must always have a list of numerators and denominators
		if numerators and denominators:
			self.numerators = numerators
			self.denominators = denominators

			# the lists must be the same length
			while len(self.numerators) < len(self.denominators):
				self.numerators.append(1)
			while len(self.denominators) < len(self.numerators):
				self.denominators.append(1)

		elif numerators and not denominators:
			self.numerators = numerators
			self.denominators = [1 for num in numerators]
		elif denominators and not numerators:
			self.numerators = [1 for den in denominators]
			self.denominators = denominators
		else:
			self.numerators = []
			self.denominators = []


	def to_frac(self):
		num = self.numerators[-1]
		den = self.denominators[-1]
		gcd = math.gcd(num, den)
		num = num // gcd
		den = den // gcd
		for idx in range(len(self.numerators)-2, -1, -1):
			new_num = self.numerators[idx] * den 
			new_den = self.denominators[idx] * den + num

			gcd = math.gcd(new_num, new_den)
			num = new_num // gcd
			den = new_den // gcd

		num = self.int_part * den + num 

		return num, den 

	def to_dec(self):
		num, den = self.to_frac()
		return num / den 


if __name__ == "__main__":
	phi_approx = continued_fraction(1, [1 for i in range(20)])
	# print(phi_approx.to_frac())
	print(phi_approx.to_dec())
	print((1 + math.sqrt(5))/2)

	nums = [(2*i+1)**2 for i in range(50)]
	dens = [6 for i in range(50)]
	pi_approx = continued_fraction(3, nums, dens)
	# print(pi_approx.to_frac())
	print(pi_approx.to_dec())
	print(math.pi)