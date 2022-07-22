from casbin.enforcer import Enforcer
from casbin_sqlalchemy_adapter import Adapter


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()




class CasbinRule(Base):
    __tablename__ = "policy"

    id = Column(Integer, primary_key=True)
    ptype = Column(String(255))
    v0 = Column(String(255))
    v1 = Column(String(255))
    v2 = Column(String(255))
    v3 = Column(String(255))
    v4 = Column(String(255))
    v5 = Column(String(255))


adapter = Adapter("postgresql://permissions:permissions@permissions-database:5432/permissions", CasbinRule)


enforcer = Enforcer("policies/ac_model.conf", adapter)
