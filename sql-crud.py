from django.views import (
    create_engine, Column, Integer, String
)
from .models import Post
from .forms import CommentForm


db = create_engine("postgresql:///thenews")
news = declarative_news()


class CommentForm(news):
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email_adress = Column(String)


Session = sessionmaker(db)

session = Session()

news.metadata.create_all(db)


username = input("Enter username: ")
password = input("Enter password: ")
   if commentform is not None:
        print("comment Found: ", commentform.username +
              " " + commentform.password)
        confirmation = input(
            "Are you sure you want to delete this comment? (y/n) ")
        if confirmation.lower() == "y":
            session.delete(commentform)
            session.commit()
            print("Comment has been deleted")
        else:
            print("Comment not deleted")
    else:
        print("No comment found")
