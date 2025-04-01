from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessário para usar sessões

# Inicializa a pontuação
@app.before_request
def initialize_score():
    if 'score' not in session:
        session['score'] = 0

# Função para verificar a resposta
def verificar_resposta(selected_option, correct_option):
    if str(selected_option) == correct_option:  # Convertendo selected_option para string
        session['score'] += 1


@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/modo_paz')
def modo_paz():
    return render_template('modo_paz.html')

@app.route('/modo_guerra')
def modo_guerra():
    return render_template('modo_guerra.html')

@app.route('/desafio_personagem', methods=['GET', 'POST'])
def desafio_personagem():
    if request.method == 'POST':
        selected_option = int(request.form['option'])
        correct_option = 2 # Exemplo: A resposta correta é a opção 2
        verificar_resposta(selected_option, correct_option)
        return redirect(url_for('quiz_jogo_2'))  # Redireciona para o próximo quiz
    return render_template('quiz_jogo_1.html')


@app.route('/quiz_jogo_2', methods=['GET', 'POST'])
def quiz_jogo_2():
    if request.method == 'POST':
        selected_option = int(request.form['option'])
        correct_option = 3  # Resposta correta para o quiz 2
        verificar_resposta(selected_option, correct_option)
        return redirect(url_for('quiz_jogo_3'))
    return render_template('quiz_jogo_2.html')

@app.route('/quiz_jogo_3', methods=['GET', 'POST'])
def quiz_jogo_3():
    if request.method == 'POST':
        selected_option = int(request.form['option'])
        correct_option = 3  # Resposta correta para o quiz 3
        verificar_resposta(selected_option, correct_option)
        return redirect(url_for('quiz_jogo_4'))
    return render_template('quiz_jogo_3.html')

@app.route('/quiz_jogo_4', methods=['GET', 'POST'])
def quiz_jogo_4():
    if request.method == 'POST':
        selected_option = int(request.form['option'])
        correct_option = 1  # Resposta correta para o quiz 4
        verificar_resposta(selected_option, correct_option)
        return redirect(url_for('quiz_jogo_5'))
    return render_template('quiz_jogo_4.html')

@app.route('/quiz_jogo_5', methods=['GET', 'POST'])
def quiz_jogo_5():
    if request.method == 'POST':
        selected_option = int(request.form['option'])
        correct_option = 2  # Resposta correta para o quiz 5
        verificar_resposta(selected_option, correct_option)
        return redirect(url_for('quiz_jogo_6'))
    return render_template('quiz_jogo_5.html')

@app.route('/quiz_jogo_6', methods=['GET', 'POST'])
def quiz_jogo_6():
    if request.method == 'POST':
        selected_option = int(request.form['option'])
        correct_option = 0  # Resposta correta para o quiz 6
        verificar_resposta(selected_option, correct_option)
        return redirect(url_for('quiz_jogo_7'))
    return render_template('quiz_jogo_6.html')

@app.route('/quiz_jogo_7', methods=['GET', 'POST'])
def quiz_jogo_7():
    if request.method == 'POST':
        selected_option = int(request.form['option'])
        correct_option = 1  # Resposta correta para o quiz 7
        verificar_resposta(selected_option, correct_option)
        return redirect(url_for('quiz_jogo_8'))
    return render_template('quiz_jogo_7.html')

@app.route('/quiz_jogo_8', methods=['GET', 'POST'])
def quiz_jogo_8():
    if request.method == 'POST':
        selected_option = int(request.form['option'])
        correct_option = 0  # Resposta correta para o quiz 8
        verificar_resposta(selected_option, correct_option)
        return redirect(url_for('quiz_jogo_9'))
    return render_template('quiz_jogo_8.html')

@app.route('/quiz_jogo_9', methods=['GET', 'POST'])
def quiz_jogo_9():
    if request.method == 'POST':
        selected_option = int(request.form['option'])
        correct_option = 0  # Resposta correta para o quiz 9
        verificar_resposta(selected_option, correct_option)
        return redirect(url_for('quiz_jogo_10'))
    return render_template('quiz_jogo_9.html')

@app.route('/quiz_jogo_10', methods=['GET', 'POST'])
def quiz_jogo_10():
    if request.method == 'POST':
        selected_option = int(request.form['option'])
        correct_option = 3  # Resposta correta para o quiz 10
        verificar_resposta(selected_option, correct_option)
        return redirect(url_for('quiz_jogo_11'))
    return render_template('quiz_jogo_10.html')

@app.route('/quiz_jogo_11', methods=['GET', 'POST'])
def quiz_jogo_11():
    # Ao final do quiz, calculamos a pontuação e redirecionamos para a página de resultado
    score = session['score']
    print(f'Valor de score: {score}')  # Adicione esta linha para depurar

    if score <= 4:
        return redirect(url_for('bad_end'))  # Fim ruim
    elif 4 < score <= 8:
        return redirect(url_for('neutral_end'))  # Fim neutro
    elif score > 8:
        return redirect(url_for('good_end'))  # Fim bom

@app.route('/quiz_nome_personagem')
def quiz_nome_personagem():
    return render_template('nome.html')

@app.route('/bad_end')
def bad_end():
    return render_template('bad_end.html')

@app.route('/neutral_end')
def neutral_end():
    return render_template('neutral_end.html')

@app.route('/good_end')
def good_end():
    return render_template('good_end.html')

if __name__ == '__main__':
    app.run(debug=True)
