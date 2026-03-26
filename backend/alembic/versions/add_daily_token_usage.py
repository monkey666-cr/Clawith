"""Add daily_token_usage table.

Revision ID: add_daily_token_usage
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "add_daily_token_usage"
down_revision = "add_agentbay_enum_value"
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Create the daily_token_usage table for time-series analytics
    op.create_table(
        "daily_token_usage",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("tenant_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("tenants.id"), nullable=False, index=True),
        sa.Column("agent_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("agents.id"), nullable=False, index=True),
        sa.Column("date", sa.DateTime(timezone=True), nullable=False, index=True),
        sa.Column("tokens_used", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
        sa.UniqueConstraint("agent_id", "date", name="uq_daily_token_usage_agent_date"),
    )

def downgrade() -> None:
    op.drop_table("daily_token_usage")
