from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = 'Knowledge'
	student_id= Column(Integer, primary_key=True)
	wiki_article=Column(String)
	topic=Column(String)
	rating=Column(Integer)
	def __repr__(self):
		return("if you want to learn about {}, you sould look at the Wikipedia article called {} we gave this article a rating of {} out of 10!").format(
			self.wiki_article, self.topic, self.rating)

