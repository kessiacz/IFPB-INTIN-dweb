
function aluno_matricula(id){
    var aluno = document.getElementById('dados').aluno.value;
    var matricula = document.getElementById('dados').matricula.value;

    var _table = document.querySelector('table');
    
    var newRow = document.createElement('tr');
    newRow.insertCell(0).innerHTML = aluno;
    newRow.insertCell(1).innerHTML = matricula;

    var input_hidden = document.createElement('input');
    input_hidden.type = 'hidden';
    input_hidden.name = 'alunos';
    input_hidden.value = matricula;

    document.getElementById(id).appendChild(newRow);
    document.getElementById(id).appendChild(input_hidden);

    newRow.prepend(input_hidden);

    return false;
}

function printWindow(){
    var originalContents = document.body.innerHTML;
    var printReport= document.getElementById('form').innerHTML;
    var printReport2= document.getElementById('table_hw').innerHTML;
    document.body.innerHTML = printReport + printReport2;
    window.print();
    document.body.innerHTML = originalContents;
}

function alertCadastre(){
    alert("Cadastre-se")
}