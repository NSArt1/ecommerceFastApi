"""Initial migration3

Revision ID: 64e615179892
Revises: d6edc0921212
Create Date: 2025-02-02 00:01:30.651443

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '64e615179892'
down_revision: Union[str, None] = 'd6edc0921212'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
