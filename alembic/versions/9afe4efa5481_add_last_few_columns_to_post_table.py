"""add last few columns to post table

Revision ID: 9afe4efa5481
Revises: a410bf0405bf
Create Date: 2022-06-03 00:41:50.289054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9afe4efa5481'
down_revision = 'a410bf0405bf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='True'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
