from StoringObjectsDatabase import Base, User, Post, Tag
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table


#  database engine
engine = create_engine('sqlite:///blog.db')

# database tables
Base.metadata.create_all(engine)

# csession factory
Session = sessionmaker(bind=engine)


session = Session()

#  users
saron = User(name='Saron', email='saron@gmail.com', password='password', role ='developer')
berhane = User(name='Berhane', email='berhane@gmail.com', password='password', role ='developer')
zebiba = User(name='Zebiba', email='zebiba@gmail.com', password='password', role ='developer')

# add the users to the session
session.add_all([saron, berhane, zebiba])
session.commit()

# tags
python = Tag(name='Python')
sqlalchemy = Tag(name='SQLAlchemy')
flask = Tag(name='Flask')

# adding tags to the session
session.add_all([python, sqlalchemy, flask])
session.commit()

# creating a post
post = Post(title='Hello, Everyone!', content='This is my first blog post', author=saron)

# tags to the post
tag_ids = [python.id, sqlalchemy.id]
post.tags = [session.query(Tag).get(tag_id) for tag_id in tag_ids]

#post to the session
session.add(post)
session.commit()

# query the database
posts = session.query(Post).all()
print(posts)

# update post
post.title = 'My First Blog Post'
session.commit()

# delete post
session.delete(post)
session.commit()

# closing the session
session.close()
