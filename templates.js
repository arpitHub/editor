window.template = {}
window.template.list = []

window.template.get = function(name) {
    return window.template.list[name].join('\n');
}

template.list["files"] = [
    "<div id='namebar'>",
        "<input class='saveas' />",
        "<div id='save-saveas'><a href='#'>Save</a></div>",
    "</div>",
    "<div id='dir-list'>",
        "<ul>",
            "{% for (var i=0; i < 16; i++) { %}",
            "<li class=\"choices\" title='mehh'>",
                "<span style='float:right; color: lavender; background: black'><i>Folder {%= i %}</i></span>",
            "</li>",
            "{% } %}",
        "</ul>",
    "</div>"
];
