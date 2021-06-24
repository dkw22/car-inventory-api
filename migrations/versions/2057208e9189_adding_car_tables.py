"""adding car tables

Revision ID: 2057208e9189
Revises: 5a4b75985f0d
Create Date: 2021-06-24 02:42:31.046650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2057208e9189'
down_revision = '5a4b75985f0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('make', sa.String(length=150), nullable=True),
    sa.Column('model', sa.String(length=200), nullable=True),
    sa.Column('year', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('color', sa.String(length=150), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('doors', sa.String(length=100), nullable=True),
    sa.Column('seats', sa.String(length=100), nullable=True),
    sa.Column('condition', sa.String(length=50), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car')
    # ### end Alembic commands ###
