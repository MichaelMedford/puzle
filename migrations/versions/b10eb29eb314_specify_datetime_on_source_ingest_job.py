"""specify datetime on source ingest job

Revision ID: b10eb29eb314
Revises: 206f65b2b504
Create Date: 2020-12-03 20:39:50.420123

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b10eb29eb314'
down_revision = '206f65b2b504'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('source_ingest_job', sa.Column('datetime_finished', sa.DateTime(), nullable=True))
    op.add_column('source_ingest_job', sa.Column('datetime_started', sa.DateTime(), nullable=True))
    op.drop_column('source_ingest_job', 'datetime')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('source_ingest_job', sa.Column('datetime', sa.DateTime(), nullable=True))
    op.drop_column('source_ingest_job', 'datetime_started')
    op.drop_column('source_ingest_job', 'datetime_finished')
    # ### end Alembic commands ###
