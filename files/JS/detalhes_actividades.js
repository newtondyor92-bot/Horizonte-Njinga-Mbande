
const dados = [
{
img:"files/imagens/outras/o enterro.jpg",
data:"🗓️ 17,18,19 de Abril de 2026",
titulo:"O ENTERRO",
desc:"A Hori – Njinga Mbande apresenta uma emocionante peça teatral que promete prender a tua atenção do início ao fim! O Enterro traz uma história forte, cheia de emoções, conflitos e reflexões sobre a vida e...",
link:"Ler mais"

},
{
img:"files/imagens/outras/segredo da cama",
data:"🗓️ 2,3,5 de Abril 2026",
titulo:"O SEGREDO DA CAMA",
desc:"A Horizonte – Njinga Mbande apresenta mais uma grande produção teatral que vai surpreender o público: “O Segredo da Cama”.Uma história envolvente cheia de mistério, emoções e reviravoltas, que explora relações humanas, escolhas da vida e consequências inesperada",
link:"Ler mais"
},
{
img:"files/imagens/outras/o enterro.jpg",
data:"🗓️ BREVEMENTE",
titulo:"BREVEMENTE: SITE OFICIAL DA HORIZONTE NJINGA MBANDE!",
desc:" 🌐Estamos a preparar algo grande para ti! Muito em breve, a Horizonte – Njinga Mbande vai lançar o seu site oficial, com um design moderno, elegante e totalmente intuitivo.",
link:"Ler mais"

},
{
img:"files/imagens/outras/o enterro.jpg",
data:"🗓️ 17,18,19 de Abril de 2026",
titulo:"O ENTERRO",
desc:"A Horizonte – Njinga Mbande apresenta uma emocionante peça teatral que promete prender a tua atenção do início ao fim! O Enterro traz uma história forte, cheia de emoções, conflitos e reflexões sobre a vida e...",
link:"Ler mais"
},
{
img:"files/imagens/outras/o enterro.jpg"",
data:"🗓️ 2,3,5 de Abril 2026",
titulo:"O SEGREDO DA CAMA",
desc:"A Horizonte – Njinga Mbande apresenta mais uma grande produção teatral que vai surpreender o público: “O Segredo da Cama”.Uma história envolvente cheia de mistério, emoções e reviravoltas, que explora relações humanas, escolhas da vida e consequências inesperada",
link:"Ler mais"


},
{
img:"files/imagens/outras/o enterro.jpg",
data:"🗓️ BREVEMENTE",
titulo:"BREVEMENTE: SITE OFICIAL DA HORIZONTE NJINGA MBANDE!",
desc:" 🌐Estamos a preparar algo grande para ti! Muito em breve, a Horizonte – Njinga Mbande vai lançar o seu site oficial, com um design moderno, elegante e totalmente intuitivo.",
link:"Ler mais"


},]


const params = new URLSearchParams(window.location.search);
const id = Number(params.get("id"));

const atividade = dados[id];
if(atividade){
  document.getElementById("titulo").innerText = atividade.titulo;
  document.getElementById("data").innerText = atividade.data;
document.getElementById("descricao").innerText = atividade.desc;
document.getElementById("imagem").src = atividade.img;
}

