import json
from flask import Flask, render_template
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
import psycopg2
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = 'test.mosquitto.org'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False

mqtt = Mqtt(app)
socketio = SocketIO(app)
bootstrap = Bootstrap(app)


# Conexion con timescaledb
conn = psycopg2.connect(
    dbname="sensor_data",
    user="admin",
    password="admin123",
    host="localhost",
    port=5432
)

cursor = conn.cursor()

@app.route('/')
def index():
    
    return render_template('charts.html')

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('upiih_h')
    mqtt.subscribe('upiih_m')

latest_temp = None
latest_hum = None

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    global latest_temp, latest_hum

    topic = message.topic
    value = float(message.payload.decode())
    now = datetime.utcnow()

    if topic == "upiih_m":
        latest_temp = value
    elif topic == "upiih_h":
        latest_hum = value

    # Solo guardamos y emitimos cuando tenemos ambos
    if latest_temp is not None and latest_hum is not None:
        try:
            cursor.execute("""
                INSERT INTO dht_readings (time, temperature, humidity)
                VALUES (%s, %s, %s)
            """, (now, latest_temp, latest_hum))
            conn.commit()
            print(f"📥 Guardado en DB: {latest_temp}°C, {latest_hum}%")

            # Emitimos al frontend por WebSocket
            socketio.emit('mqtt_message', data={
                'timestamp': now.isoformat(),
                'temperature': latest_temp,
                'humidity': latest_hum
            })

        except Exception as e:
            print("Error on insert -> ", e)

        # Reseteamos los datos
        latest_temp = None
        latest_hum = None


@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    # print(level, buf)
    return

@socketio.on('subscribe')
def handle_subscribe(json_str):
    
    mqtt.subscribe('upiih_m') 
    mqtt.subscribe('upiih_h') 

@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    mqtt.unsubscribe_all()

@socketio.on('load_history')
def handle_load_history(limit=20):
    try:
        cursor.execute("""
            SELECT time, temperature, humidity
            FROM dht_readings
            ORDER BY time DESC
            LIMIT %s
        """, (limit,))
        rows = cursor.fetchall()
        rows.reverse()  # Para ordenarlos cronológicamente

        data = [
            {
                "timestamp": r[0].isoformat(),
                "temperature": r[1],
                "humidity": r[2]
            }
            for r in rows
        ]

        socketio.emit('history_data', data)

    except Exception as e:
        print("Error when consulting history -> ", e)
        socketio.emit('history_data', [])


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=True)