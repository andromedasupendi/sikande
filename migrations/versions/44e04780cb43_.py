"""empty message

Revision ID: 44e04780cb43
Revises: 
Create Date: 2022-08-03 04:58:49.191176

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '44e04780cb43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_item_item', table_name='item')
    op.drop_index('ix_item_timestamp', table_name='item')
    op.drop_table('item')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('item', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('timestamp', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_item_timestamp', 'item', ['timestamp'], unique=False)
    op.create_index('ix_item_item', 'item', ['item'], unique=True)
    # ### end Alembic commands ###