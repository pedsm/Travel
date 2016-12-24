class city
    constructor:(@name,@x,@y)->

mandala = new city("Mandala city",20,30)
newCity = new city("New city",30,50)

calcDistance = (city1,city2) ->
    Math.sqrt(Math.pow(Math.abs(city1.x - city2.x),2)
            + Math.pow(Math.abs(city1.y - city2.y),2))

console.log(calcDistance(mandala,newCity))

cities = []
cityNum = 10
worldSize = 100

#generate cities
console.log "Generating 10 cities"
for i in [1..cityNum]
    x = Math.floor(Math.random() * 100)
    y = Math.floor(Math.random() * 100)
    cities.push(new city("City " + i,x,y))

#permutation for iterations
arrayExcept = (arr, idx) ->
    res = arr[0..]
    res.splice idx, 1
    res

permute = (arr) ->
    arr = Array::slice.call arr, 0
    return [[]] if arr.length == 0
    permutations = (for value,idx in arr
            [value].concat perm for perm in permute arrayExcept arr, idx)
    # Flatten the array before returning it.
    [].concat permutations...

#prepare min
min = worldSize*worldSize
#lazy optimization
lazy = false
for p in permute(cities)
    total = 0
    for i in [1..p.length-1]
        total += calcDistance(p[i-1],p[i])
        if total > min
            lazy = true
            break

    if lazy
        lazy = false
        continue

    total += calcDistance(p[0],p[p.length-1])
    if total < min or min == 0
        min = total
        console.log "New min distance: " + total
        console.log "Route:"
        for city in p
            console.log city.name

