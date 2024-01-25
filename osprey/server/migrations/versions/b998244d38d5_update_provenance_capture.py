"""update provenance capture

Revision ID: b998244d38d5
Revises: c4fcf7da01fe
Create Date: 2023-11-27 23:50:55.154782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b998244d38d5'
down_revision = 'c4fcf7da01fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('output',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('provenance_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['provenance_id'], ['provenance.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('provenance', schema=None) as batch_op:
        batch_op.drop_constraint('provenance_source_version_id_fkey', type_='foreignkey')
        batch_op.drop_column('source_version_id')

    with op.batch_alter_table('provenance_derivation', schema=None) as batch_op:
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('provenance_derivation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))

    with op.batch_alter_table('provenance', schema=None) as batch_op:
        batch_op.add_column(sa.Column('source_version_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('provenance_source_version_id_fkey', 'source_version', ['source_version_id'], ['id'])

    op.drop_table('output')
    # ### end Alembic commands ###