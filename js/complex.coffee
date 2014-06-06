window.Editor ||= {}

class Base
    constructor: ->
        @startUp()

class Editor.CommandBox extends Base

    element: "#menu"

    startUp: =>
        @render()

    render: (html)=>
        $(@element).html Editor.Templates.render "menu"


class Editor.Application extends Base

    startUp: =>
        new Editor.CommandBox