import os
import luigi
from scandir import scandir
from uuid import uuid4

from lega.workflow.transfer import MoveTransferToWorkspace

import logging
LOGGER = logging.getLogger(__name__)


class ProcessTransfer(luigi.WrapperTask):

    workspace_root = luigi.Parameter()
    home_path = luigi.Parameter()

    def requires(self):

        LOGGER.info('Process transfers from users home directory %s and move '
                    'them to %s' % (self.workspace_root, self.home_path))

        for filename in scandir(self.home_path):

            unique = str(uuid4())
            source = os.path.join(self.home_path, filename.name)
            destination = os.path.join(self.workspace_root, '%s-%s' %
                                       (filename.name, unique))

            yield MoveTransferToWorkspace(
                transfer_path=source,
                workspace_path=destination)
