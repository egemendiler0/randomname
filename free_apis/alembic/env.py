from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import os
from dotenv import load_dotenv
import sys

# Load environment variables
load_dotenv()

# Get absolute path to alembic directory
alembic_dir = os.path.dirname(os.path.abspath(__file__))
# Get absolute path to project root (free_apis)
project_root = os.path.dirname(alembic_dir)

# Add project root to Python path
sys.path.insert(0, project_root)

# Debugging - print paths
print(f"Project root: {project_root}")
print(f"Python path: {sys.path}")

# Alembic config
config = context.config
fileConfig(config.config_file_name)

# Import models
try:
    from alembic_versions.v001_initial_models import get_metadata
    target_metadata = get_metadata()
    print("Successfully imported models")
except ImportError as e:
    print(f"Import error: {e}")
    raise

# Migration functions
def run_migrations_offline():
    url = os.getenv("DB_URL")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = os.getenv("DB_URL")
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()