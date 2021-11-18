class Calculator:
    def multiply(self,x,y):
        return x * y
    def add(self,x,y):
        return x + y
    def divide(self, x,y):
        if y == 0:
            return f'Ошибка!'
        else:
            return x /y
    def subtract(self, x,y):
        return x - y 

