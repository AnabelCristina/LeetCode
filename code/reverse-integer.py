class Solution:
    def reverse(self, x: int) -> int:
        numbers = []
        signal = False

        if x < 0:
            signal = True
            x = -x

        [numbers.append(d) for d in str(x)]

        for i in range(math.floor(len(numbers)/2)):
            last = len(numbers) -1 -i

            temp = numbers[i]
            numbers[i] = numbers[last]
            numbers[last] = temp
        
        result = int("".join([str(i) for i in numbers]))

        result = result if result >= -2**31 and result <= (2**31) -1 else 0 

        return int(result)*-1 if (signal == True) else int(result);