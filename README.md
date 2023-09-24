# Funcao-calculadora2-pelo-usuario
## Desafio de projeto sobre função calculadora em Python onde o usuário define a operação.

## Apresentação do Problema

Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:</br>
</br>
1: Soma</br>
2: Subtração</br>
3: Multiplicação</br>
4: Divisão</br>
0: Sair</br>
</br>
Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem <strong>“Essa opção não existe”</strong> e voltar ao menu de opções.</br>
</br>
Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção <strong>“Sair”</strong>, o sistema irá parar.</br>
</br>
É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 
</br>
## Solução para o problema

Aqui está uma função calculadora que atende aos requisitos especificados:</br>
</br>
Calculadora simples que permite ao usuário escolher entre as seguintes operações:</br>
</br>
 &nbsp; 1: Soma</br>
 &nbsp; 2: Subtração</br>
 &nbsp; 3: Multiplicação</br>
 &nbsp; 4: Divisão</br>
&nbsp;  0: Sair</br>
</br>
O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair.</br>
</br>
### Este código funciona da seguinte forma:
</br>
<ul>
<li>A variável opções armazena uma lista com as opções disponíveis.</li>
<li>O loop infinito while True: fica rodando até que o usuário escolha a opção de sair (0).</li>
<li>Na primeira linha do loop, o código exibe as opções para o usuário.</li>
<li>Na segunda linha, o código lê a opção do usuário.</li>
<li>Na terceira linha, o código valida a opção do usuário. Se o usuário inserir um valor que não seja um número, o código exibe a mensagem "Essa opção não existe" e volta ao menu de opções.</li>
<li>Na quarta linha, o código verifica qual opção o usuário escolheu.</li>
<li>Se a opção for 0, o código quebra o loop e o programa termina.</li>
<li>Se a opção for diferente de 0, o código realiza a operação correspondente.</li>
<li>Na quinta linha, o código lê os dois valores da operação.</li>
<li>Na sexta linha, o código calcula o resultado da operação.</li>
<li>Na sétima linha, o código exibe o resultado para o usuário.</li>
</ul>

### Aqui está um exemplo de como o código funciona:

Escolha uma opção:</br>
1: Soma</br>
2: Subtração</br>
3: Multiplicação</br>
4: Divisão</br>
0: Sair</br>
Opção: 1</br>
Digite o primeiro valor:</br>
10</br>
Digite o segundo valor:</br>
20</br>
O resultado é: 30</br>
Escolha uma opção:</br>
1: Soma</br>
2: Subtração</br>
3: Multiplicação</br>
4: Divisão</br>
0: Sair</br>
Opção: 2</br>
Digite o primeiro valor:</br>
30</br>
Digite o segundo valor:</br>
20</br>
O resultado é: 10</br>
Escolha uma opção:</br>
1: Soma</br>
2: Subtração</br>
3: Multiplicação</br>
4: Divisão</br>
0: Sair</br>
Opção: 3</br>
Digite o primeiro valor:</br>
10</br>
Digite o segundo valor:</br>
20</br>
O resultado é: 200</br>
Escolha uma opção:</br>
1: Soma</br>
2: Subtração</br>
3: Multiplicação</br>
4: Divisão</br>
0: Sair</br>
Opção: 4</br>
Digite o primeiro valor:</br>
10</br>
Digite o segundo valor:</br>
20</br>
O resultado é: 0.5</br>
Escolha uma opção:</br>
1: Soma</br>
2: Subtração</br>
3: Multiplicação</br>
4: Divisão</br>
0: Sair</br>
Opção: 0</br>
