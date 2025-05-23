"""user source association table

Revision ID: 8c67f94b52b0
Revises: f2fdfe3eaae0
Create Date: 2020-11-20 15:58:09.992203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c67f94b52b0'
down_revision = 'f2fdfe3eaae0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_source_association',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('source_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['source_id'], ['puzle.source.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['puzle.user.id'], ),
    schema='puzle'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_source_association', schema='puzle')
    # ### end Alembic commands ###
