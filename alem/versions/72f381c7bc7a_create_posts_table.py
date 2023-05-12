"""create posts table

Revision ID: 72f381c7bc7a
Revises: 
Create Date: 2023-05-11 05:12:34.126657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72f381c7bc7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True,nullable=False),
        sa.Column('title', sa.String(), nullable=False)
    )
    


def downgrade() -> None:
    op.drop_table('posts')
