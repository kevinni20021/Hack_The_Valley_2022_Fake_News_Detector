
// Manifest V3
var obj;

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
   if (changeInfo.status == 'complete' && tab.active) {
       chrome.tabs.query({ active: true, lastFocusedWindow: true }, tabs => {
           let url = tabs[0].url;
           console.log(url);
           setStone(url);
           }) 
       };
   })

async function getData(url) {
    const final = await fetch('http://127.0.0.1:5000/scrape', {
        method: 'POST',
        body: JSON.stringify({url})})
    const response = await final.json();
    return response;
    }

async function setStone(url) {
    this.obj = await getData(url);
    console.log(obj);

}

// async function getData(url) {
//     return fetch('http://127.0.0.1:5000/scrape', {
//         method: 'POST',
//         body: JSON.stringify({url})})
//         .then((response) => response.json())
//         .then((data) => {
//             console.log(data);
//             return data;
//         })
//     }



