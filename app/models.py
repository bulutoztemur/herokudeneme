from sqlalchemy import create_engine, Column, String, Integer, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


engine = create_engine('postgres://ojrfzzowvvqupi:cd263cf0b985a723b7b087f9c1fdeeac4e225114d64a1871df98a69b03ff23fe@ec2-54-83-55-115.compute-1.amazonaws.com:5432/d4ndo4vffkmgg9')
Session = sessionmaker(bind=engine)

Base = declarative_base()

Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    Password = Column(String(128))

'''
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
'''

class Login(Base):
    __tablename__ = 'logins'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", backref="logins")
    date = Column(DateTime, default=datetime.datetime.utcnow)


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    authername = Column(String)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    categoryname = Column(String)


books_authors_association = Table(
    'books_authors', Base.metadata,
     Column('book_id', Integer, ForeignKey('books.id')),
     Column('author_id', Integer, ForeignKey('authors.id'))
)

books_categories_association = Table(
    'books_categories', Base.metadata,
     Column('book_id', Integer, ForeignKey('books.id')),
     Column('category_id', Integer, ForeignKey('categories.id'))
)

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    bookname = Column(String)
    '''year = Column(Integer, )'''
    summary = Column(String)
    authors = relationship("Author", secondary=books_authors_association)
    categories = relationship("Category", secondary=books_categories_association)


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    commentinfo = Column(String)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    book = relationship("Book", backref="comments")
    user = relationship("User", backref="comments")


class Point(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    pointval = Column(Integer)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    book = relationship("Book", backref="points")
    user = relationship("User", backref="points")