using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.Data.SQLite;
using System.Security.Cryptography;
using System.Data.SqlClient;



namespace PIM3_CRUD
{
    class Banco
    {
        private static SQLiteConnection? conexao;
        
        private static SQLiteConnection ConexaoBanco()
        {

            conexao = new SQLiteConnection("Data Source=Banco\\pimcrud;Version=3;") ;
            conexao.Open();
            return conexao;
        }

        public static DataTable ObterTodosFuncionarios()
        {
            SQLiteDataAdapter da = null;
            DataTable dt = new DataTable();
             
            try
            {
                using (var cmd = ConexaoBanco().CreateCommand()) {

                    cmd.CommandText = "SELECT * FROM funcionario";
                    da = new SQLiteDataAdapter(cmd.CommandText, ConexaoBanco());
                    da.Fill(dt);
                    ConexaoBanco().Close();
                    return dt;
                }

            }catch (Exception)
            {
                throw;
            }

        }

        public static DataTable Consulta(string sql)
        {
            SQLiteDataAdapter da = null;
            DataTable dt = new DataTable();

            try
            {
                using (var cmd = ConexaoBanco().CreateCommand())
                {

                    cmd.CommandText = sql;
                    da = new SQLiteDataAdapter(cmd.CommandText, ConexaoBanco());
                    da.Fill(dt);
                    ConexaoBanco().Close();
                    return dt;
                }

            }
            catch (Exception)
            {
                throw;
            }

        }

        public static void NovoFuncionario(Funcionario u)
        {

            if (ExisteFunc(u))
            {
                Console.WriteLine("Funcionario ja existe no banco de dados");
                return;

            }
            try
            {
                DateTime thisDay = DateTime.Today;
                var cmd = ConexaoBanco().CreateCommand();
                cmd.CommandText = "INSERT INTO funcionario (Nome, Cargo, CPF, Sexo, Senha, Nascimento, Email, Setor, Dat_Inicio) VALUES (@nome, @cargo, @cpf, @sexo, @senha, @nascimento, @email, @setor, @dat_inicio)";

                cmd.Parameters.AddWithValue("@nome", u.nome);
                cmd.Parameters.AddWithValue("@cargo", u.cargo);
                cmd.Parameters.AddWithValue("@cpf", u.cpf);
                cmd.Parameters.AddWithValue("@sexo", u.sexo);
                cmd.Parameters.AddWithValue("@senha", u.senha);
                cmd.Parameters.AddWithValue("@nascimento", u.nascimento);
                cmd.Parameters.AddWithValue("@email", u.email);
                cmd.Parameters.AddWithValue("@setor", u.setor);
                cmd.Parameters.AddWithValue("@dat_inicio", thisDay.ToString());
                cmd.ExecuteNonQuery();
                Console.WriteLine("Novo funcionario cadastrado com sucesso");


                ConexaoBanco().Close();


            }
            catch (Exception ex)
            {
                Console.WriteLine("Erro ao gravar novo funcionario");
                Console.WriteLine(ex.Message);
            }
        }

        public static bool ExisteFunc(Funcionario f)
        {
            bool res;
            SQLiteDataAdapter da = null;
            DataTable dt = new DataTable(); 

            var cmd = ConexaoBanco().CreateCommand();
            cmd.CommandText = "SELECT cpf FROM funcionario WHERE cpf='" + f.cpf + "'";
            da = new SQLiteDataAdapter(cmd.CommandText, ConexaoBanco());
            da.Fill(dt);
            if(dt.Rows.Count > 0)
            {
                res = true;
            }
            else
            {
                res = false;
            }


            return res;

        }


        public static void AtualizarFuncionario(Funcionario f)
        {

            SQLiteDataAdapter da = null;
            DataTable dt = new DataTable();
            try
            {
                var vcon = ConexaoBanco();
                var cmd = vcon.CreateCommand();
                cmd.CommandText = "UPDATE funcionario SET Nome='" + f.nome + "',Cargo='" + f.cargo + "', Sexo='" + f.sexo + "', Senha='" + f.senha + "', Email='" + f.email + "', Nascimento='" + f.nascimento + "' WHERE id_funcionario=" + f.idfuncionario;
                da = new SQLiteDataAdapter(cmd.CommandText, vcon);
                cmd.ExecuteNonQuery();
                 vcon.Close();
   


            }catch (Exception)
            {
                throw;
            }

        }

        public static bool CheckSetor(int id)
        {
            bool res;
            var conn = ConexaoBanco();
            var cmd = conn.CreateCommand();
            cmd.CommandText = "SELECT Setor FROM Funcionario WHERE id_funcionario = @id";
            cmd.Parameters.AddWithValue("@id", id);

            var setor = cmd.ExecuteScalar()?.ToString();

            conn.Close();

            if (setor == "RH")
            {
                res = true;
            }
            else
            {
                res = false;
                Console.WriteLine("ID INSERIDO INVALIDO");
            }

            return res;

        }


        public static bool Existeid(int id)
        {
            bool res;
            SQLiteDataAdapter da = null;
            DataTable dt = new DataTable();

            var cmd = ConexaoBanco().CreateCommand();
            cmd.CommandText = "SELECT id_funcionario FROM funcionario WHERE id_funcionario='" + id + "'";
            da = new SQLiteDataAdapter(cmd.CommandText, ConexaoBanco());
            da.Fill(dt);
            if (dt.Rows.Count > 0)
            {
                Console.WriteLine(id);
                res = true; //existe 
                
            }
            else
            {
                Console.WriteLine(id);
                res = false;// Não existe
            }


            return res; 

        }


         
        public static bool DeletExisteid(int id)
        {
            bool res;
            SQLiteDataAdapter da = null;
            DataTable dt = new DataTable();

            var cmd = ConexaoBanco().CreateCommand();
            cmd.CommandText = "SELECT id_funcionario FROM funcionario WHERE id_funcionario='" + id + "'";
            da = new SQLiteDataAdapter(cmd.CommandText, ConexaoBanco());
            da.Fill(dt);
            if (dt.Rows.Count > 0)
            {
                
                res = true; //existe 
                Banco.DeletFunc(id);

            }
            else
            {
                Console.WriteLine("USUARIO INEXISTENTE!");
                res = false;// Não existe
            }


            return res;

        }


        static void DeletFunc(int id)
        {

            var conn = ConexaoBanco();
            var cmd = conn.CreateCommand();
            cmd.CommandText = "DELETE FROM Funcionario WHERE id_funcionario = @id";
            cmd.Parameters.AddWithValue("@id", id);

            cmd.ExecuteNonQuery();
            Console.WriteLine("Funcionário deletado com sucesso.");

            conn.Close();

           
        }


        public static void VizualizarBanco()
        {

            var conn = ConexaoBanco();
            var cmd = conn.CreateCommand();
            cmd.CommandText = "SELECT * FROM Funcionario";

            var reader = cmd.ExecuteReader();

            Console.WriteLine("id_funcionario  |  Nome  |  Cargo  |  CPF  |  Sexo  |  Senha  |  Nascimento  |  Email  |  Setor     Dat_Inicio\n \n");

            
            while (reader.Read())
            {
                Console.WriteLine($"{reader["id_funcionario"]}  |  " +
                                  $"{reader["Nome"]}  |  " +
                                  $"{reader["Cargo"]}  |  " +
                                  $"{reader["CPF"]}  |  " +
                                  $"{reader["Sexo"]}  |  " +
                                  $"{reader["Nascimento"]}  |  " +
                                  $"{reader["Email"]}  |  " +
                                  $"{reader["Setor"]}  |  " +
                                  $"{reader["Dat_Inicio"]}\n");
            }

            reader.Close();
            conn.Close();
        }

    }

    
}
