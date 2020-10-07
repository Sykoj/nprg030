
# For a while

V Pythonu máme více možností, jak procházet nějakou kolekci (třeba `list` nebo `set`) a postupně zpracovávat její prvky.

Krátce, `for` dělá pohodlně to, co popisuje poslední věta. `while` dokáže to samé, ale vyžaduje mnohem víc režie kolem, protože závisí v základu jenom na podmínce. Výběr `for` nebo `while` by neměl být o preferenci, projdeme případy, kde je lepší používat `for` a kdy `while`.

Uvažme tenhle (odstrašující) příklad:

```python
numbers = [1, 2, 3, 4, 5, 6]

i = 0
length = len(numbers)

while (i < length):
    print(numbers[i] ** 2) # or whatever we need to do with numbers[i]
    i += 1
```

který jde zapsat taky takhle:

```python
numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    print(number ** 2)
```

Vidíme, že tohle je kratší (a přehlednější) zápis. Kde jinde je problém s `while` cyklem? Používání proměnných `i` a `length` může vést k chybám. Použitím `for` za mě tohle implementuje někdo jiný.


## Kdy používat for cyklus

V Python `for` ulehčuje práci s kolekcemi (vysvětlení implementace uvnitř zatím pro nás na vysvětlení moc složité :) ), už již z výše zmíněných důvodů. Pokud zpracovávám všechny prvky z nějaké kolekce `list`, `set`, `dictionary`, určitě je dobrý nápad použít `for`.

## Kdy používat while cyklus

Pokud nevím, kolik iterací ještě proběhne. Mám například algoritmus, který zpracovává nějaké prvky (můžu si představit, že jsou ve frontě, do fronty se občas vrátí), výpočet závisí na mnoha faktorech:

```python
set = { 10, 20, 30, 40 }

while (set): # if empty, this evaluates as False
    item = set.pop() # remove random element from set
    # do some computation, possibly adding other item to set
```

Nebo prostě čekáme třeba na vstup od uživatele :)

```python
while userIsSleeping():
     wait()
```

## Co když potřebuju indexy při procházení kolekce ve for cyklu

Je možné použít `enumerate()`:

```python
for index, number in enumerate([8, 4, 2, 1]):
    print(str(number) + " from index " + str(index))
```

`enumerate()` vrátí `tuples`, které zpracuje `for` a dosadí je (první člen - index a druhý člen - prvek) do proměnných:

```python
>>> print(list(enumerate(['a', 'b', 'c', 'd'])))
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
```

Pozor, kdybych zpracoval ve `for` tímto způsobem (za použití jedné proměnné), `for` do `number` nyní dosazuje `tuple`:
```python
>>> for number in enumerate(['a', 'b', 'c', 'd']):
...    print(number)
...
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
```


## Range

`range()` má víc parametrů, z přednášky víme:

```python
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
>>> list(range(5,10))
[5, 6, 7, 8, 9]
```

Existuje ještě možnost, jak zadat průchod po krocích:

```python
>>> list(range(0,10,2)) # from 0 to 10 after 2
[0, 2, 4, 6, 8]
```

## Comprehensions

V pythonu jde ještě použít koncept [comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions), který úvodní příklad umožní zapsat pěkně (zápis, který vytvoří `list` v `[]`):

```python
for number in [ x ** 2 for x in range(1,7)]:
    print(number)
```

Nebo [program]() z algoritmizace by šel zapsat i takto, za použití comprehensions:

```python
number = int(input())

powersOfTwo = [ 2 ** x
                for x in range(number)
                if 2 ** x < number ]

powersSums = [ sum(range(x+1)) # x+1: include the power of two
              for x in powersOfTwo ]

print(sum(powersSums))
```