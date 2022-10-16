// Manifest V3

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    if (changeInfo.status == 'complete' && tab.active) {
        chrome.tabs.query({ active: true, lastFocusedWindow: true }, tabs => {
            let url = tabs[0].url;
            console.log(url)
            fetch('http://127.0.0.1:5000/scrape', {
                method: 'POST',
                body: JSON.stringify({url}),
                })
            }).then((data) => console.log(data.text()))
        };
    })