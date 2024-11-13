class Funcionario:   
    def __init__(self, id_funcionario, nome, cpf, sexo, fk_id_cargo, senha, nascimento, email, setor, fk_data_inicio):
        self.id = id_funcionario
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.fk_id_cargo = fk_id_cargo
        self.senha = senha
        self.nascimento = nascimento
        self.email = email
        self.setor = setor
        self.fk_data_inicio = fk_data_inicio

    def __str__(self):
        return f"Funcionário: {self.nome}, ID: {self.id_funcionario}"
    