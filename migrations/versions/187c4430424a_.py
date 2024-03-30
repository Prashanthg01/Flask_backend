"""empty message

Revision ID: 187c4430424a
Revises: 437b0c969352
Create Date: 2022-02-12 11:22:39.582987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '187c4430424a'
down_revision = '437b0c969352'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customization_of_features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.Text(), nullable=True),
    sa.Column('average_rating_map', sa.Integer(), nullable=True),
    sa.Column('no_of_rating_map', sa.Integer(), nullable=True),
    sa.Column('wordcloud', sa.Integer(), nullable=True),
    sa.Column('sentiment', sa.Integer(), nullable=True),
    sa.Column('features', sa.Integer(), nullable=True),
    sa.Column('competitor', sa.Integer(), nullable=True),
    sa.Column('retailanalysis', sa.Integer(), nullable=True),
    sa.Column('retailpricing', sa.Integer(), nullable=True),
    sa.Column('pricingcomparison', sa.Integer(), nullable=True),
    sa.Column('weeklypricing', sa.Integer(), nullable=True),
    sa.Column('monthlypricing', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], name='fk', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customization_of_features')
    # ### end Alembic commands ###