"""posts table

Revision ID: 50c59dc39e94
Revises: 2ca505b7dd92
Create Date: 2018-10-05 13:36:11.076224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50c59dc39e94'
down_revision = '2ca505b7dd92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('caption', sa.String(length=380), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_caption'), 'post', ['caption'], unique=False)
    op.create_index(op.f('ix_post_location'), 'post', ['location'], unique=False)
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.create_index(op.f('ix_post_url'), 'post', ['url'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_url'), table_name='post')
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_index(op.f('ix_post_location'), table_name='post')
    op.drop_index(op.f('ix_post_caption'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
