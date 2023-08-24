"""Source - Add user endpoint uuid

Revision ID: efd5d46f7a15
Revises: 2cf5303eb175
Create Date: 2023-08-08 18:03:56.148870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efd5d46f7a15'
down_revision = '2cf5303eb175'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_endpoint', sa.String(), nullable=True))
        batch_op.drop_column('last_refreshed')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_refreshed', sa.DATE(), autoincrement=False, nullable=True))
        batch_op.drop_column('user_endpoint')

    # ### end Alembic commands ###