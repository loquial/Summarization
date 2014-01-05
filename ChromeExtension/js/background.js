function summarizeSelection(info, tab) {
    jQuery.post("http://localhost:5000/sumDoc", {'aDoc':info.selectionText})
    	.done(function(data){
    		chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
				chrome.tabs.sendMessage(tabs[0].id, {"type": "show_summary", "summary":data}, function(response) {
				console.log(response.farewell);
			});
		});
    		console.log(data);
    	}).error(function(){
    		console.log("error");}
	);
};

var title = "Summarize selection";
var id = chrome.contextMenus.create({"title": title, "contexts":["selection"],
	"onclick": summarizeSelection});
console.log("summarize selection item: "+ id);