<%!
import sys
from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.declarative import declarative_base
from alembic import context
from alembic import op
import sqlalchemy as sa

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Set the target metadata for migrations
target_metadata = Base.metadata
%>

# revision identifiers, used by Alembic.
revision = '<%= revision %>'
down_revision = '<%= down_revision %>'
branch_labels = None
depends_on = None

def upgrade():
    # Add your upgrade logic here
    pass

def downgrade():
    # Add your downgrade logic here
    pass
