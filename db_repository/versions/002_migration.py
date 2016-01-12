from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
courses = Table('courses', post_meta,
    Column('uid', Integer, primary_key=True, nullable=False),
    Column('course_id', String(length=50)),
    Column('subject', String(length=10)),
    Column('catalog_number', String(length=10)),
    Column('title', String(length=200)),
    Column('description', String(length=1000)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['courses'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['courses'].drop()
