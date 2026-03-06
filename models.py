from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Equipo(db.Model):
    __tablename__ = 'equipos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    facultad = db.Column(db.String(100), nullable=False)
    puntos = db.Column(db.Integer, default=0)
    partidos_jugados = db.Column(db.Integer, default=0)
    partidos_ganados = db.Column(db.Integer, default=0)
    partidos_empatados = db.Column(db.Integer, default=0)
    partidos_perdidos = db.Column(db.Integer, default=0)
    goles_favor = db.Column(db.Integer, default=0)
    goles_contra = db.Column(db.Integer, default=0)

    jugadores = db.relationship('Jugador', backref='equipo', lazy=True)

    @property
    def diferencia_goles(self):
        return self.goles_favor - self.goles_contra

    def __repr__(self):
        return f'<Equipo {self.nombre}>'


class Jugador(db.Model):
    __tablename__ = 'jugadores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.Integer)
    goles = db.Column(db.Integer, default=0)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'), nullable=False)

    def __repr__(self):
        return f'<Jugador {self.nombre}>'


class Partido(db.Model):
    __tablename__ = 'partidos'
    id = db.Column(db.Integer, primary_key=True)
    jornada = db.Column(db.Integer, nullable=False)
    equipo_local_id = db.Column(db.Integer, db.ForeignKey('equipos.id'), nullable=False)
    equipo_visitante_id = db.Column(db.Integer, db.ForeignKey('equipos.id'), nullable=False)
    goles_local = db.Column(db.Integer, default=0)
    goles_visitante = db.Column(db.Integer, default=0)
    jugado = db.Column(db.Boolean, default=False)

    equipo_local = db.relationship('Equipo', foreign_keys=[equipo_local_id], backref='partidos_local')
    equipo_visitante = db.relationship('Equipo', foreign_keys=[equipo_visitante_id], backref='partidos_visitante')

    def __repr__(self):
        return f'<Partido {self.equipo_local} vs {self.equipo_visitante}>'


class Resultado(db.Model):
    __tablename__ = 'resultados'
    id = db.Column(db.Integer, primary_key=True)
    partido_id = db.Column(db.Integer, db.ForeignKey('partidos.id'))
    descripcion = db.Column(db.String(300))
