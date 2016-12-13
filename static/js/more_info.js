$(document).ready(function(){
    $('#dialog').dialog({
    autoOpen: false,
    modal: true,
    dialogClass: 'bulk_dialog',
    buttons: {
        "Volver": function() {
            $(this).dialog('close');
        }
    }
    });
    $("div.bulk_dialog div button:nth-child(1)").addClass("confirm");
    $("div.bulk_dialog div button:nth-child(2)").addClass("go_back");

    $(".clickable").on('click', function(){
        $(".description").html($(this).parent().parent().attr('data-description'));
        $(".code").html($(this).parent().parent().attr('data-code'));
        $(".pvp").html($(this).parent().parent().attr('data-pvp'));
        $(".dc2").html($(this).parent().parent().attr('data-discount-l2'));
        $(".net2").html($(this).parent().parent().attr('data-net-l2'));
        $(".dc4").html($(this).parent().parent().attr('data-discount-l4'));
        $(".net4").html($(this).parent().parent().attr('data-net-l4'));
        $(".of1").html($(this).parent().parent().attr('data-offer1'));
        $(".net1").html($(this).parent().parent().attr('data-net1'));
        $(".of2").html($(this).parent().parent().attr('data-offer2'));
        $(".net2").html($(this).parent().parent().attr('data-net2'));
        $(".of3").html($(this).parent().parent().attr('data-offer3'));
        $(".net3").html($(this).parent().parent().attr('data-net3'));
        $('#dialog').dialog('open');

    })
});
