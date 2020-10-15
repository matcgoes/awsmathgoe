from flask import Flask, request, render_template # Importa a biblioteca

application = Flask(__name__) # Inicializa a aplicação

@application.route('/') # Nova rota
def main():
    resultado = None
    media = None    

    primeira = request.args.get('primeira')
    segunda = request.args.get('segunda')

    if primeira and segunda:  
        primeira = float(primeira)
        segunda = float(segunda)

        media = (primeira + segunda) / 2
        if media >= 7:
            resultado = 'Aprovado'
        elif media >= 5:
            resultado = 'Recuperação'
        else:
            resultado = 'Reprovado'

    return render_template('index.html', media=media,
                                         resultado=resultado)

if __name__ == '__main__':
  application.run(host='0.0.0.0', debug=True) # Executa a aplicação
