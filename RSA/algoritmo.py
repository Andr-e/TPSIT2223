def mcd_esteso(a,b):
    if a < b:
        d,x,y = mcd_esteso(b,a)
        return d,y,x
    d = b
    dp = a
    x = 0
    y = 1
    xp = 1
    yp = 0
    while d > 0 :
        print(dp,xp,yp)
        dpp,xpp,ypp = dp,xp,yp
        dp,xp,yp = d,x,y
        d = dpp%dp
        di = dpp // dp
        x,y = xpp - di * xp, ypp -di *yp
    return dp,xp,yp


if __name__ =="__main__":
    print(mcd_esteso(70,60))
    p = 11
    q = 5

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3

    gcd,d,k = mcd_esteso(e,phi)
    print(gcd, d,k)
    if d<0:
        d = d + phi
        k = k - e
    m = 2
    c = (m ** e) % n
    m = (c ** d) % n
    print( m)
   