"""empty message

Revision ID: bf870ebf646f
Revises: 054888bdd2a9
Create Date: 2022-12-10 20:55:13.398777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf870ebf646f'
down_revision = '054888bdd2a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('competition_information', sa.Column('item_registration_free', sa.String(length=4), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('competition_information', 'item_registration_free')
    # ### end Alembic commands ###