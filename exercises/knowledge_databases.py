from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(wiki_article, topic, rating):
	new_object = Knowledge(
		wiki_article=wiki_article,
		topic=topic,
        rating=rating)
	session.add(new_object)
	session.commit()

def query_all_articles():
	articles= session.query(
		Knowledge).all()
	return articles

def query_article_by_topic(the_topic):
	article = session.query(
		Knowledge).filter_by(
		topic=the_topic).first()
	return article

def delete_article_by_topic(the_topic):
	article = session.query(
		Knowledge).filter_by(
		topic=the_topic).delete()
	session.commit()

def delete_all_articles():
	articles= session.query(
		Knowledge).delete()
	session.commit()

def edit_article_rating():
	pass

add_article("wiki.cats","cats", 7)
add_article("wiki.dogs","dogs", 8)
add_article("wiki.pizza","pizza", 10)
print(query_all_articles())
#print(query_article_by_topic("cats"))
#print(delete_article_by_topic("dogs"))
print("new line")
print(query_all_articles())
print("new line")
delete_all_articles()
print("new line")
print(query_all_articles())

