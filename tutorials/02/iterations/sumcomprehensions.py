number = int(input())

powersOfTwo = [ 2 ** x
                for x in range(number)
                if 2 ** x < number ]

powersSums = [ sum(range(x+1)) # from 0 to include the power of two
              for x in powersOfTwo ]

print(sum(powersSums))