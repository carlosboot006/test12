function abrirPastaDownload() {
    var request = new XMLHttpRequest();
    request.open('GET', '/abrir_pasta_download', true);
    request.send();
}
