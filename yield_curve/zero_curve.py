# create a Class called ZeroCurve that will be used to store the zero rates and the discount factors
# for a given set of maturities and zero rates
# the class will have the following methods:
# - add_zero_rate(maturity, zero_rate): add a zero rate to the curve
# - get_zero_rate(maturity): get the zero rate for a given maturity

class ZeroCurve:
    def __init__(self):
        self.maturities = []
        self.zero_rates = []
        self.discount_factors = []
    
    def add_zero_rate(self, maturity, zero_rate):
        self.maturities.append(maturity)
        self.zero_rates.append(zero_rate)
        self.discount_factors.append(1/(1+zero_rate)**maturity)
    
    def get_zero_rate(self, maturity):
        if maturity in self.maturities:
            return self.zero_rates[self.maturities.index(maturity)]
        else:
            return None

    def get_discount_factor(self, maturity):
        if maturity in self.maturities:
            return self.discount_factors[self.maturities.index(maturity)]
        else:
            return None