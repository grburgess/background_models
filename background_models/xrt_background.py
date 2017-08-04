from generic_background_model import Background
from astromodels import Broken_powerlaw, StepFunction, Gaussian

class XRTBackground(Background):
    
    def __init__(self,level):
        
        xrt_continuum = Broken_powerlaw(xb=2)
        
        xrt_continuum.xb.min_value = 0.2
        xrt_continuum.xb.max_value= 5
        
        xrt_continuum.alpha.min_value= -4
        xrt_continuum.beta.min_value= -4
        xrt_continuum.alpha.max_value = 0.8
        xrt_continuum.beta.max_value = 0.8
        xrt_continuum.alpha.value = -2
        xrt_continuum.beta.value = -1.5

        xrt_continuum.K.min_value = 1e-10
        xrt_continuum.K.max_value= 1
        xrt_continuum.K.value = 0.004

        line_parameters = [(0.1, 0.7, 1.1), (2, 2.15, 2.5), (1, 1.2, 1.4), (0, 0.4, 0.5)]
        
        lines = []

        for (lo, mid, hi)  in line_parameters:

            gg = Gaussian(mu=mid)
            gg.mu.bounds = (lo, hi)
            gg.sigma = 0.2 * self._fwhm2sigma
            gg.F=0.01

            lines.append(gg)
            
            
        step = StepFunction()
        
        step.lower_bound.value = 2
        step.upper_bound.value = 3
        step.lower_bound.min_value = 1.75
        step.lower_bound.max_value = 2.25
        step.upper_bound.min_value = 2.75
        step.upper_bound.max_value = 3.25
        step.value.value = 0.5
        step.value.min_value = 1e-3
        step.value.max_value = 1 - 1e-3

        super(XRTBackground,self).__init__(continuum=xrt_continuum,
                                           lines=lines,
                                           extra_funcs=[step]
        )
        
        self._setup(level)
        
        
    def _setup(self,level):
        
        

        
        for i in xrange(min([level,3])):
            
            self._background += self._lines[i]
            
        if level > 4:
            
            self._background *= (1. - self._extra_funcs[0])
        
        if level > 5:
            
            self._background += self._lines[2]
