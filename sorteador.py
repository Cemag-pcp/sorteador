import random
import streamlit as st

import base64

#@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file) 
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: contain;
    background-repeat: repeat;
    background-attachment: scroll; # doesn't work
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('sequencia.png')

tabs_font_css = """
<style>
div[class*="stTextInput"] label p {
font-size: 26px;
color: black;
}
</style>
"""

st.write(tabs_font_css, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; font-size:50px; color: black'>Sorteador de lovezim</h1>", unsafe_allow_html=True)

nomes = st.text_input("Insira os nomes separados por vírgula") # entrada de texto para os nomes separados por vírgula

nomes = [nome.strip() for nome in nomes.split(",")] # separa os nomes pelo caractere "," e remove espaços em branco antes e depois de cada nome

if st.button("Sortear"):
    if nomes:
        nome_sorteado = random.choice(nomes) # sorteia um nome aleatório da lista
        st.write("O nome sorteado foi:", nome_sorteado) # exibe o nome sorteado
    else:
        st.write("Nenhum nome encontrado") # exibe mensagem de erro se a lista de nomes estiver vaziaor