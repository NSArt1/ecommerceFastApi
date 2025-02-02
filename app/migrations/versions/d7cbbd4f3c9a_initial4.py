"""initial4

Revision ID: d7cbbd4f3c9a
Revises: 64e615179892
Create Date: 2025-02-02 18:20:45.818373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7cbbd4f3c9a'
down_revision: Union[str, None] = '64e615179892'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
