"""add comment to source

Revision ID: 8dea6dd71726
Revises: aa192fe06ac3
Create Date: 2020-11-16 16:31:05.051826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8dea6dd71726'
down_revision = 'aa192fe06ac3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('source', sa.Column('comments', sa.String(length=1024), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('source', 'comments')
    # ### end Alembic commands ###
