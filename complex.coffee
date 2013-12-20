LiveJS = {}

class LiveJS.User
  name: null
  constructor: (@name)->
  getName: =>
    @name
  setName: (@name)=>

class LiveJS.fileExplorer
  user: null
  fileName: undefined
  constructor: (@user)->
  userExists: =>
    if @user
      if @user.getName()
        return true
    false

  execute: =>
    result= @userExists()
    if result
      @showSaveCall()
    else
      @showCreateUser()
    
  showSaveCall: =>
    @getFolder @user.getName()

  getFolder: (name)=>
    $.ajax
      url: "gears/getContents.php"
      method: "GET"
      data: {user: @user.getName()}
      success: (list) =>
        list = tmpl(template.get('files'), { files: list})
        $("#filedialog").html list
        @toggle()

  toggle: =>
    $("#filedialog").fadeToggle();
    $("#mycan").fadeToggle();
    @events()
      
  showCreateUser: =>
    name = prompt "Enter a Name for yourSelf, you can access all your saved files from this name only"
    @user = new LiveJS.User name

  saveFile: ()=>
      if @fileName is undefined
        @fileName = $("#namebar .saveas").val()
      $.ajax
        url: "gears/saveFile.php"
        method: "POST"
        data: {fileName: @fileName, str: editor.getValue()}
        success: ->
          alert 'Saved Veere'

  events: =>
    $("#save-saveas").on("click", @saveFile)
