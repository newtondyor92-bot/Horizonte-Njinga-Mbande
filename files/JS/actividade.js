const dados = [
{
img:"imagens/outras/o enterro.jpg",
data:"🗓️ 17,18,19 de Abril de 2026",
titulo:"O ENTERRO",
desc:"A Horizonte – Njinga Mbande apresenta uma emocionante peça teatral que promete prender a tua atenção do início ao fim! O Enterro traz uma história forte, cheia de emoções, conflitos e reflexões sobre a vida e...",
link:"Ler mais"
},
{
img:"imagens/outras/o enterro.jpg",
data:"🗓️ 2,3,5 de Abril 2026",
titulo:"O SEGREDO DA CAMA",
desc:"A Horizonte – Njinga Mbande apresenta mais uma grande produção teatral que vai surpreender o público: “O Segredo da Cama”.Uma história envolvente cheia de mistério, emoções e reviravoltas, que explora relações humanas, escolhas da vida e consequências inesperada",
link:"Ler mais"
},
{
img:"imagens/outras/o enterro.jpg",
data:"🗓️ BREVEMENTE",
titulo:"BREVEMENTE: SITE OFICIAL DA HORIZONTE NJINGA MBANDE!",
desc:" 🌐Estamos as preparar algo grande para ti! Muito em breve, a Horizonte – Njinga Mbande vai lançar o seu site oficial, com um design moderno, elegante e totalmente intuitivo.",
link:"Ler mais"

},
{
img:"imagens/outras/o enterro.jpg",
data:"🗓️ 17,18,19 de Abril de 2026",
titulo:"O ENTERRO",
desc:"A Horizonte – Njinga Mbande apresenta uma emocionante peça teatral que promete prender a tua atenção do início ao fim! O Enterro traz uma história forte, cheia de emoções, conflitos e reflexões sobre a vida e...",
link:"Ler mais"
},
{
img:"imagens/outras/o enterro.jpg",
data:"🗓️ 2,3,5 de Abril 2026",
titulo:"O SEGREDO DA CAMA",
desc:"A Horizonte – Njinga Mbande apresenta mais uma grande produção teatral que vai surpreender o público: “O Segredo da Cama”.Uma história envolvente cheia de mistério, emoções e reviravoltas, que explora relações humanas, escolhas da vida e consequências inesperada",
link:"Ler mais"

},
{
img:"imagens/outras/o enterro.jpg",
data:"🗓️ BREVEMENTE",
titulo:"BREVEMENTE: SITE OFICIAL DA HORIZONTE NJINGA MBANDE!",
desc:" 🌐Estamos a preparar algo grande para ti! Muito em breve, a Horizonte – Njinga Mbande vai lançar o seu site oficial, com um design moderno, elegante e totalmente intuitivo.",
link:"Ler mais"

},]
const container = document.getElementById('cards')
dados.forEach((item,index)=>{
const card = document.createElement('div')
card.classList.add('card')
card.innerHTML = `
<img src="${item.img}" alt="">
<div class="card-content">
<div class="date">${item.data}</div>
<div class="card-title">${item.titulo}</div>
<div class="card-desc"><strong>${item.desc}</strong></div>

<a href="files/Html/detalhes_actividades.html?id=${index}" class="link">
  ${item.link}
</a>

</div>
`
container.appendChild(card)
});
