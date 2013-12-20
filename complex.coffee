LiveJS = {}

class LiveJS.User
  name: null
  constructor: (@name)->
  getName: =>
    @name
  setName: (@name)=>

class LiveJS.fileExplorer
  user: null
  constructor: (@user)->
  userExists: =>
    if @user
      if @user.getName()
        return true
    false

  execute: =>
    reult= @userExists()
    if reult
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
      
  showCreateUser: =>
    @user = new LiveJS.User "Ramu"
      