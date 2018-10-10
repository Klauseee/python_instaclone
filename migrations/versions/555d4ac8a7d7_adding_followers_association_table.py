"""adding followers association table

Revision ID: 555d4ac8a7d7
Revises: 50c59dc39e94
Create Date: 2018-10-10 14:29:14.631533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '555d4ac8a7d7'
down_revision = '50c59dc39e94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###