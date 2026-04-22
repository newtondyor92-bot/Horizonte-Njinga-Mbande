$rootFiles = @("index.html")
$subFiles = @(
    "files/Html/eventos.html",
    "files/Html/galeria.html",
    "files/Html/cursos.html",
    "files/Html/sobre.html",
    "files/Html/contacto.html",
    "files/Html/actividades.html",
    "files/Html/detalhes_actividades.html"
)

foreach ($file in $rootFiles) {
    $content = Get-Content -Path $file -Raw
    if ($content -notmatch 'styles/responsive\.css') {
        $content = $content -replace '</head>', "    <link rel=`"stylesheet`" href=`"styles/responsive.css`">`r`n</head>"
        [System.IO.File]::WriteAllText((Resolve-Path $file), $content, [System.Text.UTF8Encoding]::new($false))
    }
}

foreach ($file in $subFiles) {
    $content = Get-Content -Path $file -Raw
    if ($content -notmatch '\.\./\.\./styles/responsive\.css') {
        $content = $content -replace '</head>', "    <link rel=`"stylesheet`" href=`"../../styles/responsive.css`">`r`n</head>"
        [System.IO.File]::WriteAllText((Resolve-Path $file), $content, [System.Text.UTF8Encoding]::new($false))
    }
}

Write-Host "Folha responsive.css ligada às páginas principais."
