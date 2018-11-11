stations={}
stations["kone"]=set(["id","nv","ut"])
stations["ktwo"]=set(["id","wa","mt"])
stations["kthree"]=set(["or","ca","nv"])
stations["kfour"]=set(["nv","ut"])
stations["kfive"]=set(["ca","az"])
final_station=set()

state_need=set(["wa","mt","id","nv","ut","or","ca","az"])

while state_need:
    best_station=None
    state_covered=set()
    for station,state in stations.items():
        covered=state_need & state
        if len(covered) > len(state_covered):
            state_covered=covered
            best_station=station
    state_need -= state_covered
    final_station.add(best_station)
    
print final_station
