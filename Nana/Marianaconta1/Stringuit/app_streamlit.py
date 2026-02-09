import streamlit as st

st.title("Calculadora Simples🧮")
st.subheader("Feito com streamlit❤️")
st.text ("byNana⭐")
###
nome = st.text_input("Digite o seu nome:")
bemvindo = st.write(f"BEM VINDO(A) {nome}")
niver = st.date_input("Qual sua data de nascimento?:")
####
v1 = st.number_input("Digite o primeiro valor",0)
v2 = st.number_input("Digite o segundo valor",0)

opcao = st.selectbox("Qual operação deseja realizar?",\
                      ("Soma", "Subtração", "Multiplicação", "Divisão"))

if st.button("Calcular"):
    try:
        if opcao == "Soma":
            st.success(f"{v1 + v2:.2f}")
        elif opcao == "Subtração":
            st.success(f"{v1 - v2:.2f}")
        elif opcao == "Multiplicação":
            st.success(f"{v1 * v2:.2f}")
        elif opcao == "Divisão":
            st.success(f"{v1 / v2:.2f}")
        else:
            st.error("Opção inválida.")
    except:
        st.error("Ocorreu um erro.")

