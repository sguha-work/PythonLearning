class Calculator:
    def add(self, *numbers):
        if len(numbers)!=0:
            if len(numbers)==1:
                return numbers[0]
            else:
                result = 0
                for number in numbers:
                    result += number
                return result
        else:
            return 0


calcObject = Calculator()
print(calcObject.add())
print(calcObject.add(5))
print(calcObject.add(2, 5))
print(calcObject.add(2, 5, 3))
print(calcObject.add(2, 5, 3, 6))
