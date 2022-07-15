$(document).ready(function () {
    $('#example').DataTable({
        ajax: 'data/data_table.json',
        deferRender: true,
        columns: [{
                data: 'man_full_sig',
                render: function (data, type, row) {
                    if (type === 'display') {
                        let link = row.man_website_url;
                        return '<a href="' + link + '">' + data + '</a>';
                    }

                    return data;
                },
            },
            {
                data: 'man_title',
                render: function (data, type, row) {
                    if (type === 'display') {
                        let hash_id = row.man_id;
                        return data + '<br />' + '<small>' + '<a href="https://www.freud-edition.net/jsonapi/node/manifestation/' + hash_id + '" target="_blank">' + hash_id + '</a>' + '</small>';
                    }
                    return data;
                },
            },
            {
                data: 'man_field_status_umschrift'
            },
            {
                data: 'man_pages'
            },
            {
                data: 'man_chapters'
            },
            {
                data: 'work_title',
                render: function (data, type, row) {
                    if (type === 'display') {
                        let link = row.werk_website_url;
                        let hash_id = row.work_id;
                        return '<a href="' + link + '" target="_blank">' + data + '</a><br /><small>' + '<a href="https://www.freud-edition.net/jsonapi/node/werk/' + hash_id + '" target="_blank">' + hash_id + '</a>' + '</small>';
                    }

                    return data;
                },
            },
            {
                data: 'work_status'
            },
            {
                data: 'file'
            },
            {
                data: 'tei'
            },
        ],
        dom: 'PfrtipB',
        searchPanes: {
            initCollapsed: true
        },
        buttons: [
            'copy', 'excel', 'pdf'
        ]
    });
});