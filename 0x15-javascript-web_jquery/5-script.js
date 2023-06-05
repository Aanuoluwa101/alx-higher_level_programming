#!/usr/bin/node
$('div#add_item').on('click', () => $('ul.my_list').append($('<li></li>').text('Item')));
