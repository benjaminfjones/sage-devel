from sage.rings.all import CIF

def _is_numerically_zero_ginac(x):
    if not is_a_numeric(x._gobj):
        return False
    return x._gobj.is_zero()

def _is_numerically_zero_CIF(x):
    from sage.rings.all import ComplexIntervalField
    try:
        approx_x = ComplexIntervalField()(x)
        if bool(approx_x.imag() == 0) and bool(approx_x.real() == 0):
            return True
    except:
        return False
