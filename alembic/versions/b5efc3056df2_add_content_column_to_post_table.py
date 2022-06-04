"""add content column to post table

Revision ID: b5efc3056df2
Revises: 2f47dbca936d
Create Date: 2022-05-30 17:01:09.992642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5efc3056df2'
down_revision = '2f47dbca936d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', 
    sa.Column('content', sa.String(), nullable=False)
    )
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
