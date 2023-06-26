"""Adding Proxies & Tags

Revision ID: 37d2bc3fa266
Revises: 3e982908aedf
Create Date: 2023-06-26 16:42:02.505661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37d2bc3fa266'
down_revision = '3e982908aedf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('source_tag',
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['source_id'], ['source.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    with op.batch_alter_table('source_version', schema=None) as batch_op:
        batch_op.drop_column('proxy_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source_version', schema=None) as batch_op:
        batch_op.add_column(sa.Column('proxy_id', sa.INTEGER(), autoincrement=False, nullable=True))

    op.drop_table('source_tag')
    op.drop_table('tag')
    # ### end Alembic commands ###
