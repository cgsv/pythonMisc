#converting floating to bits that represent them in computer
def bits2float(bits):
    if len(bits) != 32:
        return
    if not set(bits).issubset({'0','1'}):
        return
    sign =1 - 2 * int(bits[0])
    return sign*(1.0+float(int(bits[9:],2))/2**23)*2**(int(bits[1:9],2)-127)

def float2bits(fnum):
    sign = 0 if fnum > 0 else 1
    fnum = abs(fnum)
    exponent = 0
    step = 1 if fnum > 1.0 else -1
    while True:
        if 1.0 <= fnum < 2.0:
            break
        fnum = fnum / 2**step
        exponent += step
    return str(sign) +  bin(exponent + 127)[2:].rjust(8,'0') \
           + bin(int((fnum - 1)*2**23))[2:].rjust(23,'0')

if __name__ == '__main__':
    print float2bits(-5.5)
    print float2bits(0.75)
    print bits2float(float2bits(-5.5))
    print bits2float(float2bits(0.75))
