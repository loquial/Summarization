// Handle requests for passwords
chrome.runtime.onMessage.addListener(function(request) {
    if (request.type === 'show_summary') {
    	console.log("SUM: "+request.summary);
	d=document.createElement('div');
	$(d).html(request.summary)
		.attr("id","foo")
		.appendTo($("body")) //main div
		.click(function(){
		    $(this).remove();
		})
		.attr("style","position: absolute; width: 350px; border: 1px solid rgb(51, 102, 153); padding: 10px; background-color: rgb(255, 255, 255); z-index: 2001; overflow: auto; text-align: center; top: 149px; left: 497px;")
    }
});