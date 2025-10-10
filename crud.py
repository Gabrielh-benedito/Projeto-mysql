from conexao import conectar


def inserir_aluno(nome_aluno, idade_aluno):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO aluno (nome,idade) VALUES (%s , %s)",
                (nome_aluno, idade_aluno)
            )
            conexao.commit()
        except Exception as erro :
            print(f"Erro ao tentar inserir aluno: {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_aluno():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM aluno ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro a listar os alunos: {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()


def atualizar_idade(id_aluno,nova_idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE aluno SET idade = %s WHERE id = %s",
                (nova_idade, id_aluno)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar aluno: {erro}")
        finally:
            cursor.close()
            conexao.close()



