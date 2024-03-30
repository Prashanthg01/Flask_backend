"""empty message

Revision ID: 6a4ea9a9650d
Revises: 9defdba66d55
Create Date: 2020-01-31 08:10:32.104284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a4ea9a9650d'
down_revision = '9defdba66d55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.drop_column('country')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.add_column(sa.Column('country', sa.VARCHAR(length=100), nullable=True))

    # ### end Alembic commands ###
