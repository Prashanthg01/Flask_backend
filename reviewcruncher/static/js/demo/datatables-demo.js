// Call the dataTables jQuery plugin
var table = $(document).ready(function() {
 $('#dataTable').dataTable({
     "bDestroy": true
});

});

$( "#filter" ).on( "change", function() {
  var e = document.getElementById("filter");
var value = e.options[e.selectedIndex].value;
var text = e.options[e.selectedIndex].text;
  initializeSlider(text);
});
// function initializeSlider(idx) {
//     var s = $(document).ready(function () {
//         $('#dataTable').DataTable({
//             "ajax": "http://127.0.0.1:8080/getdata_by_month",
//             "columns": [
//                 {"data": "sno"},
//                 {"data": "product_name"},
//                 {"data": "num_of_reviews"},
//                 {"data": "rating_avg"},
//                 {"data": "rating_total"}
//             ]
//         });
//     });
//
//     s.ajax.reload();
// }
function initializeSlider(idx) {
    $("#dataTable").dataTable().fnDestroy();

    var s1 = $(document).ready(function () {
        $('#dataTable').DataTable({
            "ajax": {
                'type': 'POST',
                'url': "/getdata_by_month",
                'data': {
                   filter_key: idx,
                },
            },
            "columns": [
           {"data": "sno"},
                {"data": "product_name"},
                {"data": "num_of_reviews"},
                {"data": "rating_avg"},
                {"data": "rating_total"}
            ]
        });
    });

    s1.ajax.reload();
}
