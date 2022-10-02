from flask import Flask, render_template, Response, request
app = Flask(__name__)

@app.route('/<discord_id>')
def index(discord_id):
    return render_template('index.html', discordId = discord_id)

@app.route('/sync', methods=['POST'])
def sync():
    discord_id = request.json['discordId']
    wallet_address = request.json['walletAddress']
    with open('log.txt', 'r+') as f:
        file = f.read()
        if discord_id in file:
            if wallet_address in file:
                Pass
            else:
                f.write(' ' + wallet_address)
        else:
            f.write('\n' + discord_id + ' ' + wallet_address)
    f.close()

@app.route('/read', methods=['POST'])
def read():
    discord_id = request.json['discordId']
    with open('log.txt', 'r') as f:
        file = f.read()
        if discord_id in file:
            wallet_addresses = file.split(discord_id)[1].split(' ')
            wallet_addresses.pop(0)
            return Response(str(wallet_addresses), mimetype='application/json')
        else:
            return Response('No wallet address found', mimetype='application/json')