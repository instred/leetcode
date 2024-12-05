if (Test-Path .\.venv\Scripts\activate) {
    . .\.venv\Scripts\activate
    Write-Host "Venv started successfully"
} else {
    Write-Host "Error starting Venv"
}