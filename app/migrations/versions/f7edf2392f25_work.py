"""work

Revision ID: f7edf2392f25
Revises: 8f115cef568b
Create Date: 2025-02-02 18:24:28.481940

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f7edf2392f25'
down_revision: Union[str, None] = '8f115cef568b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
