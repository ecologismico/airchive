from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
stations = Table('stations', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=80)),
    Column('station_url', String(length=140)),
    Column('station_port', Integer),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('institution', String(length=80)),
    Column('description', String(length=200)),
    Column('admin_email', String(length=80)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['stations'].columns['admin_email'].create()
    post_meta.tables['stations'].columns['description'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['stations'].columns['admin_email'].drop()
    post_meta.tables['stations'].columns['description'].drop()
