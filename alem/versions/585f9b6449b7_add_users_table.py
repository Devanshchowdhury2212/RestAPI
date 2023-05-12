"""Add Users table

Revision ID: 585f9b6449b7
Revises: ccf12a8bc917
Create Date: 2023-05-11 05:43:25.266245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '585f9b6449b7'
down_revision = 'ccf12a8bc917'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True,nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('pasword', sa.String(), nullable=False),
        sa.Column('created', sa.TIMESTAMP(timezone=True),server_default = sa.text('now()'), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
