using PIM3_CRUD;
using System.Data;
using System.Data.SQLite;
using System.Drawing.Text;
using System.Runtime.InteropServices;


DataTable dt = new DataTable();
bool x = false;


while(x != true)
{
    string id = "12";
    string senha = "12";
    bool b = true;
    while (b != false)
    {
        Console.WriteLine("=============PIXFARM=============\n");
        Console.WriteLine("ID Funcionario: ");
        id = Console.ReadLine();
        if (id == "" && id.Length < 3)
        {
            Console.Clear();
            Console.WriteLine("\nALERTA!!");
            Console.WriteLine("\nALGO ESTA INCORRETO NO CAMPO DE ~'ID Funcionario'~ ");
        }else
        {
            b = false;
        }
    }

    bool c = true;
    while (c != false)
    {
        Console.WriteLine("\nSenha Funcionario: ");
        senha = Console.ReadLine();
        if (senha == "" || senha.Length < 3)
        {
            Console.WriteLine("\nALERTA!!");
            Console.WriteLine("\nALGO ESTA INCORRETO NO CAMPO DE ~'Senha Funcionario'~ ");
        }
        else
        {
            c = false;
        }
    }


    string sql = "SELECT * FROM funcionario WHERE id_funcionario='" + id + "' AND Senha='" + senha + "'";
    dt = Banco.Consulta(sql);
    if (dt.Rows.Count == 0)
    {
        Console.Clear();
        Console.WriteLine("!!LOGIN NÃO ENCONTRADO!!");
    }
    else
    {
        x = true;
    }
}





Console.Clear();
Console.WriteLine("=============PIXFARM=============");
Console.WriteLine("\nDIGITE o numero conrrespondente\nCom qual das opções a baixo você deseja acessar ?");
Console.WriteLine("\n1 - Vizualizar Funcionarios Cadastradados");
Console.WriteLine("\n2 - Cadastrar Novos funcionarios");
Console.WriteLine("\n3 - Atualizar dados de funcionario ");
Console.WriteLine("\n4 - Deletar cadastro de funcionarios ");
Console.WriteLine("\n0 - Sair do sistema ");
int rpt  = int.Parse(Console.ReadLine()); 

switch (rpt)
{
    case 0:
        break;


    case 1:
        Console.Clear();
        Banco.VizualizarBanco();
        break;


    case 2:
        Funcções.Cadastrar();
        break;


    case 3:
        Funcções.ShowAtualizarFuncionario();
        break;


    case 4:
        Funcções.ShowDeletarFuncionario();
        break;  

}


