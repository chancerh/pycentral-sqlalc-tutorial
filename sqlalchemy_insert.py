from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import Address, Base, Person

engine = create_engine('sqlite:///sqlalchemy_example.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() insance establishes all conversations with the database and
# represents a "staging zone" for all of the objects loaded into the database
# session object. Any changes made against the objects in the session wont be
# persisted into the database until you call session.commit(). If you aren't
# happy with the changes, you can roll them back to the last commit by callsing
# session.rollback()
session = DBSession()

# Insert a Person into the person table
new_person = Person(name='new person')
session.add(new_person)
session.commit()

# Insert an address into the address table
new_address = Address(post_code='0000', person=new_person)
session.add(new_address)
session.commit()
