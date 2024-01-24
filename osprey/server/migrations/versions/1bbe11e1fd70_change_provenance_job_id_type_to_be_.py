"""Change Provenance job_id type to be String

Revision ID: 1bbe11e1fd70
Revises: 1d0d14a01872
Create Date: 2023-12-14 16:40:54.343641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1bbe11e1fd70"
down_revision = "1d0d14a01872"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("provenance", schema=None) as batch_op:
        batch_op.alter_column(
            "timer_job_id",
            existing_type=sa.INTEGER(),
            type_=sa.String(),
            existing_nullable=True,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("provenance", schema=None) as batch_op:
        batch_op.alter_column(
            "timer_job_id",
            existing_type=sa.String(),
            type_=sa.INTEGER(),
            existing_nullable=True,
        )

    # ### end Alembic commands ###
