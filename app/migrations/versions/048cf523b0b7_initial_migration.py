"""Initial migration

Revision ID: 048cf523b0b7
Revises: f7edf2392f25
Create Date: 2025-02-02 18:57:35.754614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '048cf523b0b7'
down_revision: Union[str, None] = 'f7edf2392f25'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
