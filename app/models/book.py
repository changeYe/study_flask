from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False,comment='标题')
    author = Column(String(30), default='未名',comment='作者')
    binding = Column(String(20))
    publisher = Column(String(50),comment='出版社')
    price = Column(String(20),comment='价格')
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass
