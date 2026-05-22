from flask import Flask, request, jsonify, render_template, redirect, url_for

@app.route('/')
def index():
    return render_template('index.html') # Tu archivo index cyberpunk

@app.route('/verify-login', append_slash=False, methods=['POST'])
def verify_login():
    data = request.json
    # Aquí recibes el 'nullifier_hash', 'merkle_root' y 'proof' de World ID.
    print("Datos recibidos de Worldcoin:", data)
    
    # (Opcional) Aquí puedes meter la lógica de verificación contra la API de Worldcoin si lo requieres.
    # Por ahora, si todo se ve bien, le dices al frontend que fue exitoso:
    return jsonify({"status": "success"}), 200

@app.route('/dashboard')
def dashboard():
    return "¡Bienvenido al Panel de CharlyCoin!" # Cambia esto por tu página interna del bot
