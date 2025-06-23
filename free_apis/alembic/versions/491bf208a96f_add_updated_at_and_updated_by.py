"""add updated_at and updated_by

Revision ID: 491bf208a96f
Revises: c000992c38c5
Create Date: 2025-03-30 11:56:41.553765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '491bf208a96f'
down_revision: Union[str, None] = 'c000992c38c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('example_table',
                  sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True))
    op.add_column('example_table',
                  sa.Column('updated_by', sa.String(255), nullable=True))


def downgrade() -> None:
    op.drop_column('example_table', 'updated_at')
    op.drop_column('example_table', 'updated_by')
