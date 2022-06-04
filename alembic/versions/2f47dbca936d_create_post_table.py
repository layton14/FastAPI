"""create post table

Revision ID: 2f47dbca936d
Revises: 
Create Date: 2022-05-30 16:43:00.490390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f47dbca936d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False)
    )
    pass

def downgrade():
    op.drop_table('posts')
    pass
