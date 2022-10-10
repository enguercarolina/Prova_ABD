class proprietario(base):
    __tablename__ = "proprietario"
    id_proprietario = Column(Integer, primary_key=True)
    nome_proprietario = Column(String(200), nullable=False)

class imovel(base):
    __tablename__ = "imovel"
    id_imovel = Column(Integer, primary_key=True)

class inquilino(base):
    __tablename__ = "inquilino"
    id_inquilino = Column(Integer, primary_key=True)
    nome_inquilino = Column(String(200), nullable=False)

class corretor(base):
    __tablename__ = "corretor"
    id_corretor = Column(Integer, primary_key=True)
    nome_corretor = Column(String(200), nullable=False)

Base.metadata.drop.all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(engine)
proprietario = [proprietario(
    id_proprietario = "1"
    nome_proprietario = "Euvina")]
imovel = [imovel(
    id_imovel = "2")]
inquilino = [inquilino(
    id_inquilino = "3",
    nome_inquilino = 'João Garcia')]
corretor = [corretor(
    id_corretor = "4",
    nome_corretor = "Maria Da Graça"]
    
with Session.begin() as session:
    for proprietario in proprietario:
    session.add(proprietario)
        
with Session.begin as session:
    for imovel in imovel:
    session.add(imovel)
    
with Session.begin() as session
    for inquilino in inquilino:
    session.add(inquilino)
        
with Session.begin() as session
    for corretor in corretor:
    session.add(corretor)