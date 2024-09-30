function Get-HiddenFiles {
    <#
    .SYNOPSIS
    Lista de archivos ocultos en una ruta específica.

    .DESCRIPTION
    Este cmdlet permite listar todos los archivos ocultos en una carpeta determinada, proporcionando la ruta completa de cada archivo.

    .PARAMETER Path
    La ruta de la carpeta donde se buscarán los archivos ocultos.

    .EXAMPLE
    Get-HiddenFiles -Path "C:\Users\Raul\Documents"
    
    .NOTES
    Archivo de módulo: hiddenfiles.psm1
    #>
    
    param (
        [string]$Path = 'C:/Windows'
    )
    if (Test-Path -Path $Path) {
        Get-ChildItem -Path $Path -File -Hidden | ForEach-Object {
            $_.FullName
        }
    } else {
        Write-Host "La ruta especificada no existe." -ForegroundColor Red
    }
}
Export-ModuleMember -Function Get-HiddenFiles
