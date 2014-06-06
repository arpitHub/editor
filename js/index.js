
init = function() {
    __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };
    window.editor = undefined;
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/twilight");
    editor.getSession().setMode("ace/mode/javascript");
    editor.commands.addCommand({
            name: 'execute',
            bindKey: {win: 'Ctrl-Enter',  mac: 'Command-Enter'},
            exec: function(editor) {
                eval(editor.getValue());
            },
            readOnly: true
    });
    editor.commands.addCommand({
            name: 'save',
            bindKey: {win: 'Ctrl-S',  mac: 'Alt-S'},
            exec: function(editor) {
                console.log("hello");
                fileExplorer.execute()
            },
            readOnly: true
    });
    new Editor.Application;
}

$(document).ready(init);