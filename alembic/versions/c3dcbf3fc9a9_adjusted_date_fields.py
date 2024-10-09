"""adjusted date fields

Revision ID: c3dcbf3fc9a9
Revises: c390afbeb713
Create Date: 2024-10-09 12:29:49.112422

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'c3dcbf3fc9a9'
down_revision: Union[str, None] = 'c390afbeb713'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('po_receiver', 'receiver_number',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=120),
               existing_nullable=True)
    op.alter_column('po_receiver', 'receive_date',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)
    op.alter_column('po_receiver', 'start_ship',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)
    op.alter_column('po_receiver', 'stop_ship',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)
    op.add_column('routing_request_1', sa.Column('hdr_start_pickup_dt', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('routing_request_1', 'hdr_start_pickup_dt')
    op.alter_column('po_receiver', 'stop_ship',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
    op.alter_column('po_receiver', 'start_ship',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
    op.alter_column('po_receiver', 'receive_date',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
    op.alter_column('po_receiver', 'receiver_number',
               existing_type=sa.String(length=120),
               type_=mysql.INTEGER(),
               existing_nullable=True)
    # ### end Alembic commands ###