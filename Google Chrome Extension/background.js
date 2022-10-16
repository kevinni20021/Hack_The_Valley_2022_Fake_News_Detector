// Manifest V3
// chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
//     if (changeInfo.status == 'complete' && tab.active) {
//         chrome.tabs.query({ active: true, lastFocusedWindow: true }, tabs => {
//             let url = tabs[0].url;
//             console.log(url)
//             fetch('http://127.0.0.1:5000/scrape', {
//                 method: 'POST',
//                 body: JSON.stringify({url}),
//                 }).then((response) => {
//                     if (response.ok) {
//                         return response.json();
//                     }else {
//                         throw new Error("NETWORK RESPONSE ERROR");
//                       }})
//                 .then((data) => {
//                     console.log(data);
//                     doStuff(data);
//                 }).catch((error) => console.error("FETCH ERROR:", error));;
//             })
//         };
//     })

// function doStuff(data) {
//     var a = data.title;
//     var b = data.score;
//     var c = data.summary;
//     var d = data.related1;
//     var e = data.related2;
//     var f = data.related3;
//     document.getElementById("Title").textContent= a;
//     document.getElementById("TF").textContent= b;
//     document.getElementById("Summary").textContent=c;
//     document.getElementById("ref1").textContent=d;
//     document.getElementById("ref2").textContent= e;
//     document.getElementById("ref3").textContent= f;
// }
// // function doStuff(a,b,c,d,e,f) {
// //     document.getElementById("Title").textContent= a;
// //     document.getElementById("TF").textContent= b;
// //     document.getElementById("Summary").textContent=c;
// //     document.getElementById("ref1").textContent=d;
// //     document.getElementById("ref2").textContent= e;
// //     document.getElementById("ref3").textContent= f;
// // }

// // doStuff(a,b,c,d,e,f);
// //
chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
   if (changeInfo.status == 'complete' && tab.active) {
       chrome.tabs.query({ active: true, lastFocusedWindow: true }, tabs => {
           let url = tabs[0].url;
           console.log(url)
           fetch('http://127.0.0.1:5000/scrape', {
               method: 'POST',
               body: JSON.stringify({url}),
               }).then((response) => response.json())
               .then((data) => console.log(data))
           })
       };
   })