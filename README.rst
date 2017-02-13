What is this
=============================
This is a demonstrator how Luigi could be used to build ingestion workflow for Local EGA service. 

There is two workflows in this repository: one for starting starting the ingestion process after transmission is completed (ProcessTransfer) and the other one for submission quality control (ProcessWorkspaces). Workflows can be ran periodically (cron) or triggered for example from HTTP request. 

How to use this
======================
Test this out yourself::

        $ git clone https://github.com/CSC-IT-Center-for-Science/lega-ingest-workflow.git # Clone the repository
        $ cd ega-ingest-workflow # Change directory
        $ sudo pip install -r requirements_dev.txt # Install depencides
        $ touch tests/home/dataset-xyz # Create example dataset 

        $ luigid # Start luigid central planner 
        $ python -m luigi --module lega.scripts.process_transfers ProcessTransfer --workspace-root tests/workspace/ --home-path tests/home/ # Run the first workflow
        $ python -m luigi --module lega.scripts.process_workspaces ProcessWorkspaces --workspace-root tests/workspace/ # Run the second workflow 

What else 
======================
- Check the Web UI: http://localhost:8082
- Workflow can be ran without central planner with --local-scheduler option  
- Read the docs: https://luigi.readthedocs.io/en/stable/index.html  

