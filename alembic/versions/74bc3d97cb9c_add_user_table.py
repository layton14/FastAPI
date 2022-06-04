"""Add user table

Revision ID: 74bc3d97cb9c
Revises: b5efc3056df2
Create Date: 2022-06-03 00:21:52.148339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74bc3d97cb9c'
down_revision = 'b5efc3056df2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
