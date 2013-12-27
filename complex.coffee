LiveJS = {}

class LiveJS.User
  name: null
  constructor: (@name)->
  getName: =>
    @name
  setName: (@name)=>

class LiveJS.fileExplorer
  noToggle: false
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
    if result is false
      @showCreateUser()
    @showSaveCall()
    
  showSaveCall: =>
    if @fileName is undefined
      @getFolder @user.getName()
    else
      @noToggle = true
      @saveFile()

  getFolder: (name)=>
    $.ajax
      url: "gears/getContents.php"
      method: "GET"
      data: {user: @user.getName()}
      success: (list) =>
        list = tmpl(template.get('files'), { files: list.split("{%}")})
        $("#filedialog").html list
        @toggle()

  toggle: =>
    $("#filedialog").fadeToggle();
    $("#mycan").fadeToggle();
    @events()
      
  showCreateUser: =>
    name = prompt "Enter a Name for yourSelf, you can access all your saved files from this name only"
    @user = new LiveJS.User name

  saveFile: (e)=>
      if @fileName is undefined
        @fileName = $("#namebar .saveas").val()
      $.ajax
        url: "gears/saveFile.php"
        method: "POST"
        data: {fileName: @fileName, str: editor.getValue(), user: @user.getName()}
        success: =>
          alert 'File Saved'
          if not @noToggle
            @toggle()

  events: =>
    $("#save-saveas").on("click", @saveFile)
    $(".saveas").keyup (e)=> 
        if e.type == "keyup" and e.keyCode == 13
          @saveFile(e);
