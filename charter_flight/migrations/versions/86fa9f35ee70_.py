"""empty message

Revision ID: 86fa9f35ee70
Revises: a5e7b388041b
Create Date: 2022-11-18 17:52:38.545730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86fa9f35ee70'
down_revision = 'a5e7b388041b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pilot_aircrafts')
    op.create_unique_constraint(None, 'aircrafts', ['aircraft_name'])
    op.drop_constraint('customers_email_key', 'customers', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('customers_email_key', 'customers', ['email'])
    op.drop_constraint(None, 'aircrafts', type_='unique')
    op.create_table('pilot_aircrafts',
    sa.Column('pilot_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('tail_number', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['pilot_id'], ['pilots.pilot_id'], name='fk_pilot_aircrafts_pilots'),
    sa.ForeignKeyConstraint(['tail_number'], ['aircrafts.tail_number'], name='fk_pilot_aircrafts_aircrafts'),
    sa.PrimaryKeyConstraint('pilot_id', 'tail_number', name='pilot_aircrafts_pkey')
    )
    # ### end Alembic commands ###