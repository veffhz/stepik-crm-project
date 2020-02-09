"""empty message

Revision ID: c4fc191a6e29
Revises: 
Create Date: 2020-02-09 02:58:08.704239

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa

from application.models import ApplicantStatus, GroupCourse, GroupStatus

# revision identifiers, used by Alembic.
revision = 'c4fc191a6e29'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('status', sqlalchemy_utils.types.choice.ChoiceType(GroupStatus), nullable=False),
    sa.Column('course', sqlalchemy_utils.types.choice.ChoiceType(GroupCourse, impl=sa.Integer()), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('mail', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mail')
    )
    op.create_table('applicants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('mail', sa.String(length=80), nullable=False),
    sa.Column('status', sqlalchemy_utils.types.choice.ChoiceType(ApplicantStatus), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mail'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('applicants')
    op.drop_table('users')
    op.drop_table('groups')
    # ### end Alembic commands ###