$(document).ready(function() {
    $("select.update-cart").on("change", function() {
        $(this).closest("form").submit();
    })
});