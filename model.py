#import gurobipy as gp
#from gurobipy import GRB

## assume scenario 3A is selected
## set definitions
# collection alternatives
K = [0,1,2,3,4]
#products required
J = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#planning horizon
T = [0,1,2,3,4,5,6]
#blood groups
I = [0,1,2,3,4,5,6,7]
#shelf life alternatives
S = [0,1,2,3,4,5]
#set of platlets
P = [0,1]

values = [[53, 81.10923163412492, 26.388446364308283, 43.299213384643515], [128, 70.70804598078107, 3.460460027118386, 55.95425411945416], [113, 95.22121141909994, 82.86139883852162, 39.8931834395421], [188, 127.25354364734929, 89.75739981905785, 27.759519000670377], [76, 72.07005687679279, 29.779994587167778, 23.48169383860372], [108, 148.10187291811576, 64.08244288309393, 63.39531348117182], [17, 40.24949285971841, 32.0542145488337, 42.67039239220871]]

## parameter definitions
Aik = {}




Bjt = {(0, 0): '', (0, 1): '', (0, 2): '', (0, 3): '', (0, 4): '', (0, 5): '', (0, 6): '', (1, 0): '', (1, 1): '', (1, 2): '', (1, 3): '', (1, 4): '', (1, 5): '', (1, 6): '', (2, 0): '', (2, 1): '', (2, 2): '', (2, 3): '', (2, 4): '', (2, 5): '', (2, 6): '', (3, 0): '', (3, 1): '', (3, 2): '', (3, 3): '', (3, 4): '', (3, 5): '', (3, 6): '', (4, 0): '', (4, 1): '', (4, 2): '', (4, 3): '', (4, 4): '', (4, 5): '', (4, 6): '', (5, 0): '', (5, 1): '', (5, 2): '', (5, 3): '', (5, 4): '', (5, 5): '', (5, 6): '', (6, 0): '', (6, 1): '', (6, 2): '', (6, 3): '', (6, 4): '', (6, 5): '', (6, 6): '', (7, 0): '', (7, 1): '', (7, 2): '', (7, 3): '', (7, 4): '', (7, 5): '', (7, 6): '', (8, 0): '', (8, 1): '', (8, 2): '', (8, 3): '', (8, 4): '', (8, 5): '', (8, 6): '', (9, 0): '', (9, 1): '', (9, 2): '', (9, 3): '', (9, 4): '', (9, 5): '', (9, 6): '', (10, 0): '', (10, 1): '', (10, 2): '', (10, 3): '', (10, 4): '', (10, 5): '', (10, 6): '', (11, 0): '', (11, 1): '', (11, 2): '', (11, 3): '', (11, 4): '', (11, 5): '', (11, 6): '', (12, 0): '', (12, 1): '', (12, 2): '', (12, 3): '', (12, 4): '', (12, 5): '', (12, 6): '', (13, 0): '', (13, 1): '', (13, 2): '', (13, 3): '', (13, 4): '', (13, 5): '', (13, 6): '', (14, 0): '', (14, 1): '', (14, 2): '', (14, 3): '', (14, 4): '', (14, 5): '', (14, 6): '', (15, 0): '', (15, 1): '', (15, 2): '', (15, 3): '', (15, 4): '', (15, 5): '', (15, 6): '', (16, 0): '', (16, 1): '', (16, 2): '', (16, 3): '', (16, 4): '', (16, 5): '', (16, 6): '', (17, 0): '', (17, 1): '', (17, 2): '', (17, 3): '', (17, 4): '', (17, 5): '', (17, 6): '', (18, 0): '', (18, 1): '', (18, 2): '', (18, 3): '', (18, 4): '', (18, 5): '', (18, 6): '', (19, 0): '', (19, 1): '', (19, 2): '', (19, 3): '', (19, 4): '', (19, 5): '', (19, 6): ''}

for i in range Bjt:
    #first 16 products are RBC
    if i <=112:
        


Cikj = {}
Di = {
    0 : 0.609,
    1 : 0.23,
    2 : 0.0792,
    3 : 0.0422,
    4 : 0.0172,
    5 : 0.0154,
    6 : 0.0051,
    7 : 0.0011
}
Ek = {}

F, G, H, = 0,0,0
L,Q,V,W,Z = 0,0,0,0,0

#assume alpha j is equivalent to discard rate 
alpha_j = {0: 0.049725, 1: 0.049725, 2: 0.049725, 3: 0.049725, 4: 0.049725, 5: 0.049725, 
           6: 0.049725, 7: 0.049725, 8: 0.049725, 9: 0.049725, 10: 0.049725, 11: 0.049725, 
          12: 0.049725, 13: 0.049725, 14: 0.049725, 15: 0.049725, 16: 0.0434, 17: 0.0434, 18: 0, 19: 0}
Mj ={}
Ot ={
    0 : 0.07759882869692533,
    1 : 0.18740849194729137,
    2 : 0.16544655929721816,
    3 : 0.2752562225475842,
    4 : 0.11127379209370425,
    5 : 0.1581259150805271,
    6 : 0.024890190336749635,
}

Rt = {    
    0 : 1,
    1 : 1,
    2 : 1,
    3 : 1,
    4 : 1,
    5 : 1,
    6 : 1,
    }
Xps = {}

a = {(j,t): "" for j in J for t in T}

print(a)

'''
model = gp.Model('version1')

## NOTE: every variable is integer+ except for slack and surplus (default is continuous)

## decision variables
dv_x=model.addVars(I, K, T, name='x_ikt', vtype=GRB.INTEGER)

## auxiliary variables
av_q=model.addVars(J, T, name='q_jt', vtype=GRB.INTEGER)
av_i=model.addVars(J, T, name='i_jt', vtype=GRB.INTEGER)
av_y=model.addVars(J, T, name='y_jt', vtype=GRB.INTEGER)
av_sl=model.addVars(I, T, name='sl_it')
av_spl=model.addVars(I,T, name='spl_it')

av_p=model.addVars(P, T, name='p_pt', vtype=GRB.INTEGER)
av_r=model.addVars(P, S, T, name='r_pst', vtype=GRB.INTEGER)
av_u=model.addVars(P, S, T, name='u_pst', vtype=GRB.INTEGER)
av_e = model.addVars(P,T, name='e_pt', vtype=GRB.INTEGER)


## objective functionv (minimization)
obj_W = sum([
    sum([Ek[k]*dv_x.sum('*',k,'*') for k in K]),
    Q*av_e.sum('*', '*'),
    L*av_y.sum('*', '*'),
    L*av_spl.sum('*', '*'),
])

model.setObjective(obj_W, GRB.MINIMIZE)


## note constraint labelling starts from 2 (first contstraint is 2)
#model.addConstrs((), "(15)")
# constraints (2) -- b,c need to be checked
model.addConstrs( (
    sum([dv_x.sum('*', k, t) for k in {0,1,2} ]) <= F*Rt[t] 
    for t in T 
    ), "(2)a")
model.addConstrs( (
    dv_x.sum(i, K[3], t) <= G*Rt[t] 
    for i in I for t in T 
    ), "(2)b")
model.addConstrs( (
    dv_x.sum(i, K[4], t) <= H*Rt[t] 
    for i in I for t in T 
    ), "(2)c")

#constraint (3)
model.addConstrs( (
    av_q[j, 0] == sum([sum([Aik[i,k]*Cikj[i,k,j] for i in I]) for k in K]) 
    for j in J 
    ), "(3)")

# constraint (4)
model.addConstrs( (
    av_q[j, t] == sum([sum([Aik[i,k]*Cikj[i,k,j] for i in I]) for k in K]) 
    for j in J for t in T if t >=1 
    ), "(4)")

# constraint (5), (6)
model.addConstrs((
    (av_i[j,0] - av_y[j,0]) == (N[j] - B[j,0]) 
    for j in J if j not in {16,17} 
    ), "(5)")
model.addConstrs((
    av_i[j,t] == (av_i[j,t-1] + av_q[j,t-1] + av_y[j,t] - B[j,t]) 
    for t in T for j in J if (j not in {16,17} and t > 0) 
    ), "(6)")

# constraint (7)-(12)
model.addConstrs((
    av_e[p,0] == (Xps[p,0] - av_u[p,0,0]) 
    for p in P 
    ), "(7)")
model.addConstrs((
    av_r[p,s-1,0] == (X[p,s] - av_u[p,s,0]) 
    for p in P for s in S if s > 0
    ), "(8)")
model.addConstrs((
    av_e[p,t] == (av_r[p,0,t]-av_u[p,0,t]) 
    for p in P for t in T if t > 0
    ), "(9)")
model.addConstrs((
    av_r[p,s-1,t] == (av_r[p,s,t-1] - av_u[p,s,t]) 
    for p in P for s in S for t in T if (t > 0 and (s not in {0,4}))
    ), "(10)")
model.addConstrs((
    av_r[0,3,t] == (av_r[0,4,t-1] + av_q[16,t-1] - av_u[0,4,t]) 
    for t in T if t > 0 
    ), "(11)")
model.addConstrs((
    av_r[1,3,t] == (av_r[1,4,t-1] + av_q[17, t-1] - av_u[1,4,t]) 
    for t in T if t > 0
    ), "(12)")

# constraint (13), (14)
model.addConstrs((
    av_u.sum(0, '*', t) == Bjt[16, t] 
    for t in T
    ), "(13)")
model.addConstrs((
    (av_u.sum(1, '*', t) - av_p[1,t]) == Bjt[17,t] 
    for t in T 
    ), "(14)")

# constraint (15) - (18)
model.addConstrs((
    (dv_x.sum(i,'*', t) - Di[i]*dv_x.sum('*','*',t) + av_sl[i,t] - av_spl[i,t] ) == 0 
    for i in I for t in T 
    ), "(15)")
model.addConstrs((
    dv_x.sum(i, '*', t) <= Di[i]*V 
    for i in I for t in T
    ), "(16)")
model.addConstrs((
    dv_x.sum('*', '*', t) <= W*Ot[t] 
    for t in T
    ), "(17)")
model.addConstrs((
    av_i[j,t] >= Mj[j] 
    for j in J for t in T
    ), "(18)")


# model.optimize()
'''
