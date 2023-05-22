$(document).ready(function () {
    $('ul.navbar-nav > li').click(function (e) {
        $('ul.navbar-nav > li').removeClass('active');
        $(this).addClass('active');
    });
    var table = $('#example1').DataTable({
        "lengthMenu": [5, 10, 50, 100],
        "pageLength": 50,
        "scrollX": true,
        dom: 'Bfrtip',
        buttons: [{
            extend: 'excelHtml5',
            text: 'Export All',
            exportOptions: {
                columns: ':visible:not(.not-exported)'
            },
            title: 'Data export'
        }, {
            extend: 'excelHtml5',
            text: 'Export selected',
            exportOptions: {
                columns: ':visible:not(.not-exported)',
                modifier: {
                    selected: true
                }
            },
            title: 'Data export'
        }
        ],
        select: {
            style: "multi"
        }
    });
});