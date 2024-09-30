#!/bin/bash
set -e 

errors() {
    echo "Error en el comando: '$1' con código de salida $2"
    exit $2
}

view_ports() {
    echo "Mostrando puertos abiertos y conexiones activas..."
    if ! netstat -tuln; then
        errors "netstat -tuln" $?
    fi
}

check_process() {
    echo "Revisando procesos sospechosos..."
    if ! ps aux --sort=-%cpu | head -n 10; then
        errors "ps aux --sort=-%cpu" $?
    fi
}

generate_report() {
    echo "Generando reporte de puertos y procesos..."
    {
        echo "### Reporte de Puertos Abiertos ###"
        netstat -tuln
        echo
        echo "### Procesos que más consumen CPU ###"
        ps aux --sort=-%cpu | head -n 10
    } > system_report.txt

    echo "Reporte generado en 'reporte_sistema.txt'"
}