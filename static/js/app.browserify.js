'use strict';


var HelloMessage = React.createClass({
  displayName: "HelloMessage",

  render: function render() {
   	return React.createElement(
	      "div",
	        null,
		"Oh shit! React works!"
	);	
	}
});
React.render(React.createElement(HelloMessage,null), 
document.getElementById('content'));
