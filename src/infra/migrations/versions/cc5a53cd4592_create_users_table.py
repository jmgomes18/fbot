"""create users table

Revision ID: cc5a53cd4592
Revises: 
Create Date: 2022-04-26 00:39:20.850068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc5a53cd4592'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('password', sa.String(100), nullable=False),
    )

def downgrade():
    op.drop_table('users')
