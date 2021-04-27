"""merge heads

Revision ID: 6f3bc0b966cb
Revises: e683f5d61ac1, aea14a70cf4b
Create Date: 2021-04-27 19:44:11.627346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f3bc0b966cb'
down_revision = ('e683f5d61ac1', 'aea14a70cf4b')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
