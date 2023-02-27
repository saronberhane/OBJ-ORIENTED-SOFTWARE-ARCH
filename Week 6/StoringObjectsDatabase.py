from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# create engine and session
engine = create_engine('sqlite:///blog.db')
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

# base class for declarative models
Base = declarative_base()


# creating all tables 
Base.metadata.create_all(engine)

# create many-to-many relationship between posts and tags
post_tag_association_table = Table('post_tag_association', Base.metadata,
    Column('post_id', Integer, ForeignKey('post.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)

#user
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(String(50), nullable=False, default='reader')


# adding user to database
def add_user(name, email, password, role='reader'):
    user = User(name=name, email=email, password=password, role=role)
    session.add(user)
    session.commit()
    return user

# post 
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    author = relationship('User', backref='posts')
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', backref='posts')
    tags = relationship('Tag', secondary=post_tag_association_table, backref='posts')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# adding post to database
def add_post(title, content, author_id, category_id=None, tag_ids=None):
    post = Post(title=title, content=content, author_id=author_id, category_id=category_id)
    if tag_ids:
        post.tags = [session.query(Tag).get(tag_id) for tag_id in tag_ids]


# comment
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    author = relationship('User')
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship('Post', backref='comments')
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50), nullable=False, default='pending')

# category 
class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)

# tag 
class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)
