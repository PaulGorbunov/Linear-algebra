import numpy as np

def seidel(a,b,e):
    a = np.asarray(a)
    at = a.transpose()
    mul1 = np.dot(at,a)
    mul2 = np.dot(at,np.asarray(b).transpose())
    a = np.ndarray.tolist(mul1)
    b = np.ndarray.tolist(mul2)
    n_m = [[float(-a[m][k])/a[m][m] for k in range(len(a[m])) if k != m ] for m in range(len(a))]
    (lambda:[n_m[i].append(float(b[i])/a[i][i]) for i in range(len(b))] )()
    v = [i[-1] for i in n_m]
    while True:
        old_v = [r for r in v]
        for u in range(len(n_m)):
            mod_v =v[:u]+v[u+1:]
            l = [n_m[u][i]*mod_v[i] for i in range(len(n_m[u])-1)]
            l.append(n_m[u][-1])
            v[u]=sum(l)
        f = True
        for u in range(len(v)):
            if abs(v[u] - old_v[u]) >= e:
                f = False
                break
        if f:
            return [round(a1,5) for a1 in v]
        
