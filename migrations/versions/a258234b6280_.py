"""empty message

Revision ID: a258234b6280
Revises: 31955f542d8b
Create Date: 2018-08-15 23:25:25.858126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a258234b6280'
down_revision = '31955f542d8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mastodon_host', sa.Column('defer_until', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mastodon_host', 'defer_until')
    # ### end Alembic commands ###