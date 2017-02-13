import os
import luigi
from time import sleep
from uuid import uuid4

class MoveTransferToWorkspace(luigi.Task):

    transfer_path = luigi.Parameter()
    workspace_path = luigi.Parameter()

    def requires(self):
        return ReadyForTransfer(filename=self.transfer_path)

    def complete(self):
        return not os.path.exists(self.transfer_path)

    def run(self):
        # Create workspace directory
        if not os.path.exists(self.workspace_path):
            os.mkdir(self.workspace_path)

        # Create workspace/transfer directory for
        # storing original copy of transfer
        transfer_path = os.path.join(self.workspace_path, 'transfer')
        if not os.path.exists(transfer_path):
            os.mkdir(transfer_path)

        transfer_path = os.path.join(transfer_path, 'original-transfer.zip')
        os.rename(self.transfer_path, transfer_path)


class ReadyForTransfer(luigi.ExternalTask):

    filename = luigi.Parameter()
    is_ready = False

    def run(self):
        sleep(1)

    def output(self):
        return luigi.LocalTarget(self.filename)

    def complete(self):
        # Implement logic for determing if transfer is complete and
        # processing can begin.
        if not self.is_ready:
            self.is_ready = True
            return False

        return True
