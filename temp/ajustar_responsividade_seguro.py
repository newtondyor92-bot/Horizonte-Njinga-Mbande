from pathlib import Path
import re

FILES = [
    Path("index.html"),
    Path("files/Html/eventos.html"),
    Path("files/Html/galeria.html"),
    Path("files/Html/cursos.html"),
    Path("files/Html/sobre.html"),
    Path("files/Html/contacto.html"),
    Path("files/Html/actividades.html"),
    Path("files/Html/detalhes_actividades.html"),
]

ROOT_LINK = '<link rel="stylesheet" href="styles/responsive.css">'
SUB_LINK = '<link rel="stylesheet" href="../../styles/responsive.css">'

def fix_mojibake(text: str) -> str:
    try:
        repaired = text.encode("cp1252", errors="replace").decode("utf-8", errors="replace")
        return repaired
    except Exception:
        return text

def ensure_link(text: str, link: str) -> str:
    if link not in text:
        text = text.replace("</head>", f"    {link}\n</head>")
    return text

def fix_common_html(text: str, is_root: bool) -> str:
    text = text.replace('<html lang="en">', '<html lang="pt">')
    text = text.replace(">PÃ¡gina Inicial<", ">Página Inicial<")
    text = text.replace("PÃ¡gina Inicial", "Página Inicial")
    text = text.replace("AtuaÃ§Ã£o", "Atuação")
    text = text.replace("InscriÃ§Ã£o", "Inscrição")
    text = text.replace("danÃ§a", "dança")
    text = text.replace("produÃ§Ã£o", "produção")
    text = text.replace("artÃ­sticas", "artísticas")
    text = text.replace("atuaÃ§Ã£o", "atuação")
    text = text.replace("tÃ©cnicas", "técnicas")
    text = text.replace("interpretaÃ§Ã£o", "interpretação")
    text = text.replace("expressÃ£o", "expressão")
    text = text.replace("improvisaÃ§Ã£o", "improvisação")
    text = text.replace("DuraÃ§Ã£o", "Duração")
    text = text.replace("NÃ­vel", "Nível")
    text = text.replace("presenÃ§a", "presença")
    text = text.replace("ProduÃ§Ã£o", "Produção")
    text = text.replace("iluminaÃ§Ã£o", "iluminação")
    text = text.replace("direÃ§Ã£o", "direção")
    text = text.replace("espetÃ¡culos", "espetáculos")
    text = text.replace("AvanÃ§ado", "Avançado")
    text = text.replace("histÃ³rias", "histórias")
    text = text.replace("FormulÃ¡rio", "Formulário")
    text = text.replace("Ã  esquerda", "à esquerda")
    text = text.replace("serÃ¡", "será")
    text = text.replace("GÃªnero", "Gênero")
    text = text.replace("EndereÃ§o", "Endereço")
    text = text.replace("TelefÃ´nico", "Telefônico")
    text = text.replace("NÃºmero", "Número")
    text = text.replace("inscriÃ§Ã£o", "inscrição")
    text = text.replace("Links rÃ¡pidos", "Links rápidos")
    text = text.replace("Â©", "©")
    text = text.replace("ConteÃºdo", "Conteúdo")
    text = text.replace("NotÃ­cias", "Notícias")
    text = text.replace("MÃºsica", "Música")
    text = text.replace("ExposiÃ§Ã£o", "Exposição")
    text = text.replace("ContemporÃ¢nea", "Contemporânea")
    text = text.replace("CelebraÃ§Ã£o", "Celebração")
    text = text.replace("GrÃ¡tis", "Grátis")
    text = text.replace("DanÃ§a", "Dança")
    text = text.replace("ApresentaÃ§Ã£o", "Apresentação")
    text = text.replace("HistÃ³ria", "História")
    text = text.replace("DiscussÃ£o", "Discussão")
    text = text.replace("sessÃ£o", "sessão")
    text = text.replace("ProjeÃ§Ãµes", "Projeções")
    text = text.replace("documentÃ¡rios", "documentários")
    text = text.replace("descriÃ§Ãµes", "descrições")
    text = text.replace("prÃ¡ticas", "práticas")
    text = text.replace("artÃ­sticas", "artísticas")
    text = text.replace("ApresentaÃ§Ã£o Cultural", "Apresentação Cultural")
    text = text.replace("mÃºsica", "música")
    text = text.replace("tÃ­picos", "típicos")
    text = text.replace("CerimÃ´nia", "Cerimónia")
    text = text.replace("MemÃ³ria", "Memória")
    text = text.replace("tradiÃ§Ãµes", "tradições")
    text = text.replace("memÃ³rias", "memórias")
    text = text.replace("artÃ­sticos", "artísticos")
    text = text.replace("patrimÃ³nio", "património")
    text = text.replace("Sobre NÃ³s", "Sobre Nós")
    text = text.replace("Ã©", "é")
    text = text.replace("Ã ", "à")
    text = text.replace("missÃ£o", "missão")
    text = text.replace("atravÃ©s", "através")
    text = text.replace("exposiÃ§Ãµes", "exposições")
    text = text.replace("heranÃ§a", "herança")
    text = text.replace("geraÃ§Ãµes", "gerações")
    text = text.replace("inovaÃ§Ã£o", "inovação")
    text = text.replace("territÃ³rio", "território")
    text = text.replace("instituiÃ§Ãµes", "instituições")
    text = text.replace("experiÃªncias", "experiências")
    text = text.replace("VisÃ£o", "Visão")
    text = text.replace("referÃªncia", "referência")
    text = text.replace("promoÃ§Ã£o", "promoção")
    text = text.replace("excelÃªncia", "excelência")
    text = text.replace("contribuiÃ§Ã£o", "contribuição")
    text = text.replace("sustentÃ¡vel", "sustentável")
    text = text.replace("entretÃªm", "entretêm")
    text = text.replace("contemporÃ¢nea", "contemporânea")
    text = text.replace("InclusÃ£o", "Inclusão")
    text = text.replace("InovaÃ§Ã£o", "Inovação")
    text = text.replace("experiÃªncia", "experiência")
    text = text.replace("Sustentabilidade", "Sustentabilidade")
    text = text.replace("prÃ¡ticas", "práticas")
    text = text.replace("patrimÃ´nio", "património")
    text = text.replace("conexÃµes", "conexões")
    text = text.replace("PortfÃ³lio", "Portfólio")
    text = text.replace("realizaÃ§Ãµes", "realizações")
    text = text.replace("estÃ£o", "estão")
    text = text.replace("Festivais Culturais", "Festivais Culturais")
    text = text.replace("ExposiÃ§Ãµes de Arte", "Exposições de Arte")
    text = text.replace("emergentes", "emergentes")
    text = text.replace("tÃ©cnicas", "técnicas")
    text = text.replace("PublicaÃ§Ãµes", "Publicações")
    text = text.replace("histÃ³ria", "história")
    text = text.replace("disponÃ­veis", "disponíveis")
    text = text.replace("bibliotecas pÃºblicas", "bibliotecas públicas")
    text = text.replace("organizaÃ§Ãµes", "organizações")
    text = text.replace("exposiÃ§Ãµes estrangeiras", "exposições estrangeiras")
    text = text.replace("Projetos ComunitÃ¡rios", "Projetos Comunitários")
    text = text.replace("sessÃµes", "sessões")
    text = text.replace("contaÃ§Ã£o", "contação")
    text = text.replace("histÃ³rias", "histórias")
    text = text.replace("equipe Ã©", "equipe é")
    text = text.replace("acessÃ­vel", "acessível")
    text = text.replace("informaÃ§Ãµes", "informações")
    text = text.replace("pÃ¡gina", "página")
    text = text.replace("â¬…", "⬅")
    text = text.replace("Voltar Ã s Atividades", "Voltar às Atividades")
    text = text.replace("FormaÃ§Ã£o ArtÃ­stica", "Formação Artística")
    text = text.replace("ðŸ—“ï¸", "🗓️")
    text = text.replace("ðŸŒ", "🌐")
    text = text.replace("â€“", "–")
    text = text.replace("â€œ", "“")
    text = text.replace("â€", "”")

    if not is_root:
        text = text.replace('<a href="files/index.html" class="back">⬅ Voltar</a>', '<a href="../../index.html" class="back">⬅ Voltar</a>')

    return text

def fix_broken_media_queries(text: str, page_name: str) -> str:
    replacements = {
        "cursos.html": '@media(max-width:640px){header{flex-wrap:wrap;gap:15px}header nav ul{flex-wrap:wrap;gap:12px}.course-card{padding:18px}.course-form-panel{padding:22px}}',
        "eventos.html": '@media(max-width:640px){header{flex-wrap:wrap;gap:15px}header nav ul{flex-wrap:wrap;gap:12px}.events-page{margin:20px auto}}',
        "galeria.html": '@media(max-width:640px){header{flex-wrap:wrap;gap:15px}header nav ul{flex-wrap:wrap;gap:12px}.gallery-page{margin:20px auto}}',
        "contacto.html": '@media(max-width:640px){header{flex-wrap:wrap;gap:15px}header nav ul{flex-wrap:wrap;gap:12px}}',
    }

    if page_name in replacements:
        text = re.sub(
            r'@media\(max-width:640px\)\{.*?\}',
            replacements[page_name],
            text,
            count=1,
            flags=re.S
        )

    return text

for file_path in FILES:
    is_root = file_path.name == "index.html"
    text = file_path.read_text(encoding="utf-8")
    text = fix_mojibake(text)
    text = fix_common_html(text, is_root=is_root)
    text = fix_broken_media_queries(text, file_path.name)
    text = ensure_link(text, ROOT_LINK if is_root else SUB_LINK)
    file_path.write_text(text, encoding="utf-8")

print("Responsividade preservada e textos corrigidos em UTF-8.")
