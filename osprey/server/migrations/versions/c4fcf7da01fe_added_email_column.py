"""added email column

Revision ID: c4fcf7da01fe
Revises: 3bfddefbf995
Create Date: 2023-11-03 16:50:20.004064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4fcf7da01fe'
down_revision = '3bfddefbf995'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.drop_column('email')

    # ### end Alembic commands ###