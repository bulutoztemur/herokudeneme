from sqlalchemy import create_engine, Column, String, Integer, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    Password = Column(String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Login(Base):
    __tablename__ = 'logins'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
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
    year = Column(Integer, )****
    summary = Column(String)
    image =
    authors = relationship("Author", secondary=books_authors_association)
    categories = relationship("Category", secondary=books_categories_association)



class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    commentinfo = Column(String)
    book = relationship("Book", backref="comments")
    user = relationship("User", backref="comments")

class Point(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    pointval = Column(String)
    book = relationship("Book", backref="points")
    user = relationship("User", backref="points")