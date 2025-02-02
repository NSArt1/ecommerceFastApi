"""Initial migration

Revision ID: 43c456a9c473
Revises: 048cf523b0b7
Create Date: 2025-02-02 18:59:32.704991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43c456a9c473'
down_revision: Union[str, None] = '048cf523b0b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
