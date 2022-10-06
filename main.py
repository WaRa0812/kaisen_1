from kaisen import app
from flask import render_template, request
import math

@app.route('/')
def base():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    bhaisui = request.form['bhaisui']
    bsoukou = request.form['bsoukou']
    tairyoku = int(bhaisui)*2 + int(bsoukou)*20
    bsyuhoukoukei = request.form['bsyuhoukoukei']
    bsyuhousuu = request.form['bsyuhousuu']
    bhukuhoukoukei = request.form['bhukuhoukoukei']
    bhukuhousuu = request.form['bhukuhousuu']
    hou = (int(bsyuhoukoukei)+int(bhukuhoukoukei))*(int(bsyuhousuu)+int(bhukuhousuu))*3
    bgyoraikoukei = request.form['bgyoraikoukei']
    bgyoraisuu = request.form['bgyoraisuu']
    gyo1 = int(bgyoraikoukei)*5
    gyo2 = int(bgyoraisuu)
    bkoukakukoukei = request.form['bkoukakukoukei']
    bkoukakusuu = request.form['bkoukakusuu']
    koukaku = int(bkoukakukoukei)*int(bkoukakusuu)*8
    bkikankoukei1 = request.form['bkikankoukei1']
    bkikansuu1 = request.form['bkikansuu1']
    bkikankoukei2 = request.form['bkikankoukei2']
    bkikansuu2 = request.form['bkikansuu2']
    kikan = (int(bkikankoukei1)+int(bkikankoukei2))*(int(bkikansuu1)+int(bkikansuu2))*5
    bzentyou= request.form['bzentyou']
    taikuu = (int(koukaku)+int(kikan))/math.isqrt(int(bzentyou))
    bbaku = request.form['bbaku']
    baku = int(bbaku)*800
    bki = request.form['bki']
    ki = int(bki)*1000
    bsoku= request.form['bsoku']
    soku = bsoku
    return render_template('index.html', tairyoku=tairyoku, hou=hou, gyo1=gyo1, gyo2=gyo2, baku=baku, ki=ki, soku=soku, taikuu=taikuu) 
