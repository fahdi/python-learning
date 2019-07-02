
## Find The Max Value In A Dictionary


Create A Dictionary

```
ages = {'John': 21,
        'Mike': 52,
        'Sarah': 12,
        'Bob': 43
       }
```
       
**Find The Maximum Value Of The Values**

```
max(zip(ages.values(), ages.keys()))
```


> (52, 'Mike')
