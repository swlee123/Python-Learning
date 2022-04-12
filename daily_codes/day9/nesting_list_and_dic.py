capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

#nesting a list in a dictionary
travel_log1 = {
    "France": ["Paris","Lille","Dijon"]
    "Germany": ["Berlin","Hamburg","Stuggart"],
}
#nest list in a list also can but not so useful

#nest a dictionary in dictionary

travel_log2 = {
    
    "France": {
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits":12},
    
    "Germany": {
        "cities_visited":["Berlin","Hamburg","Stuggart"],
        "total_visits":15},
    
}

#nesting a dictionary in a list

travel_log2 = [
    
    {
        "country":"France",
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits":12
        },
    
    {
        "country":"Germany",
        "cities_visited":["Berlin","Hamburg","Stuggart"],
        "total_visits":15
        },
    
]


