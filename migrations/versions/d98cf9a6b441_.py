"""empty message

Revision ID: d98cf9a6b441
Revises: 99d9b5b3c9f4
Create Date: 2020-01-22 20:14:20.370637

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = 'd98cf9a6b441'
down_revision = '99d9b5b3c9f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sublets', sa.Column('address', sa.String(length=100), nullable=True))
    op.add_column('sublets', sa.Column('management', sa.String(length=30), nullable=True))
    op.add_column('sublets', sa.Column('postalcode', sa.String(length=6), nullable=True))
    op.add_column('sublets', sa.Column('title', sa.String(length=100), nullable=True))
    op.alter_column('users', 'anonymous',
               existing_type=mssql.BIT(),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('users', 'verifiedstu',
               existing_type=mssql.BIT(),
               type_=sa.Boolean(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'verifiedstu',
               existing_type=sa.Boolean(),
               type_=mssql.BIT(),
               existing_nullable=True)
    op.alter_column('users', 'anonymous',
               existing_type=sa.Boolean(),
               type_=mssql.BIT(),
               existing_nullable=True)
    op.drop_column('sublets', 'title')
    op.drop_column('sublets', 'postalcode')
    op.drop_column('sublets', 'management')
    op.drop_column('sublets', 'address')
    # ### end Alembic commands ###
