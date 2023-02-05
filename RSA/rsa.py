class RSAPublicKey:
    n: int
    e: int
    def __init__(self, n, e):
        self.n = n
        self.e = e

    def encrypt(self, m: int):
        return modexp(m, self.e, self.n)


class RSAPrivateKey:
    p: int
    q: int
    e: int
    def __init__(self, p, q, d):
        self.p = p
        self.q = q
        self.d = d

    def decrypt(self, c: int):
        return modexp(c, self.d, self.p * self.q)

# (a ** b) % n
def modexp(a, b, n):
    acc = 1
    while b > 0:
        if b % 2 == 1:
            acc = (acc * a) % n
        a = (a * a) % n
        b = b // 2
    return acc

def extended_gcd(a, b):
    if a <= 0 or b <= 0:
        raise Exception("Arguments must be positive")

    # In the algorithm a > b, otherwise just swap the coefficients
    if a < b:
        d, alpha, beta = extended_gcd(b, a)
        return d, beta, alpha

    prec = (a, 1, 0)
    curr = (b, 0, 1)

    while curr[0] > 0:
        pprec = prec
        prec = curr
        div = pprec[0] // prec[0]
        # https://ilprofalberto.github.io/sistemicrypto/#/8
        curr = (pprec[0] % prec[0], pprec[1] - div * prec[1], pprec[2] - div * prec[2])

    return prec

def generate_keypair(p, q):
    n = p * q
    phi = (p-1) * (q-1)
    e = 3

    # solve ed+k*phi(n)=1
    gcd, alpha, beta = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception("Wrong parameters")

    # alpha > 0
    # TODO: remove while
    while alpha < 0:
        alpha = alpha + phi

    d = alpha

    return RSAPrivateKey(p, q, d), RSAPublicKey(n, e)

if __name__ == "__main__":
    p = 89
    q = 41
    sk, pk = generate_keypair(p, q)

    m = 100
    c = pk.encrypt(m)
    print(c)
    assert(m == sk.decrypt(c))
