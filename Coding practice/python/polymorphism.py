import multipledispatch
class A:
    @multipledispatch.dispatch(int,int)
    def multiply(self,a,b):
        return a*b
    @multipledispatch.dispatch(int,int,int)
    def multiply(self,a,b,c):
        return a*b*c
    @multipledispatch.dispatch(float,float)
    def multiply(self,a,b):
        return a*b
    @multipledispatch.dispatch(int,str)
    def multiply(self,a,b):
        return a*b
obj = A()
print (obj.multiply(2,"yash"))