graph={}
graph["start"]={}
graph["start"]["a"]=6
graph["start"]["b"]=2
graph["a"]={}
graph["a"]["fin"]=1
graph["b"]={}
graph["b"]["a"]=3
graph["b"]["fin"]=5
graph["fin"]={}

costs={}
infinity=float("inf")
costs["a"]=6
costs["b"]=2
costs["fin"]=infinity

parents={}
parents["a"]="start"
parents["b"]="start"
parents["fin"]= None

processed=[]

def find_lowest_cost_node(costs):
    lowest_cost=float("inf")
    lowest_cost_node=None
    for n in costs:
        cost=costs[n]
        if cost < lowest_cost and n not in processed:
            lowest_cost=cost
            lowest_cost_node =n
    return lowest_cost_node
node=find_lowest_cost_node(costs)  
while node is not None:
    cost=costs[node]
    neighbor=graph[node]
    for n in neighbor.keys():
        new_cost=cost+neighbor[n]
        if costs[n] > new_cost:
            costs[n]=new_cost
            parents[n]=node
    processed.append(node)
 node=find_lowest_cost_node(costs)
    
print costs
print parents
