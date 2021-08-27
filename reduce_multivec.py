import numpy
import copy


"""
A container that describes a multiplet 

For example, in a 3-d space possible multuplets include x0, x5, x3 x4^2, x2^6, ...

Each multuplet is described by the set of dimension-index and power.

For example, x0 -> {0: 1}, x5-{5:1} , x3 x4 -> {3:1, 4:2} , x2^6 -> {2: 6}

Natively one multiplet is stored in a dictionary.

The container knows how to multiply multiply multiplets
"""

class Multiplet():

    """
    powers - dictionary of format {index : power}
    """
    def __init__(self, powers):
        self.powers = powers

    def multiply(self, toadd):
        ans = copy.copy(dict(self.powers))
        for key in toadd.powers.keys():
            if key in ans.keys():
                ans[key] = ans[key]+toadd.powers[key]
            else:
                ans[key] = toadd.powers[key]
        return Multiplet(ans)

    @staticmethod

    def test():
        m1 = Multiplet({0:2, 4:2})
        m2 = Multiplet({1:3, 6:7})
        print(m1)
        print(m2)
        print(m1.multiply(m2))

    def __str__(self):
        first=True
        for key in sorted(self.powers.keys()):
            if first:
                ans = "{{{}: {}".format(key,self.powers[key])
                first=False
            else:
                ans=ans+", {}: {}".format(key,self.powers[key])
        ans=ans+"}"
        return ans

"""
A container that describes an equation

An equation is described by a set of {cofficient,multiplet} pairs

Here they are saved as two ordered lists of the coffeicients and multuplets

For our work we want to create a new equation from 

(equation + y) multiplet

note positive sign of y.

the product of an equation and a multiplt
"""

class Equation():

    def __init__(self, coeffs, multiplets):
        self.coeffs = coeffs
        self.multiplets = multiplets

    def multiply(self, y, power):
        newcoeffs = self.coeffs.copy()
        newcoeffs.append(y)
        newpowers = self.multiplets.copy()
        for i in range(len(newpowers)):
            newpowers[i]=newpowers[i].multiply(power)
        newpowers.append(power)
        return Equation(newcoeffs, newpowers)

    @staticmethod

    def test():
        eq1 = Equation([1, 1, 1, 1, 1],
                       [Multiplet({0: 2, 3: 1}), Multiplet({1: 2}), Multiplet({2: 2}), Multiplet({3: 2}),
                        Multiplet({4: 2})])

        eq2 = eq1.multiply(-1, Multiplet({0: 1, 4: 1}))
        print(eq1)
        print(eq2)

    def __str__(self):
        out=""
        for a, b in zip(self.coeffs, self.multiplets):
            out=out+"{}    {}\n".format(a, b)
        return out

"""
How to proceed:

Make a list of the 12 quadratic Equations

Construct a list of qartic Equations by multiplying the 12 with all possible quartics

Count the number and index unique quardarics and quartics to get the dimensionality of the problem.

Construct an mxm matrix picking out appropriate coefficient for each index and solve the linear equations.
Note that the first elements of y will be (1,1,y,y,y,y, 0,0,0,0)

Solve the linear algebra!

"""



# if __name__ == "__main__":
#     y=numpy.uniform(-1,1,10)
#     reduce2(y,5)
