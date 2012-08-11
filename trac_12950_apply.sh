#!/bin/bash

for url in \
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/12950/trac_12950-pickle_symbolic_function-trac.patch \
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/12950/trac_11423-atan_error-trac.patch \
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/12950/trac_12950-revolution_plot3d.patch \
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/12950/trac_12950-numeric_comparison_doctest_fixes-trac.patch \
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/12950/trac_12950-further_doctests_for_numerics.patch \
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/12950/trac_12950-symbolic_beta-trac.patch \
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/12950/trac_12950-pynac_infinities-trac.patch \
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/12950/trac_12950-pynac_infinities_doctest_fixes-trac.patch \
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/12950/trac_12950-psi_evalf-trac.patch \
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/12950/trac_12950-reviewer.patch; do
    hg qimport $url && hg qpush
done
