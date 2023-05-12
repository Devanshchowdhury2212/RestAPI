"""add foreign key to posts table

Revision ID: 29ef4e63fb9e
Revises: 585f9b6449b7
Create Date: 2023-05-11 08:11:34.701807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29ef4e63fb9e'
down_revision = '585f9b6449b7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('user_id',sa.Integer(),nullable = False))
    op.create_foreign_key('posts_user_fk',source_table='posts',referent_table='users',local_cols=['user_id']
                          ,remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade() -> None:    
    op.drop_constraint('posts_user_fk',table_name='posts')
    op.drop_column('posts','user_id')
    pass
