"""persist volume_id on revision chapter snapshots

Revision ID: 1022
Revises: 1021
Create Date: 2026-10-03
"""

from __future__ import annotations

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "1022"
down_revision: Union[str, Sequence[str], None] = "1021"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "revision_chapter_snapshots",
        sa.Column("volume_id", sa.String(), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("revision_chapter_snapshots", "volume_id")
