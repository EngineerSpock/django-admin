(function ($) {
    $(function () {
        function allowDrow(ev) {
            ev.preventDefault();
        }

        function drag(ev) {
            ev.originalEvent.dataTransfer.setData("text", ev.target.id);
            ev.originalEvent.dataTransfer.setData("content", ev.target.textContent);
            ev.originalEvent.dataTransfer.setData("form", ev.target.getElementsByTagName("form"));
        }

        function drop(ev, block) {
            ev.preventDefault();
            var task_id = ev.originalEvent.dataTransfer.getData("text"),
                task_pk = task_id.split('-')[1];
            $(block).append($('#' + task_id));
            updateTodoColumn(block, task_pk);
        }

        $('.dashboard__task-area').on('dragover', function(ev) {
            allowDrow(ev);
        });

        $('.dashboard__task-area').on('drop', function(ev) {
            drop(ev, this);
        });

        $('.dashboard__task-item').on('dragstart', function(ev) {
           drag(ev);
        });

        function updateTodoColumn(block, pk) {
            $('#todo-' + pk + ' input[name="dashboard_column"]').val(block.id.split('-')[1]);
            var form_data = $('#todo-' + pk).serialize();

            $.ajax({
                url: '/admin/kanban/todo/update/' + pk + '/',
                method: 'POST',
                data: form_data
            })
                .done(function (data) {
                    console.log(data);
                });
        }
    });
})(jQuery);