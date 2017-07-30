


class Background(object):
    _fwhm2sigma = 1./2.355

    def __init__(self, continuum, lines, extra_funcs):

        self._background = continuum

        self._continuum = continuum

        self._lines = lines

        self._extra_funcs = extra_funcs

        self._setup()

    def _setup(self, **kwargs):

        pass



    @property
    def lines(self):

        return self._lines
    
    @property
    def continuum(self):

        return self._continuum
    
    @property
    def background_spectrum(self):

        return self._background
