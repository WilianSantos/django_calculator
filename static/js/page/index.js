document.addEventListener('DOMContentLoaded', () => {
    const panel = document.getElementById('panel')
    let expression = panel.textContent || '';

    const inputParameters = document.getElementById('parameters')
    const inputResult = document.getElementById('result')
    const form = document.getElementById('form-calculator')

    document.querySelectorAll('.btnCalculator').forEach(btn => {
        btn.addEventListener('click', () => {
            const value = btn.dataset.value

            if (value === '=') {
                try {
                    const result = eval(expression)
                    panel.textContent = result

                    inputParameters.value = expression
                    inputResult.value = result

                    form.submit()
                } catch {
                    panel.textContent = 'Erro'
                }
            }

            else if (value === 'clearScreen') {
                expression = ''
                panel.textContent = ''
            }

            else if (value === 'plusminus') {
                if (expression.trim() === '') {
                    // Começar com número negativo
                    expression = '-';
                    panel.textContent = expression;
                    return;
                }

                if (expression.trim() === '-') {
                    // Voltar para vazio (positivo)
                    expression = '';
                    panel.textContent = expression;
                    return;
                }

                const tokens = expression.trim().split(' ');
                const last = tokens[tokens.length - 1];
                const thirdLast = tokens[tokens.length - 3];

                if (['+', '-', '*', '/'].includes(last) && thirdLast !== '-') {
                    // Após operador, adicionar sinal negativo
                    expression += ' -';
                    panel.textContent = expression;
                    return;
                }
                if(last === '-' && ['+', '-', '*', '/', '%'].includes(thirdLast)) {
                    // Remove o sinal negativo após o operador
                    tokens.pop(); // remove o último item ('-')
                    expression = tokens.join(' ');
                    panel.textContent = expression;
                    return;
                }

                // Se o último é um número → inverter sinal
                let popped = tokens.pop();
                if (!popped || isNaN(popped)) return;

                if (popped.startsWith('-')) {
                    popped = popped.slice(1);
                } else {
                    popped = '-' + popped;
                }

                tokens.push(popped);
                expression = tokens.join(' ');
                panel.textContent = expression;
            }



            else if (['+', '-', '*', '/', '%'].includes(value)) {
                // Evita operadores duplicados
                if (expression.trim().endsWith('+') || expression.trim().endsWith('-') || 
                    expression.trim().endsWith('*') || expression.trim().endsWith('/')) {
                    return
                }
                expression += ' ' + value + ' '
                panel.textContent = expression
            }

            else {
                expression += value
                panel.textContent = expression
            }
        })
    })
})
