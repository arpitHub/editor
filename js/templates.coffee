window.Editor ||= {}

class templates

	render: (name, params={})=>
		k = @[name](params)

	menu: _.template '''
		<div id="command-box" onClick="this.contentEditable='true';">
		</div>
	'''

Editor.Templates = new templates