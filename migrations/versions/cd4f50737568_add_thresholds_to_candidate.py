"""add thresholds to candidate

Revision ID: cd4f50737568
Revises: 7b162d32f76b
Create Date: 2021-03-04 15:31:14.569815

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cd4f50737568'
down_revision = '7b162d32f76b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('candidate', sa.Column('eta_thresholds', sa.ARRAY(sa.Float), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('candidate', 'eta_thresholds')
    # ### end Alembic commands ###
