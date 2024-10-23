$exclude = @("venv", "Automacao_pagamento.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Automacao_pagamento.zip" -Force