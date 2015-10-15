

from .interface import ActionInterface


class Devel(ActionInterface):
    """For development purpose only."""

    def __init__(self):
        self._exitCode = 0

        self._ui = None
        self._concurrency = None
        self._rascal = None
        self._options = {}


    def exception(self, e):
        self._exitCode = 7

    def getExitCode(self):
        return self._exitCode

    def initialize(self, ui, concurrency, rascal, options):
        self._ui = ui
        self._concurrency = concurrency
        self._rascal = rascal
        self._options = options

    def run(self):
        self._ui.infoL(1, 'running devel action')

        from ..imap.imap import Imap

        imap = Imap('imaplib2-2.50')
        imap.configure(self._ui)
        imap.connect('127.0.0.1', 10143)
        imap.logout()
