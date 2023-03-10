"""empty message

Revision ID: fa1f5a1d7193
Revises: 86fa9f35ee70
Create Date: 2022-11-19 15:51:38.633542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa1f5a1d7193'
down_revision = '86fa9f35ee70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pilot_aircrafts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pilot_aircrafts',
    sa.Column('pilot_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('tail_number', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['pilot_id'], ['pilots.pilot_id'], name='fk_pilot_aircrafts_pilots'),
    sa.ForeignKeyConstraint(['tail_number'], ['aircrafts.tail_number'], name='fk_pilot_aircrafts_aircrafts'),
    sa.PrimaryKeyConstraint('pilot_id', 'tail_number', name='pilot_aircrafts_pkey')
    )
    # ### end Alembic commands ###
