
import time
import os

from .driver import DriverBase

from ..constants import DRV
from ..toolkit import expandPath
from ..error import DriverFatalError


class Maildir(DriverBase):
    """Maildir driver possibly redefined by the rascal."""

    def connect(self):
        path = expandPath(self.conf.get('path'))
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
        except FileNotFoundError:
            raise DriverFatalError(
                "parent directory of '%s' does not exists"% path)
        return True

    def logout(self):
        self.ui.debugC(DRV, 'logged out')

    def getFolders(self):
        time.sleep(1) # simulate long time
        return ['a', 'b', 'x']
