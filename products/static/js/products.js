$(document).ready(function() {
    $("#filter-select").on("change", function() {
        let $selected = $(this).find("option:selected");
        let filterInput = $selected.val();
        if (filterInput !== "reset") {
            let $target = $(".filter-menu").find(`.${filterInput}`);
            $(".filter-menu").find(".filter").not(`.${filterInput}`).each((i, el) => {
                $(el).hide();
            });
            $target.show();
        } else {
            $(".filter-menu").find("input").each((i, el) => $(el).val(""))
            $(".filter-menu").find(".filter").each((i, el) => {
                $(el).hide();
            });
        }

        if ($(".filter-menu").find(".filter:visible").length > 0) {
            $("#add-filter").closest(".row").show();
        } else {
            $("#add-filter").closest(".row").hide();
        }
    });

    $("#add-filter").on("click", function() {
        const currentUrl = new URL(window.location);
        let $selectedFilter = $("#filter-select").find("option:selected");
        let filterType = $selectedFilter.attr("name");
        let filterField = $selectedFilter.text();
        let $inputs = $(".filter-menu").find(`.${$selectedFilter.val()}`).find("input");

        if(filterType === "range") {
            let filterKey = `${filterField.toLowerCase()}__range`;
            currentUrl.searchParams.delete(filterKey);

            let rangeArr = [];
            $inputs.each((i, el) => currentUrl.searchParams.append(filterKey, $(el).val()));

            window.location.replace(currentUrl);
        }
    });

    $(".remove-filter").on("click", function() {
        const currentUrl = new URL(window.location);
        let filter = $(this).data("filter");
        
        currentUrl.searchParams.delete(filter);
        window.location.replace(currentUrl);
    });

    $(".edit-filter").on("click", function() {
        let type = $(this).data('type');
        let field = $(this).data('field');
        let value = $(this).data('value');

        
        if (type === "range") {
            let valueArr = value.split(",");
            $inputs = $(`.filter-${field}`).find("input");
            $inputs.each((i, el) => {
                $(el).val(valueArr[i]);
            });
        }
        
        $("#filter-select").find(`option[value="filter-${field}"]`).prop("selected", true);
        $("#filter-select").trigger("change");
    });
});