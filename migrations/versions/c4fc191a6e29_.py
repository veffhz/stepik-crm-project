from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils import ChoiceType

from application.models import ApplicantStatus, GroupCourse, GroupStatus

revision = 'c4fc191a6e29'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('status', ChoiceType(GroupStatus), nullable=False),
    sa.Column('course', ChoiceType(GroupCourse, impl=sa.Integer()), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=False),
    sa.Column('seats', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('applicants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('status', ChoiceType(ApplicantStatus), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('applicants')
    op.drop_table('users')
    op.drop_table('groups')
