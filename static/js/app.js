$(document).ready(function(){
    $(document).on('click', '.delete-task', function() {
        var id = $(this).attr('id');

        $.ajax({
            url: "/ajax/delete_task/",
            data: {
            'id' : id,
            },
            success: function(response){
               $(".task").html(response);
            }
        });
    });
});

$(document).ready(function(){
    $(document).on('click', '.finish-task', function() {
        var id = $(this).attr('id');

        $.ajax({
            url: "/ajax/finish_task/",
            data: {
            'id' : id,
            },
            success: function(response){
                $(".task").html(response);
            }
        });
    });
});

$(document).ready(function(){
    $(document).on('click', '.reopen-task',function() {
        var id = $(this).attr('id');

        $.ajax({
            url: "/ajax/reopen_task/",
            data: {
            'id' : id,
            },
            success: function(response){
                $(".task").html(response);
            }
        });
    });
});
