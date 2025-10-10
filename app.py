import streamlit as st
from crud import inserir_aluno,listar_aluno,atualizar_idade,deletar_aluno
# python -m pip install streamlit

#Rodar o streamlit

st.set_page_config(page_title="Gerenciamento de alunos", page_icon="👨‍🎓")

st.title("Sistema de alunos com MYSQL")

menu = st.sidebar.radio("Menu : ", ["Adicionar aluno", "Listar aluno","Atualizar idade", "Deletar aluno"])

if menu == "Adicionar aluno":
    st.subheader("➕Inserir aluno")
    nome = st.text_input("Nome: ",placeholder="Digite seu nome")
    idade = st.number_input("Idade", min_value=8, step=1 )
    if st.button("Cadastrar"):
        if nome.strip() != "":
            inserir_aluno(nome,idade)
            st.success(f"Aluno{nome} cadastrado com sucesso")
        else:
            st.warning("O campo nome não pode ser vazio!.")
        
elif menu == "Listar aluno":
    st.subheader("Lista de alunos cadastrados.")
    alunos = listar_aluno()
    if alunos:
        st.dataframe(alunos)

    else:
        st.info("Nenhum aluno cadastrado")
elif menu == "Atualizar idade":
    st.subheader("Atulizar idade")
    alunos = listar_aluno()
    if alunos:
        id_aluno = st.selectbox("Escolha o id do aluno",[linha[0]for linha in alunos])
        nova_idade = st.number_input("Nova idade",min_value=8, step=1)
        if st.button("Salvar"):
            atualizar_idade(id_aluno,nova_idade)
            st.success("Idade atualizada com sucesso!")

        else:
            st.info("Nenhum aluno para atualizar")
        
elif menu == "Deletar aluno":
    st.subheader("❌ Deletar aluno")
    alunos = listar_aluno()
    if alunos:
        id_aluno = st.selectbox("Escolha o ID do aluno que deseja deletar", [linha[0] for linha in alunos])
        if st.button("Deletar"):
            deletar_aluno(id_aluno)
            st.success(f"Aluno com ID {id_aluno} deletado com sucesso.")
    else:
        st.info("Nenhum aluno para deletar.")