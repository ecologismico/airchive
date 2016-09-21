from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
quantities = Table('quantities', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=80)),
    Column('ontology', String(length=80)),
    Column('uom_name', String(length=40)),
    Column('uom_ontology', String(length=80)),
    Column('uom_symbol', String(length=20)),
)

sensors = Table('sensors', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('long_name', String(length=80)),
    Column('short_name', String(length=60)),
    Column('manufacturer', String(length=60)),
    Column('manufacturer_url', String(length=140)),
    Column('urn', String(length=60)),
    Column('first_measurement', DateTime),
    Column('last_measurement', DateTime),
    Column('quantity_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['quantities'].columns['uom_symbol'].create()
    post_meta.tables['sensors'].columns['first_measurement'].create()
    post_meta.tables['sensors'].columns['last_measurement'].create()
    post_meta.tables['sensors'].columns['quantity_id'].create()
    post_meta.tables['sensors'].columns['urn'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['quantities'].columns['uom_symbol'].drop()
    post_meta.tables['sensors'].columns['first_measurement'].drop()
    post_meta.tables['sensors'].columns['last_measurement'].drop()
    post_meta.tables['sensors'].columns['quantity_id'].drop()
    post_meta.tables['sensors'].columns['urn'].drop()
