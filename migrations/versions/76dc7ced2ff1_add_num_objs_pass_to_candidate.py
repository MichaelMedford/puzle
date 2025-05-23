"""add num_objs_pass to candidate

Revision ID: 76dc7ced2ff1
Revises: 6b0505db9fbe
Create Date: 2021-03-12 15:39:51.764092

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '76dc7ced2ff1'
down_revision = '6b0505db9fbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('candidate', sa.Column('num_objs_pass', sa.Integer()))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('candidate', 'num_objs_pass')
    # ### end Alembic commands ###
