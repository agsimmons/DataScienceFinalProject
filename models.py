import postgres_engine

from sqlalchemy import Column, Boolean, BigInteger, String, Date
from sqlalchemy.ext.declarative import declarative_base

engine = postgres_engine.get_engine()

Base = declarative_base()


class Smart(Base):
    __tablename__ = 'data'

    id = Column(BigInteger, primary_key=True)

    date = Column(Date)

    serial_number = Column(String)
    model = Column(String)

    capacity_bytes = Column(BigInteger)

    failure = Column(Boolean)

    smart_1_normalized = Column(BigInteger)
    smart_1_raw = Column(BigInteger)
    smart_2_normalized = Column(BigInteger)
    smart_2_raw = Column(BigInteger)
    smart_3_normalized = Column(BigInteger)
    smart_3_raw = Column(BigInteger)
    smart_4_normalized = Column(BigInteger)
    smart_4_raw = Column(BigInteger)
    smart_5_normalized = Column(BigInteger)
    smart_5_raw = Column(BigInteger)
    smart_7_normalized = Column(BigInteger)
    smart_7_raw = Column(BigInteger)
    smart_8_normalized = Column(BigInteger)
    smart_8_raw = Column(BigInteger)
    smart_9_normalized = Column(BigInteger)
    smart_9_raw = Column(BigInteger)
    smart_10_normalized = Column(BigInteger)
    smart_10_raw = Column(BigInteger)
    smart_11_normalized = Column(BigInteger)
    smart_11_raw = Column(BigInteger)
    smart_12_normalized = Column(BigInteger)
    smart_12_raw = Column(BigInteger)
    smart_13_normalized = Column(BigInteger)
    smart_13_raw = Column(BigInteger)
    smart_15_normalized = Column(BigInteger)
    smart_15_raw = Column(BigInteger)
    smart_22_normalized = Column(BigInteger)
    smart_22_raw = Column(BigInteger)
    smart_23_normalized = Column(BigInteger)
    smart_23_raw = Column(BigInteger)
    smart_24_normalized = Column(BigInteger)
    smart_24_raw = Column(BigInteger)
    smart_177_normalized = Column(BigInteger)
    smart_177_raw = Column(BigInteger)
    smart_179_normalized = Column(BigInteger)
    smart_179_raw = Column(BigInteger)
    smart_181_normalized = Column(BigInteger)
    smart_181_raw = Column(BigInteger)
    smart_182_normalized = Column(BigInteger)
    smart_182_raw = Column(BigInteger)
    smart_183_normalized = Column(BigInteger)
    smart_183_raw = Column(BigInteger)
    smart_184_normalized = Column(BigInteger)
    smart_184_raw = Column(BigInteger)
    smart_187_normalized = Column(BigInteger)
    smart_187_raw = Column(BigInteger)
    smart_188_normalized = Column(BigInteger)
    smart_188_raw = Column(BigInteger)
    smart_189_normalized = Column(BigInteger)
    smart_189_raw = Column(BigInteger)
    smart_190_normalized = Column(BigInteger)
    smart_190_raw = Column(BigInteger)
    smart_191_normalized = Column(BigInteger)
    smart_191_raw = Column(BigInteger)
    smart_192_normalized = Column(BigInteger)
    smart_192_raw = Column(BigInteger)
    smart_193_normalized = Column(BigInteger)
    smart_193_raw = Column(BigInteger)
    smart_194_normalized = Column(BigInteger)
    smart_194_raw = Column(BigInteger)
    smart_195_normalized = Column(BigInteger)
    smart_195_raw = Column(BigInteger)
    smart_196_normalized = Column(BigInteger)
    smart_196_raw = Column(BigInteger)
    smart_197_normalized = Column(BigInteger)
    smart_197_raw = Column(BigInteger)
    smart_198_normalized = Column(BigInteger)
    smart_198_raw = Column(BigInteger)
    smart_199_normalized = Column(BigInteger)
    smart_199_raw = Column(BigInteger)
    smart_200_normalized = Column(BigInteger)
    smart_200_raw = Column(BigInteger)
    smart_201_normalized = Column(BigInteger)
    smart_201_raw = Column(BigInteger)
    smart_220_normalized = Column(BigInteger)
    smart_220_raw = Column(BigInteger)
    smart_222_normalized = Column(BigInteger)
    smart_222_raw = Column(BigInteger)
    smart_223_normalized = Column(BigInteger)
    smart_223_raw = Column(BigInteger)
    smart_224_normalized = Column(BigInteger)
    smart_224_raw = Column(BigInteger)
    smart_225_normalized = Column(BigInteger)
    smart_225_raw = Column(BigInteger)
    smart_226_normalized = Column(BigInteger)
    smart_226_raw = Column(BigInteger)
    smart_235_normalized = Column(BigInteger)
    smart_235_raw = Column(BigInteger)
    smart_240_normalized = Column(BigInteger)
    smart_240_raw = Column(BigInteger)
    smart_241_normalized = Column(BigInteger)
    smart_241_raw = Column(BigInteger)
    smart_242_normalized = Column(BigInteger)
    smart_242_raw = Column(BigInteger)
    smart_250_normalized = Column(BigInteger)
    smart_250_raw = Column(BigInteger)
    smart_251_normalized = Column(BigInteger)
    smart_251_raw = Column(BigInteger)
    smart_252_normalized = Column(BigInteger)
    smart_252_raw = Column(BigInteger)
    smart_254_normalized = Column(BigInteger)
    smart_254_raw = Column(BigInteger)
    smart_255_normalized = Column(BigInteger)
    smart_255_raw = Column(BigInteger)


Base.metadata.create_all(engine)
