import os
import luigi


class ValidateWorkspace(luigi.WrapperTask):
    """Wrapper task for validation workflow"""

    workspace = luigi.Parameter()

    def requires(self):
        return ChecksumWorkspace(workspace=self.workspace)


class DecryptWorkspace(luigi.Task):
    """Decrypt submission from workspace"""

    workspace = luigi.Parameter()

    def output(self):
        task_report_path = os.path.join(
            self.workspace, 'task-report-decrypt')
        return luigi.LocalTarget(task_report_path)

    def run(self):
        # Implement decrypting
        # ...

        # Write a task report

        with self.output().open('w') as fd:
            fd.write('success')


class ChecksumWorkspace(luigi.Task):
    """Check md5 checksums from workspace"""

    workspace = luigi.Parameter()

    def requires(self):
        return DecryptWorkspace(workspace=self.workspace)

    def output(self):
        task_report_path = os.path.join(
            self.workspace, 'task-report-checksum')
        return luigi.LocalTarget(task_report_path)

    def run(self):
        # Implement MD5 checksum checking
        # ...

       with self.output().open('w') as fd:
            fd.write('success')
