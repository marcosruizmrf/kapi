const spawn = require('child_process').spawn;

const process = spawn('python', ['C:/temp/PGF/univesp-pi-front/src/app/components/finalizados/requisicoes.py']);

process.stdout.on('data', data => {
    console.log(data.toString());
})