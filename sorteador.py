import random
import streamlit as st

st.title("Sorteador de nomes")

nomes = st.text_input("Insira os nomes separados por vírgula") # entrada de texto para os nomes separados por vírgula

nomes = [nome.strip() for nome in nomes.split(",")] # separa os nomes pelo caractere "," e remove espaços em branco antes e depois de cada nome

if st.button("Sortear"):
    if nomes:
        nome_sorteado = random.choice(nomes) # sorteia um nome aleatório da lista
        st.write("O nome sorteado foi:", nome_sorteado) # exibe o nome sorteado
    else:
        st.write("Nenhum nome encontrado") # exibe mensagem de erro se a lista de nomes estiver vaziaor