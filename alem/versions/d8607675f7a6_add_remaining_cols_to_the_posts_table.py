"""add remaining cols to the posts table

Revision ID: d8607675f7a6
Revises: 29ef4e63fb9e
Create Date: 2023-05-11 08:32:48.142223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8607675f7a6'
down_revision = '29ef4e63fb9e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.BOOLEAN(),nullable=False,server_default = 'True'))
    op.add_column('posts',sa.Column('created',sa.TIMESTAMP(timezone=True),nullable=False,server_default = sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created')
    pass
