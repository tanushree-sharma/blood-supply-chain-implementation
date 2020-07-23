import gurobipy as gp
from gurobipy import GRB

## set definitions
K = []
J = []
T = []
I = []
S = []
P = []


## parameter definitions

Aik = {}
Bjt = {}
Cikj = {}
Di = {}
Ek = {}

F, G, H, = 0,0,0
L,Q,V,W,Z = 0,0,0,0,0

alpha_jm = {}
Mj ={}
Ot ={}
Rt = {}
Xps = {}


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

