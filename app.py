from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Equipo, Jugador, Partido, Resultado
from itertools import combinations
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///torneo.db'
app.config['SECRET_KEY'] = 'clave_secreta_torneo_2024'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ===================== INICIO =====================
@app.route('/')
def index():
    equipos = Equipo.query.all()
    partidos = Partido.query.all()
    return render_template('index.html', equipos=equipos, partidos=partidos)

# ===================== EQUIPOS =====================
@app.route('/equipos')
def listar_equipos():
    equipos = Equipo.query.all()
    return render_template('equipos/listar.html', equipos=equipos)

@app.route('/equipos/nuevo', methods=['GET', 'POST'])
def nuevo_equipo():
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        facultad = request.form['facultad'].strip()
        if not nombre or not facultad:
            flash('Nombre y facultad son obligatorios.', 'danger')
            return redirect(url_for('nuevo_equipo'))
        if Equipo.query.filter_by(nombre=nombre).first():
            flash('Ya existe un equipo con ese nombre.', 'danger')
            return redirect(url_for('nuevo_equipo'))
        equipo = Equipo(nombre=nombre, facultad=facultad)
        db.session.add(equipo)
        db.session.commit()
        flash(f'Equipo "{nombre}" registrado exitosamente.', 'success')
        return redirect(url_for('listar_equipos'))
    return render_template('equipos/nuevo.html')

@app.route('/equipos/<int:id>')
def detalle_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    return render_template('equipos/detalle.html', equipo=equipo)

# ===================== JUGADORES =====================
@app.route('/jugadores')
def listar_jugadores():
    jugadores = Jugador.query.all()
    return render_template('jugadores/listar.html', jugadores=jugadores)

@app.route('/jugadores/nuevo', methods=['GET', 'POST'])
def nuevo_jugador():
    equipos = Equipo.query.all()
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        numero = request.form['numero']
        equipo_id = request.form['equipo_id']
        if not nombre or not equipo_id:
            flash('Nombre y equipo son obligatorios.', 'danger')
            return redirect(url_for('nuevo_jugador'))
        jugador = Jugador(nombre=nombre, numero=numero, equipo_id=equipo_id)
        db.session.add(jugador)
        db.session.commit()
        flash(f'Jugador "{nombre}" registrado exitosamente.', 'success')
        return redirect(url_for('listar_jugadores'))
    return render_template('jugadores/nuevo.html', equipos=equipos)

# ===================== CALENDARIO =====================
@app.route('/calendario')
def ver_calendario():
    partidos = Partido.query.order_by(Partido.jornada, Partido.id).all()
    return render_template('calendario/ver.html', partidos=partidos)

@app.route('/calendario/generar', methods=['POST'])
def generar_calendario():
    equipos = Equipo.query.all()
    if len(equipos) < 2:
        flash('Se necesitan al menos 2 equipos para generar el calendario.', 'danger')
        return redirect(url_for('ver_calendario'))
    if Partido.query.count() > 0:
        flash('El calendario ya fue generado. Elimina los partidos existentes para regenerar.', 'warning')
        return redirect(url_for('ver_calendario'))

    pares = list(combinations(equipos, 2))
    random.shuffle(pares)

    jornada = 1
    por_jornada = max(1, len(equipos) // 2)

    for i, (local, visitante) in enumerate(pares):
        if i > 0 and i % por_jornada == 0:
            jornada += 1
        partido = Partido(equipo_local_id=local.id, equipo_visitante_id=visitante.id, jornada=jornada)
        db.session.add(partido)

    db.session.commit()
    flash('Calendario generado exitosamente.', 'success')
    return redirect(url_for('ver_calendario'))

# ===================== RESULTADOS =====================
@app.route('/resultados')
def listar_resultados():
    partidos_jugados = Partido.query.filter_by(jugado=True).all()
    return render_template('resultados/listar.html', partidos=partidos_jugados)

@app.route('/resultados/registrar/<int:partido_id>', methods=['GET', 'POST'])
def registrar_resultado(partido_id):
    partido = Partido.query.get_or_404(partido_id)
    if partido.jugado:
        flash('Este partido ya tiene un resultado registrado.', 'warning')
        return redirect(url_for('ver_calendario'))

    jugadores_local = Jugador.query.filter_by(equipo_id=partido.equipo_local_id).all()
    jugadores_visitante = Jugador.query.filter_by(equipo_id=partido.equipo_visitante_id).all()

    if request.method == 'POST':
        goles_local = int(request.form.get('goles_local', 0))
        goles_visitante = int(request.form.get('goles_visitante', 0))
        goleadores_ids = request.form.getlist('goleadores')

        partido.goles_local = goles_local
        partido.goles_visitante = goles_visitante
        partido.jugado = True

        for jug_id in goleadores_ids:
            jugador = Jugador.query.get(int(jug_id))
            if jugador:
                jugador.goles += 1

        # Actualizar puntos en tabla
        if goles_local > goles_visitante:
            partido.equipo_local.puntos += 3
            partido.equipo_local.partidos_ganados += 1
            partido.equipo_visitante.partidos_perdidos += 1
        elif goles_visitante > goles_local:
            partido.equipo_visitante.puntos += 3
            partido.equipo_visitante.partidos_ganados += 1
            partido.equipo_local.partidos_perdidos += 1
        else:
            partido.equipo_local.puntos += 1
            partido.equipo_visitante.puntos += 1
            partido.equipo_local.partidos_empatados += 1
            partido.equipo_visitante.partidos_empatados += 1

        partido.equipo_local.partidos_jugados += 1
        partido.equipo_visitante.partidos_jugados += 1
        partido.equipo_local.goles_favor += goles_local
        partido.equipo_local.goles_contra += goles_visitante
        partido.equipo_visitante.goles_favor += goles_visitante
        partido.equipo_visitante.goles_contra += goles_local

        db.session.commit()
        flash('Resultado registrado exitosamente.', 'success')
        return redirect(url_for('ver_tabla'))

    return render_template('resultados/registrar.html', partido=partido,
                           jugadores_local=jugadores_local,
                           jugadores_visitante=jugadores_visitante)

# ===================== TABLA DE POSICIONES =====================
@app.route('/tabla')
def ver_tabla():
    equipos = Equipo.query.order_by(
        Equipo.puntos.desc(),
        (Equipo.goles_favor - Equipo.goles_contra).desc()
    ).all()
    return render_template('tabla/ver.html', equipos=equipos)

# ===================== REPORTES =====================
@app.route('/reportes')
def ver_reportes():
    goleadores = Jugador.query.filter(Jugador.goles > 0).order_by(Jugador.goles.desc()).limit(10).all()
    partidos_jugados = Partido.query.filter_by(jugado=True).count()
    partidos_pendientes = Partido.query.filter_by(jugado=False).count()
    total_goles = sum(j.goles for j in Jugador.query.all())
    return render_template('reportes/ver.html',
                           goleadores=goleadores,
                           partidos_jugados=partidos_jugados,
                           partidos_pendientes=partidos_pendientes,
                           total_goles=total_goles)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
