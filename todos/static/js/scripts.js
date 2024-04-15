$(document).ready(function(){

    var deleteBtn = $('.delete-btn');

    $(deleteBtn).on('click', function(e){

        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar esta tarefa?');

        if(result) {
            window.location.href = delLink;
        }

    })


})