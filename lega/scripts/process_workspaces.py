import os
import luigi
from scandir import scandir

from lega.workflow.validate import ValidateWorkspace

import logging
LOGGER = logging.getLogger(__name__)


class ProcessWorkspaces(luigi.WrapperTask):

    workspace_root = luigi.Parameter()

    def requires(self):
        LOGGER.info('Process from %s' % self.workspace_root)

        for workspace in scandir(self.workspace_root):
            workspace = os.path.join(self.workspace_root, workspace.name)
            yield ValidateWorkspace(workspace=workspace)
