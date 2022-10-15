// Manifest V3

chrome.runtime.onInstalled.addListenser(() => {
    chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
        let url = tabs[0].url;
        console.log(url);
    });
});

