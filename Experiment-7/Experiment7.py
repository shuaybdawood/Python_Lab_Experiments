# Base class
class A:
    def one(self):
        a = 10
        print(a)


# single inheritance
class B(A):
    def two(self):
        b = 20
        print(b)


obj = B()
obj.one()
obj.two()


# multiple inheritance
class C:
    def three(self):
        c = 30
        print(c)


class D(C, A):
    def four(self):
        d = 40
        print(d)


obj1 = D()
obj1.one()
obj1.three()
obj1.four()


# hybrid inheritance
class E(A):
    def five(self):
        e = 50
        print(e)


class F(B, E):
    def six(self):
        f = 60
        print(f)


obj2 = F()
obj2.one()
obj2.two()
obj2.five()
obj2.six()


# multilevel inheritance
class G(A):
    def seven(self):
        g = 70
        print(g)


class H(G):
    def eight(self):
        h = 80
        print(h)


obj3 = H()
obj3.one()
obj3.seven()
obj3.eight()


# hierarchical inheritance
class I(A):
    def nine(self):
        i = 90
        print(i)


class J(A):
    def ten(self):
        j = 100
        print(j)


obj4 = I()
obj4.one()
obj4.nine()

obj5 = J()
obj5.one()
obj5.ten()


# polymorphism
class K:
    def calc(self, x):
        return x + x


class L(K):
    def calc(self, x, y):
        print("double:", super().calc(x))
        return x * y


obj6 = L()
print("result:", obj6.calc(5, 3))