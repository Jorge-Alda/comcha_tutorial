import alpaca
import numpy as np

def run_coeffs(fa, cqL33, cuR, cdR, clL33, ceR):
    return alpaca.ALPcouplings({'cqL': np.diag([0,0,cqL33]), 'cuR': cuR, 'cdR': cdR, 'clL': np.diag([0,0,clL33]), 'ceR': ceR}, basis='derivative_above', scale=4*np.pi*fa).match_run(2.0, 'VA_below')

def chi2(fa, cqL33, cuR, cdR, clL33, ceR):
    c = run_coeffs(fa, cqL33, cuR, cdR, clL33, ceR)
    chi2 = alpaca.statistics.get_chi2(alpaca.sectors.default_sectors['all'], 2.0, c, fa, integrator='no_rge')
    return chi2.chi2_tot()[0]