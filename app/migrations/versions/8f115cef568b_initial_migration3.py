"""Initial migration3

Revision ID: 8f115cef568b
Revises: d7cbbd4f3c9a
Create Date: 2025-02-02 18:23:05.341581

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8f115cef568b'
down_revision: Union[str, None] = 'd7cbbd4f3c9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
