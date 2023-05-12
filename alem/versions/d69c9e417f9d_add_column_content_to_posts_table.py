"""add column content to posts table

Revision ID: d69c9e417f9d
Revises: 72f381c7bc7a
Create Date: 2023-05-11 05:30:33.621123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd69c9e417f9d'
down_revision = '72f381c7bc7a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
