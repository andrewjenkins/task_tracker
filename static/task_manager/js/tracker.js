// items
$(function() {
    $(".list").sortable({
        revert: true,
        connectWith: '.list',
        update: function(event, ui) {
            var order_data = {
                "items": $(this).sortable('serialize'),
                "csrfmiddlewaretoken": csrf_token
            };

            // make sure we only send one group change request
            if (this !== ui.item.parent()[0]) {
                var group_data = {
                    "item_id": ui.item.attr('id').substr(5),
                    "group_id": ui.item.parent().attr('id').substr(5),
                    "csrfmiddlewaretoken": csrf_token
                };

                $.ajax({
                    data: group_data,
                    type: 'POST',
                    url: item_move_url
                });
            }

            $.ajax({
                data: order_data,
                type: 'POST',
                url: group_order_url
            });
        }
    });
    $(".item").disableSelection();
});

$(function() {
    $("a.delete_item").click(function(e) {
        e.preventDefault();
        $(this).parent().hide();

        var item_data = {
            "item_id": $(this).parent().attr('id').substr(5),
            "csrfmiddlewaretoken": csrf_token
        };

        $.ajax({
            data: item_data,
            type: 'POST',
            url: item_delete_url
        });
    });
});

// groups
$(function() {
    $("#content").sortable({
        items: '.group:not(.pin)',
        revert: true,
        update: function(event, ui) {
            var order_data = {
                "groups": $(this).sortable('serialize'),
                "csrfmiddlewaretoken": csrf_token
            };

            $.ajax({
                data: order_data,
                type: 'POST',
                url: board_order_url
            });
        }
    });
    $(".header").disableSelection();
});

$(function() {
    $("a.unlock_group").click(function(e) {
        e.preventDefault();
        if ($(this).children().hasClass('lock')) {
            $(this).parents('.content').find('a.delete_item').show();
            $(this).parents('.content').find('.ui.item.segment').css({
                'padding-right': '25px'
            });
            $(this).parent().find('.delete_group').show();
            $(this).children().removeClass('lock');
            $(this).children().addClass('unlock');
        } else {
            $(this).parents('.content').find('a.delete_item').hide();
            $(this).parents('.content').find('.ui.item.segment').css({
                'padding-right': '10px'
            });
            $(this).parent().find('.delete_group').hide();
            $(this).children().removeClass('unlock');
            $(this).children().addClass('lock');
        }
    });
});

$(function() {
    $("a.delete_group").click(function(e) {
        e.preventDefault();
        $(this).parents(".group").hide();

        var group_data = {
            "group_id": $(this).parents('.group').attr('id').substr(6),
            "csrfmiddlewaretoken": csrf_token
        };

        $.ajax({
            data: group_data,
            type: 'POST',
            url: group_delete_url
        });
    });
});