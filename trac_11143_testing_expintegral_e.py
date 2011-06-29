import sys
from sage.libs.mpmath import utils as mpmath_utils
import  sage.libs.pari.all
from sage.libs.pari.all import pari, PariError
import sage.rings.complex_field as complex_field
import sage.rings.real_double as real_double
import sage.rings.complex_number
from sage.gsl.integration import numerical_integral
from sage.structure.parent import Parent
from sage.structure.coerce import parent
from sage.symbolic.expression import Expression
from sage.functions.log import exp

from sage.rings.all import (is_RealNumber, RealField,
                            is_ComplexNumber, ComplexField,
                            ZZ, RR, RDF, CDF, prime_range)
                            
from sage.symbolic.function import GinacFunction, BuiltinFunction, is_inexact
from sage.symbolic.ring import SR

import sage.plot.all

CC = complex_field.ComplexField()
I = CC.gen(0)


class Function_exp_integral_En(BuiltinFunction):
    r"""
    The generalized complex exponential integral `E_n(z)` defined by
    
    .. math:
    
        \operatorname{E_n}(z) = \int_1^{\infty} \frac{e^{-z t}}{t^n} \; dt
    
    for complex numbers `n` and `z`, see [1]. The special case where `n = 1` 
    is denoted in Sage by `exponential_integral_1`. The name `En` is also used for this 
    function.
    
    EXAMPLES::
    
        sage: N(En(1,1)) # computed using mpmath
        0.219383934395520
        sage: N(exponential_integral_1(1)) # computed using PARI
        0.219383934395520
        # verify [A & S, 5.1.45]
        sage: 
    
    Maxima returns the following improper integral as a multiple of En(1,1)::
        
        sage: uu = integral(e^(-x)*log(x+1),x,0,oo)
        sage: uu
        e*En(1, 1)
        sage: uu.n(digits=30)
        0.596347362323194074341078499369
        
    ALGORITHM: 
    
    Numerical evaluation is done using mpmath, but symbolics are handled 
    by maxima.
    
    """
    def __init__(self):
        """
        EXAMPLES::
        """
        BuiltinFunction.__init__(self, "En", nargs=2, latex_name=r'En',
                                 conversions=dict(maxima='expintegral_e'))

    def _eval_(self, n, z ):
        """
        EXAMPLES::
        """
        # howto find a common parent for n and z here? 
        if not isinstance(z, Expression) and is_inexact(z):
            return self._evalf_(n, z, parent(z))
        return None
            
    def _evalf_(self, n, z, parent=None):
        """
        EXAMPLES::
        """
        import mpmath
        if isinstance(parent, Parent) and hasattr(parent, 'prec'):
            prec = parent.prec()
        else:
            prec = 53
        return mpmath_utils.call(mpmath.expint, n, z, prec=prec)

    def __call__(self, n, z, prec=None, coerce=True, hold=False ):
        """
        Note that the ``prec`` argument is deprecated. The precision for
        the result is deduced from the precision of the input. Convert
        the input to a higher precision explicitly if a result with higher
        precision is desired.

        EXAMPLES::

        """
        if prec is not None:
            from sage.misc.misc import deprecation
            deprecation("The prec keyword argument is deprecated. Explicitly set the precision of the input, for example En(RealField(300)(1), RealField(300)(1)), or use the prec argument to .n() for exact inputs, e.g., En(1,1).n(300), instead.")
            
            import mpmath
            return mpmath_utils.call(mpmath.expint, n, z, prec=prec)

        return BuiltinFunction.__call__(self, n, z, coerce=coerce, hold=hold)

    def _derivative_(self, n, z, diff_param=None):
        """
        If `n` is an integer strictly larger than 0, then the derivative of
        `E_n(z)` with respect to `z` is `-E_{n-1}(z)`. See [A & S, 5.1.26].
        
        EXAMPLES::
        """
        if n in ZZ and n > 0:
            return -1*BuiltinFunction.__call__(self, n-1, z)
        else:
            raise NotImplementedError("The derivative d/dz En(z) is only implemented for n = 1, 2, 3, ...")

En = Function_exp_integral_En()
