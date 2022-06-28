export interface Todo {
    id?: String,
    nomeDoCliente: String,
    descricaoDoProduto?: String,
    codigoDaPeca?: Number,
    numeroDoPedido?: Number,
    status?: String,
    responsavel?:String,
    ordemDeProducao?: String,
    dataParaFinalizar: any,
    finalizado: Boolean
}