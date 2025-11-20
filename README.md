# Projeto de Estudo – Ransomware

Este documento explica como funciona o código que simula o comportamento de um ransomware. Ele não deve ser executado em computadores pessoais ou ambientes reais.

---

## Objetivo do Projeto
O objetivo é entender como um ransomware funciona para que possamos aprender a nos defender.

---

## O que o Código Faz

1. **Gera uma chave de criptografia** usando a biblioteca `cryptography`.
2. **Salva essa chave** em um arquivo chamado `chave.key`.
3. **Procura arquivos .txt** no mesmo diretório do programa.
4. **Criptografa esses arquivos**, deixando-os inacessíveis.
5. **Cria um arquivo de aviso**, chamado "LEIA ISSO.txt", simulando uma mensagem de resgate.
6. **Envia a chave por e-mail** para o endereço configurado no código.
7. **Apaga a chave do computador**, dificultando a recuperação dos arquivos.

---

## Como Proceder Após um Comprometimento

Caso um computador seja realmente infectado por um ransomware, siga estes passos:

1. **Desconecte o computador da internet ou da rede** para evitar que o ataque se espalhe.
2. **Avise imediatamente a equipe de TI ou segurança** responsável.
3. **Não apague arquivos ou formate o computador** antes que um profissional analise o caso.
4. **Preserve evidências**, como mensagens de erro e logs.
5. **Verifique quais máquinas foram afetadas** e qual é o alcance do problema.
6. **Use backups confiáveis** para restaurar o sistema, se possível.
7. **Registre o incidente** para aprendizado futuro.

---

## O Que Não Fazer Após Ser Comprometido

- Não pague o resgate. Não há garantia de que os arquivos serão recuperados.
- Não reinicie ou formate o computador sem orientação.
- Não baixe ferramentas desconhecidas para tentar recuperar arquivos.
- Não tente descriptografar arquivos por conta própria.
- Não reconecte o computador à rede antes do tratamento adequado.
- Não ignore o incidente após recuperar o sistema. É importante revisar falhas e prevenir novos ataques.
