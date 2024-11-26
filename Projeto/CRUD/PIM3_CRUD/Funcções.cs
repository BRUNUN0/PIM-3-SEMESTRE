using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PIM3_CRUD
{
    internal class Funcções
    {

        public static void Cadastrar()
        {

            Funcionario funcionario = new Funcionario();
            Console.Clear();
            Console.WriteLine("=============PIXFARM=============");
            Console.WriteLine("CADASTRAR NOVO FUNCIONARIO:");
            bool x = false;
            while (x != true)
            {

                Console.WriteLine("Nome:");
                funcionario.nome = Console.ReadLine();
                if (funcionario.nome == "" || funcionario.nome.Length < 3)
                {
                    Console.WriteLine("Algo esta errado tente novamente\nLembre que deve ter no minimo 3 caracteres");
                }
                else
                {
                    
                    x = true;
                }
            }
            bool c = false;
            while (c != true)
            {

                Console.WriteLine("Cargo:");
                funcionario.cargo = Console.ReadLine();
                if (funcionario.cargo == "")
                {
                    Console.WriteLine("Algo esta errado tente novamente\nLembre que deve ter no minimo 3 caracteres");
                }
                else
                {
                    
                    c = true;
                }
            }
            bool v = false;
            while (v != true)
            {

                Console.WriteLine("CPF:");
                funcionario.cpf = Double.Parse(Console.ReadLine());
                if (funcionario.cpf < 3 && funcionario.cpf > 11)
                {
                    Console.WriteLine("Algo esta errado tente novamente\nLembre que deve ter no minimo 3 caracteres\ne o CPF tem no maximo 11 caracter");
                }
                else
                {
                    
                    v = true;
                }
            }
            bool b = false;
            while (b != true)
            {

                Console.WriteLine("Sexo[M/F]:");
                funcionario.sexo = Console.ReadLine();
                if (funcionario.sexo == "")
                {
                    Console.WriteLine("Algo esta errado tente novamente\nLembre que deve ter no minimo 3 caracteres");
                }
                else
                {
                    
                    b = true;
                }
            }
            bool n = false;
            while (n != true)
            {

                Console.WriteLine("Senha:");
                funcionario.senha = Console.ReadLine();
                if (funcionario.senha == "" || funcionario.senha.Length < 3)
                {
                    Console.WriteLine("Algo esta errado tente novamente\nLembre que deve ter no minimo 3 caracteres");
                }
                else
                {
                   
                    n = true;
                }
            }
            bool m = false;
            while (m != true)
            {

                Console.WriteLine("Nascimento:");
                funcionario.nascimento = Console.ReadLine();
                if (funcionario.nascimento == "" || funcionario.nascimento.Length < 3)
                {
                    Console.WriteLine("Algo esta errado tente novamente\nLembre que deve ter no minimo 3 caracteres");
                }
                else
                {
                    
                    m = true;
                }
            }
            bool l = false;
            while (l != true)
            {

                Console.WriteLine("E-mail:");
                funcionario.email = Console.ReadLine();
                if (funcionario.email == "" || funcionario.email.Length < 3)
                {
                    Console.WriteLine("Algo esta errado tente novamente\nLembre que deve ter no minimo 3 caracteres");
                }
                else
                {
                   
                    l = true;
                }
            }
            bool k = false;
            while (k != true)
            {

                Console.WriteLine("Setor:");
                funcionario.setor = Console.ReadLine();
                if (funcionario.setor == "")
                {
                    Console.WriteLine("Algo esta errado tente novamente\nLembre que deve ter no minimo 3 caracteres");
                }
                else
                {
                    
                    k = true;
                }
            }

            Banco.NovoFuncionario(funcionario);
         


        }



        public static void ShowAtualizarFuncionario()
        {
            Funcionario funcionario = new Funcionario();
            Console.Clear();
            Console.WriteLine("=============PIXFARM=============");
            Console.WriteLine("ATUALIZAR DADOS FUNCIONARIO:");


            bool q = false;
            while (q != true)
            {

                Console.WriteLine(" DIGITE O (ID FUNCIONARIO) QUE DESEJA ALTERAR DADOS:");
                funcionario.idfuncionario = int.Parse(Console.ReadLine());
                int id = funcionario.idfuncionario;
                if (Banco.Existeid(id))
                {
                    
                    q = true;
                }
                else
                {
                    Console.WriteLine("Algo esta errado tente novamente");

                }
            }
            bool x = false;
            while (x != true)
            {

                Console.WriteLine("Nome:");
                funcionario.nome = Console.ReadLine();
                if (funcionario.nome == "" || funcionario.nome.Length < 3)
                {
                    Console.WriteLine("Algo esta errado tente novamente\nLembre que deve ter no minimo 3 caracteres");
                }
                else
                {

                    x = true;
                }
            }
            bool c = false;
            while (c != true)
            {

                Console.WriteLine("Cargo:");
                funcionario.cargo = Console.ReadLine();
                if (funcionario.cargo == "")
                {
                    Console.WriteLine("Algo esta errado tente novamente\nLembre que deve ter no minimo 3 caracteres");
                }
                else
                {

                    c = true;
                }
            }
            bool v = false;
            while (v != true)
            {

                Console.WriteLine("CPF:");
                funcionario.cpf = Double.Parse(Console.ReadLine());
                if (funcionario.cpf < 3 && funcionario.cpf > 11)
                {
                    Console.WriteLine("Algo esta errado tente novamente\nLembre que deve ter no minimo 3 caracteres\ne o CPF tem no maximo 11 caracter");
                }
                else
                {

                    v = true;
                }
            }
            bool b = false;
            while (b != true)
            {

                Console.WriteLine("Sexo[M/F]:");
                funcionario.sexo = Console.ReadLine();
                if (funcionario.sexo == "")
                {
                    Console.WriteLine("Algo esta errado tente novamente\nLembre que deve ter no minimo 3 caracteres");
                }
                else
                {

                    b = true;
                }
            }
            bool n = false;
            while (n != true)
            {

                Console.WriteLine("Senha:");
                funcionario.senha = Console.ReadLine();
                if (funcionario.senha == "" || funcionario.senha.Length < 3)
                {
                    Console.WriteLine("Algo esta errado tente novamente\nLembre que deve ter no minimo 3 caracteres");
                }
                else
                {

                    n = true;
                }
            }
            bool m = false;
            while (m != true)
            {

                Console.WriteLine("Nascimento:");
                funcionario.nascimento = Console.ReadLine();
                if (funcionario.nascimento == "" || funcionario.nascimento.Length < 3)
                {
                    Console.WriteLine("Algo esta errado tente novamente\nLembre que deve ter no minimo 3 caracteres");
                }
                else
                {

                    m = true;
                }
            }
            bool l = false;
            while (l != true)
            {

                Console.WriteLine("E-mail:");
                funcionario.email = Console.ReadLine();
                if (funcionario.email == "" || funcionario.email.Length < 3)
                {
                    Console.WriteLine("Algo esta errado tente novamente\nLembre que deve ter no minimo 3 caracteres");
                }
                else
                {

                    l = true;
                }
            }
            bool k = false;
            while (k != true)
            {

                Console.WriteLine("Setor:");
                funcionario.setor = Console.ReadLine();
                if (funcionario.setor == "")
                {
                    Console.WriteLine("Algo esta errado tente novamente\nLembre que deve ter no minimo 3 caracteres");
                }
                else
                {

                    k = true;
                }
            }

            Banco.AtualizarFuncionario(funcionario);

        }
            
        public static void ShowDeletarFuncionario()
        {

            Console.Clear();
            bool v = false;
            while(v != true)
            {
                Console.WriteLine("Antes de deletar um funcionario do Banco de dados é necessario fazer uma averiguação se você tem nivel de acesso necesario\nDigite o seu ID para que possa ser feito a averiguação do nivel de acesso:\n");
                int checkID = int.Parse(Console.ReadLine());
                bool res = Banco.CheckSetor(checkID);
                if(res == false)
                {
                    Console.WriteLine("NIVEL DE ACESSO INVALIDO");
                }
                else
                {
                    Console.WriteLine("ID INSERIDO VALIDO");
                    v = true;
                }
            }


            Funcionario funcionario = new Funcionario();


            bool q = false;
            while (q != true)
            {

                Console.WriteLine(" DIGITE O (ID FUNCIONARIO) QUE DESEJA DELETAR DO BANCO DADOS:");
                funcionario.idfuncionario = int.Parse(Console.ReadLine());
                int id = funcionario.idfuncionario;
                if (Banco.DeletExisteid(id))
                {

                    q = true;
                }
                else
                {
                    Console.WriteLine("Algo esta errado tente novamente");

                }
            }

        }
    }
}
