import os

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if not os.path.isfile('quotes.db'):
    os.system('touch quotes.db')

__BASE = declarative_base()
__engine = create_engine('sqlite:///quotes.db')
__BASE.metadata.create_all(__engine)
__BASE.metadata.bind = __engine
__session = sessionmaker(bind=__engine)()


class Quote(__BASE):
    __tablename__ = 'quote'

    id = Column(Integer, primary_key=True)
    quote = Column(Text, nullable=False)


def _get_session():
    return __session


def add_quote(new_quote):
    __session.add(Quote(quote=new_quote))
    __session.commit()
    number = __session.query(Quote).filter_by(quote=new_quote).first().id

    return 'I am Jack\'s new quote with number {}'.format(number), number


def get_amount_of_quotes():
    return len(__session.query(Quote).all())


def get_random_quote(random_int):
    return __session.query(Quote).filter_by(id=random_int).first().quote
