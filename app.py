from pathlib import Path

from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project


project_path = Path(".").resolve()
metadata = bootstrap_project(project_path)
with KedroSession.create(metadata.package_name, project_path) as session:
    context = session.load_context()
    catalog = context.catalog

random_number = catalog.load("random_number")
